function Show-Tree {
    param (
        [string]$Path = ".",
        [int]$Depth = 3,
        [int]$CurrentLevel = 1
    )

    Get-ChildItem -Path $Path | ForEach-Object {
        $indent = " " * (4 * ($CurrentLevel - 1))
        if ($_.PSIsContainer) {
            Write-Output "$indent|-- $($_.Name)"
            if ($CurrentLevel -lt $Depth) {
                Show-Tree -Path $_.FullName -Depth $Depth -CurrentLevel ($CurrentLevel + 1)
            }
        } else {
            Write-Output "$indent|-- $($_.Name)"
        }
    }
}

Show-Tree -Path . -Depth 3
