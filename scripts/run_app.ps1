# Launch Script for Pizza Modern Data Warehouse & AI Predictive Suite
# Runs FastAPI backend and serves the high-performance React application

Write-Host "🍕 Starting Pizza Predictive Intelligence Suite..." -ForegroundColor Cyan

# Check if frontend is built, if not, build it
if (-not (Test-Path "frontend\dist")) {
    Write-Host "Building React Single Page Application..." -ForegroundColor Yellow
    npm run build --prefix frontend
}

Write-Host "🔥 Launching FastAPI Server on http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "Opening web application in your default browser..." -ForegroundColor Cyan

# Start browser after a brief delay
Start-Process "http://127.0.0.1:8000"

# Launch Uvicorn
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
