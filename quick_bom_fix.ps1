# Quick BOM fix for critical cosmic project files

$criticalFiles = @(
    "minimal_cre.py",
    "ultimate_cre_integration.py", 
    "quantum_umt_enhancer.py",
    "test_ultimate_integration.py",
    "validate_syntax.py",
    "advanced_evolution.py",
    "physics_of_meaning.py",
    "consciousness_space.py"
)

Write-Host " Fixing BOM for critical files..." -ForegroundColor Yellow

foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        Write-Host "  Processing: $file" -ForegroundColor Gray
        $content = Get-Content -Path $file -Raw
        # Remove BOM by re-saving as UTF-8 without BOM
        $content | Out-File -FilePath $file -Encoding utf8 -NoNewline
        Write-Host "     Fixed" -ForegroundColor Green
    } else {
        Write-Host "   File not found: $file" -ForegroundColor Red
    }
}

Write-Host " Critical files BOM fix complete!" -ForegroundColor Green
