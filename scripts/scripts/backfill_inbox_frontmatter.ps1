# 给 inbox 根目录下没有 interest / next_step 的 .md 文章补全 frontmatter
# 用法：在仓库根目录执行 .\scripts\scripts\backfill_inbox_frontmatter.ps1

$inboxPath = Join-Path $PSScriptRoot "..\..\inbox"
$files = Get-ChildItem -Path $inboxPath -Filter "*.md" -File | Sort-Object Name
$updated = 0

foreach ($f in $files) {
    $content = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8
    $parts = $content -split "---", 3
    if ($parts.Count -ne 3) { continue }
    $front = $parts[1].Trim()
    $body = $parts[2]
    $changed = $false
    if ($front -notmatch "interest:") {
        $front = $front + "`ninterest: medium"
        $changed = $true
    }
    if ($front -notmatch "next_step:") {
        $front = $front + "`nnext_step: skim"
        $changed = $true
    }
    if ($changed) {
        $newContent = "---`n" + $front + "`n---" + $body
        [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.UTF8Encoding]::new($false))
        $updated++
        Write-Host $f.FullName
    }
}

Write-Host "Done. Updated $updated of $($files.Count) files."
