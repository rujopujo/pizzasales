# Launch Script for Streamlit Dashboard

Write-Host "Starting Pizza MDW Streamlit Application..." -ForegroundColor Cyan

if (Test-Path ".venv\Scripts\Activate.ps1") {
    & .\.venv\Scripts\Activate.ps1
}

streamlit run app.py
