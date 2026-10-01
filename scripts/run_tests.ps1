# Run Smoke Tests Script

Write-Host "Running Platform Smoke Tests..." -ForegroundColor Cyan

if (Test-Path ".venv\Scripts\Activate.ps1") {
    & .\.venv\Scripts\Activate.ps1
}

python -m unittest discover -s tests -v
