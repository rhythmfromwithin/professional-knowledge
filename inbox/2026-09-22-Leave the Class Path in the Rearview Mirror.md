---
link: https://netflixtechblog.com/leave-the-class-path-in-the-rearview-mirror-67a85b15b6be?source=rss
slack_ts: '1790137539.264669'
source: Netflix Tech Blog
title: Leave the Class Path in the Rearview Mirror
----2615bd06b42e---4
priority: high
status: unread
interest: medium
next_step: skim
---
# Leave the Class Path in the Rearview Mirror
> 原文: [https://netflixtechblog.com/leave-the-class-path-in-the-rearview-mirror-67a85b15b6be?source=rss----2615bd06b42e---4](https://netflixtechblog.com/leave-the-class-path-in-the-rearview-mirror-67a85b15b6be?source=rss----2615bd06b42e---4)

*Introducing composable, module system native and agent friendly command line tools for modern Java development*

By Danny Thomas, JVM Ecosystem Team

![](https://cdn-images-1.medium.com/max/848/1*AkQlaHO9bwLf_dNp-Z2HZQ.png)

Recent work on the Java language to [pave the on-ramp](https://openjdk.org/projects/amber/design-notes/on-ramp) has made it easier than ever to start a Java program and evolve it using the full language and platform. At the end of that on-ramp lies Java’s mature build and dependency management ecosystem, capable of carrying software to enormous scale and complexity.

That ecosystem reached its maturity by developing strong models for projects, dependencies, and builds. When the [Java Module System](https://openjdk.org/jeps/261) arrived, those models were already serving developers exceptionally well. The module descriptor consequently became just another description of the project to keep in agreement.

We’re excited to announce a preview of [ja](https://github.com/Netflix/ja) and its family of composable tools, that build on the capabilities of the Java Module System to provide a modern command line development experience for Java. We take the module descriptor and make it a complete description of a project, with dependency versions sitting naturally beside its requires directives and module metadata provided through documentation tags:

```
/**  
 * @mainClass com.example.application.Main  
 */  
module com.example.application {  
    requires com.example.framework; // @1.2.3  
}
```

Combined with command line ergonomics you’re used to in other languages, creating and consuming Java modules has never been easier.

### Composable Tools

Java developers have long been exceptionally well served by graphical tools. An IDE formats source, navigates between declarations and usages, presents API documentation, and maintains a compiled view of the project. That experience has been so complete that Java has had less need to expose the same capabilities through small, composable command line tools. Those gaps become quickly apparent when coding agents work with the Java language, with agents frequently struggling to locate dependencies, documentation and sources.

ja only provides command line ergonomics and tool orchestration, each feature is underpinned by a standalone tool. You don’t need to adopt ja to get the benefit of these tools, you can compose them in any way you choose:

* [jig](https://github.com/Netflix/jig) performs module version resolution, compilation and assembly, outputting standard module system arguments for use with other tools. It is also the bridge to and from Maven repositories providing a standalone module proxy and publishing commands
* [jfmt](https://github.com/Netflix/jfmt) formats source using the [Code Conventions for the Java Programming Language](https://www.oracle.com/java/technologies/javase/codeconventions-introduction.html), adapted for the modern Java language. Avoids the very common whitespace, indentation, import ordering and qualified class references introduced in agent written code
* [jist](https://github.com/Netflix/jist) provides source aware symbol search, providing a grep style interface for understanding class files and their associated sources. Gives coding agents access to symbols and sources without indexing, LSPs or MCPs while interoperating with other build tools via an [argument file contract](https://github.com/Netflix/jist/wiki/Project-Integration)
* [jdocserver](https://github.com/Netflix/jdocserver) serves locally browsable API documentation

These projects use the tool discovery and execution capabilities of the platform, and are intended to be installed in your JDK along with the standard tools. They all implement [Tool](https://docs.oracle.com/en/java/javase/25/docs/api/java.compiler/javax/tools/Tool.html) or [ToolProvider](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/spi/ToolProvider.html), allowing them to be run in process.

This is also the tool discovery and execution model for ja. There we use [OptionChecker](https://docs.oracle.com/en/java/javase/25/docs/api/java.compiler/javax/tools/OptionChecker.html) and optional custom metadata to discover which module system options are supported so it can resolve the arguments on behalf of the tool. This provides a seamless transition from your source path modules to the standard JDK tooling such as jdeps, jlink and jshell.

### Maven as a foundation

In a recent survey of the 1,000 most popular artifacts on Maven Central, just 232 had explicit module definitions and another 248 declared automatic module names. The remaining 520 expressed no Java module name opinion. The module system also makes no distinction between namespace and module name, so module-first tooling requires a solution to module naming and location in existing repositories.

Fortunately, Maven Central already gives published artifacts a verified namespace. Publishers prove control of reverse domain group IDs, reflecting Sonatype’s long standing case for [namespaces in public repositories](https://www.sonatype.com/blog/why-namespacing-matters-in-public-open-source-repositories).

We use these conventions to establish a canonical Maven module coordinate, paring a verifiable DNS namespace with the complete module name, for example pkg:maven/com.netflix/com.netflix.tools.ja. For existing modules, authors choose to publish a single Maven relocation pom at the canonical coordinate, to allow for discovery of the original coordinate.

When neither are available, candidates are walked from the root of the namespace using common Maven artifact conventions inferring coordinates from module names. We also bundle a short list of aliases for the most popular modules that don’t use a reverse DNS module name, but we suggest authors should always [namespace their modules](https://blog.joda.org/2017/04/java-se-9-jpms-module-naming.html). The module proxy in jig presents resolved modules using the filename based conventions for module naming, making even automatic modules without stable names safe when used with these tools.

These conventions and location strategies allow the majority of existing artifacts to be discovered using only the module name and version.

### Integrity by default

ALL-UNNAMED has become unfortunately common in Java access options, because of the heavy use of the class path. It hides the source of the technical debt that applications are incurring by allowing such access and becomes increasingly consequential as Java moves toward [Integrity by Default](https://openjdk.org/jeps/8305968). For example, [Preparing to Make Final Mean Final](https://openjdk.org/jeps/500) asks applications to explicitly authorize the modules allowed to mutate final fields.

We allow runtime access requirements to bedeclared as module metadata and carried with the module descriptor throughout the module’s lifecycle. For example a library may record the access it requires:

```
/**  
* @enableFinalFieldMutation com.example.framework  
*/  
module com.example.framework {  
}
```

However, the consuming application remains in control and must explicitly authorize the framework, for it to be available at runtime:

```
/**  
* @mainClass com.example.application.Main  
* @enableFinalFieldMutation com.example.framework  
*/  
module com.example.application {  
    requires com.example.framework; // @1.2.3  
}
```

The command line interface for ja allows the dependency and authorization to be added together:

```
ja require com.example.framework@1.2.3 \  
 --enable-final-field-mutation com.example.framework
```

Without that authorization, dependency resolution fails with an unsatisfied access requirement. Native access follows the same model through @enableNativeAccess and qualified exports and opens are also supported.

Module integrity is ensured by persistent hashes of resolved binary dependencies in a module-info.hash file, sequent resolution verifies those hashes and rejects an artifact that has changed.

We also take a step further than the recent improvements to annotation processor security by treating annotation processing as an explicit code generation step. The resulting sources are alongside regular module source, making them visible in code review and allowing a module to be assembled without executing generator code.

### Make modules your default

We think every Java project should be modular, regardless of the build tool you’re using. If you’re a library author producing automatic modules, we’d encourage you to avoid split packages and produce explicit modules.

You can get started with our tools today with our [installation guide](https://github.com/Netflix/ja).

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=67a85b15b6be)

---

[Leave the Class Path in the Rearview Mirror](https://netflixtechblog.com/leave-the-class-path-in-the-rearview-mirror-67a85b15b6be) was originally published in [Netflix TechBlog](https://netflixtechblog.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
