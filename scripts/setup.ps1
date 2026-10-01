# Automated Setup Script for Pizza MDW & Predictive Intelligence

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Setting up Pizza MDW Environment (Windows PowerShell)..." -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Create Virtual Environment if not present
if (-not (Test-Path ".venv")) {
    Write-Host "[1/3] Creating Python virtual environment in .venv..." -ForegroundColor Yellow
    python -m venv .venv
} else {
    Write-Host "[1/3] Virtual environment (.venv) already exists." -ForegroundColor Green
}

# 2. Activate Virtual Environment
Write-Host "[2/3] Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# 3. Upgrade pip and install requirements
Write-Host "[3/3] Installing dependencies from requirements.txt..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "`nEnvironment setup completed successfully!" -ForegroundColor Green
Write-Host "To launch the app: streamlit run app.py (or run .\scripts\run_app.ps1)" -ForegroundColor Cyan
