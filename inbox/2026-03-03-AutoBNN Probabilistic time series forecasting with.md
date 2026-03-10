---
interest: medium
link: http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html
next_step: skim
priority: high
slack_ts: '1773132424.460799'
source: Google AI Blog
status: unread
title: 'AutoBNN: Probabilistic time series forecasting with compositional bayesian
  neural networks'
---
# AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks
> 原文: [http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html)

Posted by Urs Köster, Software Engineer, Google Research
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd5Wc54p1HvgIokpazxDsMo1u6i9wg3ovpNOiFc4-wYwebETvjs9-hm2wxZ4osNbBAxhet8To3hwGg-whFScksHQB_BP1kS4Z8Cu7FQT2bjVtJl4trPid-OxCyYocwyRTN66tuvAedu9z0FepBg4zZvmLbLxY6uuib8p5jVH2kfb3RxT_HMABsKMXuSFXr/s320/AutoBNN.jpg)

[Time series](https://en.wikipedia.org/wiki/Time_series) problems are ubiquitous, from forecasting weather and traffic patterns to understanding economic trends. [Bayesian](https://en.wikipedia.org/wiki/Bayesian_inference) approaches start with an assumption about the data's patterns (prior probability), collecting evidence (e.g., new time series data), and continuously updating that assumption to form a posterior probability distribution. Traditional Bayesian approaches like [Gaussian processes](https://gaussianprocess.org/gpml/) (GPs) and [Structural Time Series](https://blog.tensorflow.org/2019/03/structural-time-series-modeling-in.html) are extensively used for modeling time series data, e.g., the commonly used [Mauna Loa CO2](https://gml.noaa.gov/ccgg/trends/) dataset. However, they often rely on domain experts to painstakingly select appropriate model components and may be computationally expensive. Alternatives such as neural networks lack interpretability, making it difficult to understand how they generate forecasts, and don't produce reliable confidence intervals.

To that end, we introduce [AutoBNN](https://github.com/tensorflow/probability/tree/main/spinoffs/autobnn), a new open-source package written in [JAX](https://github.com/google/jax). AutoBNN automates the discovery of interpretable time series forecasting models, provides high-quality uncertainty estimates, and scales effectively for use on large datasets. We describe how AutoBNN combines the interpretability of traditional probabilistic approaches with the scalability and flexibility of neural networks.

AutoBNN
-------

AutoBNN is based on a [line](https://proceedings.mlr.press/v28/duvenaud13.html) [of](https://royalsocietypublishing.org/doi/10.1098/rsta.2011.0550) [research](https://proceedings.mlr.press/v202/saad23a.html) that over the past decade has yielded improved predictive accuracy by modeling time series using GPs with learned [kernel](https://www.cs.toronto.edu/~duvenaud/cookbook/) structures. The kernel function of a GP encodes assumptions about the function being modeled, such as the presence of trends, periodicity or noise. With learned GP kernels, the kernel function is defined compositionally: it is either a base kernel (such as `Linear`, `Quadratic`, `Periodic`, `Matérn` or `ExponentiatedQuadratic`) or a composite that combines two or more kernel functions using operators such as `Addition`, `Multiplication`, or `ChangePoint`. This compositional kernel structure serves two related purposes. First, it is simple enough that a user who is an expert about their data, but not necessarily about GPs, can construct a reasonable prior for their time series. Second, techniques like [Sequential Monte Carlo](https://www.stats.ox.ac.uk/~doucet/doucet_defreitas_gordon_smcbookintro.pdf) can be used for discrete searches over small structures and can output interpretable results.

AutoBNN improves upon these ideas, replacing the GP with [Bayesian neural networks](https://www.cs.toronto.edu/~duvenaud/distill_bayes_net/public/) (BNNs) while retaining the compositional kernel structure. A BNN is a neural network with a probability distribution over weights rather than a fixed set of weights. This induces a distribution over outputs, capturing uncertainty in the predictions. BNNs bring the following advantages over GPs: First, training large GPs is computationally expensive, and traditional training algorithms scale as the cube of the number of data points in the time series. In contrast, for a fixed width, training a BNN will often be approximately linear in the number of data points. Second, BNNs lend themselves better to GPU and [TPU](https://cloud.google.com/tpu?hl=en) hardware acceleration than GP training operations. Third, compositional BNNs can be easily combined with [traditional deep BNNs](https://arxiv.org/abs/2007.06823), which have the ability to do feature discovery. One could imagine "hybrid" architectures, in which users specify a top-level structure of `Add`(`Linear`, `Periodic`, `Deep`), and the deep BNN is left to learn the contributions from potentially high-dimensional covariate information.

How might one translate a GP with compositional kernels into a BNN then? A single layer neural network will typically converge to a GP as the number of neurons (or "width") [goes to infinity](https://link.springer.com/chapter/10.1007/978-1-4612-0745-0_2). More recently, researchers have [discovered](https://openreview.net/forum?id=gRwh5HkdaTm) a correspondence in the other direction — many popular GP [kernels](https://www.cs.toronto.edu/~duvenaud/cookbook/) (such as `Matern`, `ExponentiatedQuadratic`, `Polynomial` or `Periodic`) can be obtained as infinite-width BNNs with appropriately chosen activation functions and weight distributions. Furthermore, these BNNs remain close to the corresponding GP even when the width is very much less than infinite. For example, the figures below show the difference in the [covariance](https://en.wikipedia.org/wiki/Covariance_matrix#:~:text=In%20probability%20theory%20and%20statistics,of%20a%20given%20random%20vector) between pairs of observations, and [regression](https://en.wikipedia.org/wiki/Kriging) results of the true GPs and their corresponding width-10 neural network versions.

|  |
| --- |
|  |
| Comparison of [Gram matrices](https://en.wikipedia.org/wiki/Gram_matrix) between true GP kernels (top row) and their width 10 neural network approximations (bottom row). |

|  |
| --- |
|  |
| Comparison of regression results between true GP kernels (top row) and their width 10 neural network approximations (bottom row). |

Finally, the translation is completed with [BNN analogues](https://arxiv.org/abs/1905.06076) of the `Addition` and `Multiplication` operators over GPs, and input warping to produce periodic kernels. BNN addition is straightforwardly given by adding the outputs of the component BNNs. BNN multiplication is achieved by multiplying the activations of the hidden layers of the BNNs and then applying a shared dense layer. We are therefore limited to only multiplying BNNs with the same hidden width.

Using AutoBNN
-------------

The AutoBNN [package](https://github.com/tensorflow/probability/tree/main/spinoffs/autobnn) is available within [Tensorflow Probability](https://www.tensorflow.org/probability). It is implemented in [JAX](https://github.com/google/jax) and uses the [flax.linen](https://github.com/google/flax) neural network library. It implements all of the base kernels and operators discussed so far (`Linear`, `Quadratic`, `Matern`, `ExponentiatedQuadratic`, `Periodic`, `Addition`, `Multiplication`) plus one new kernel and three new operators:

* a `OneLayer` kernel, a single hidden layer [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) BNN,
* a `ChangePoint` operator that allows smoothly switching between two kernels,
* a `LearnableChangePoint` operator which is the same as `ChangePoint` except position and slope are given prior distributions and can be learnt from the data, and
* a `WeightedSum` operator.

`WeightedSum` combines two or more BNNs with learnable mixing weights, where the learnable weights follow a [Dirichlet prior](https://en.wikipedia.org/wiki/Dirichlet_distribution). By default, a flat Dirichlet distribution with concentration 1.0 is used.

`WeightedSums` allow a "soft" version of structure discovery, i.e., training a linear combination of many possible models at once. In contrast to structure discovery with discrete structures, such as in [AutoGP](https://proceedings.mlr.press/v202/saad23a.html), this allows us to use standard gradient methods to learn structures, rather than using expensive discrete optimization. Instead of evaluating potential combinatorial structures in series, WeightedSum allows us to evaluate them in parallel.

To easily enable exploration, AutoBNN defines a [number of model structures](https://github.com/tensorflow/probability/blob/main/spinoffs/autobnn/autobnn/models.py) that contain either top-level or internal `WeightedSums`. The names of these models can be used as the first parameter in any of the [estimator](https://github.com/tensorflow/probability/blob/main/spinoffs/autobnn/autobnn/estimators.py) constructors, and include things like `sum_of_stumps` (the `WeightedSum` over all the base kernels) and `sum_of_shallow` (which adds all possible combinations of base kernels with all operators).

|  |
| --- |
|  |
| Illustration of the `sum_of_stumps` model. The bars in the top row show the amount by which each base kernel contributes, and the bottom row shows the function represented by the base kernel. The resulting weighted sum is shown on the right. |

The figure below demonstrates the technique of structure discovery on the N374 (a time series of yearly financial data starting from 1949) from the [M3](https://forecasters.org/resources/time-series-data/m3-competition/) dataset. The six base structures were `ExponentiatedQuadratic` (which is the same as the Radial Basis Function kernel, or [RBF](https://en.wikipedia.org/wiki/Radial_basis_function_kernel) for short), `Matern`, `Linear`, `Quadratic`, `OneLayer` and `Periodic` kernels. The figure shows the MAP estimates of their weights over an ensemble of 32 particles. All of the high likelihood particles gave a large weight to the `Periodic` component, low weights to `Linear`, `Quadratic` and `OneLayer`, and a large weight to either `RBF` or `Matern`.

|  |
| --- |
|  |
| Parallel coordinates plot of the [MAP](https://www.probabilitycourse.com/chapter9/9_1_2_MAP_estimation.php) estimates of the base kernel weights over 32 particles. The `sum_of_stumps` model was trained on the N374 series from the M3 dataset (insert in blue). Darker lines correspond to particles with higher likelihoods. |

By using `WeightedSums` as the inputs to other operators, it is possible to express rich combinatorial structures, while keeping models compact and the number of learnable weights small. As an example, we include the `sum_of_products` model (illustrated in the figure below) which first creates a pairwise product of two `WeightedSums`, and then a sum of the two products. By setting some of the weights to zero, we can create many different discrete structures. The total number of possible structures in this model is 216, since there are 16 base kernels that can be turned on or off. All these structures are explored implicitly by training just this one model.

|  |
| --- |
|  |
| Illustration of the "sum\_of\_products" model. Each of the four WeightedSums have the same structure as the "sum\_of\_stumps" model. |

We have found, however, that certain combinations of kernels (e.g., the product of `Periodic` and either the `Matern` or `ExponentiatedQuadratic`) lead to overfitting on many datasets. To prevent this, we have defined model classes like `sum_of_safe_shallow` that exclude such products when performing structure discovery with `WeightedSums`.

For training, AutoBNN provides `AutoBnnMapEstimator` and `AutoBnnMCMCEstimator` to perform MAP and MCMC inference, respectively. Either estimator can be combined with any of the six [likelihood functions](https://github.com/tensorflow/probability/blob/main/spinoffs/autobnn/autobnn/likelihoods.py), including four based on normal distributions with different noise characteristics for continuous data and two based on the negative binomial distribution for count data.

|  |
| --- |
|  |
| Result from running AutoBNN on the [Mauna Loa CO2](https://gml.noaa.gov/ccgg/trends/) dataset in our example [colab](https://github.com/tensorflow/probability/blob/main/discussion/examples/Forecasting_With_AutoBNN.ipynb). The model captures the trend and seasonal component in the data. Extrapolating into the future, the mean prediction slightly underestimates the actual trend, while the 95% confidence interval gradually increases. |

To fit a model like in the figure above, all it takes is the following 10 lines of code, using the [scikit-learn](https://scikit-learn.org/stable/)–inspired estimator interface:

```
import autobnn as ab

model = ab.operators.Add(
    bnns=(ab.kernels.PeriodicBNN(width=50),
          ab.kernels.LinearBNN(width=50),
          ab.kernels.MaternBNN(width=50)))

estimator = ab.estimators.AutoBnnMapEstimator(
    model, 'normal_likelihood_logistic_noise', jax.random.PRNGKey(42),
    periods=[12])

estimator.fit(my_training_data_xs, my_training_data_ys)
low, mid, high = estimator.predict_quantiles(my_training_data_xs)
```

  

Conclusion
----------

[AutoBNN](https://github.com/tensorflow/probability/tree/main/spinoffs/autobnn) provides a powerful and flexible framework for building sophisticated time series prediction models. By combining the strengths of BNNs and GPs with compositional kernels, AutoBNN opens a world of possibilities for understanding and forecasting complex data. We invite the community to try the [colab](https://github.com/tensorflow/probability/blob/main/discussion/examples/Forecasting_With_AutoBNN.ipynb), and leverage this library to innovate and solve real-world challenges.

Acknowledgements
----------------

*AutoBNN was written by Colin Carroll, Thomas Colthurst, Urs Köster and Srinivas Vasudevan. We would like to thank Kevin Murphy, Brian Patton and Feras Saad for their advice and feedback.*
