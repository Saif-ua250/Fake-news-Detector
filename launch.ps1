
# ========================================
# Quick Installation Check & Setup
# ========================================

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║         TRUTH LENS - Quick Setup & Check              ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green

    # Activate venv
    & ".\venv\Scripts\Activate.ps1"

    # Check if streamlit is installed
    Write-Host "Checking dependencies..." -ForegroundColor Yellow

    $streamlitCheck = python -c "import streamlit" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Streamlit is installed" -ForegroundColor Green
        Write-Host ""
        Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Green
        Write-Host "║              🚀 READY TO LAUNCH!                       ║" -ForegroundColor Green
        Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Green
        Write-Host ""
        Write-Host "Starting Truth Lens..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "The app will open in your browser at:" -ForegroundColor White
        Write-Host "http://localhost:8501" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
        Write-Host ""
        streamlit run app.py
    }
    else {
        Write-Host "✗ Dependencies not installed" -ForegroundColor Red
        Write-Host ""
        Write-Host "Running installation..." -ForegroundColor Yellow
        pip install -r requirements.txt
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "✓ Installation complete!" -ForegroundColor Green
            Write-Host ""
            Write-Host "Starting Truth Lens..." -ForegroundColor Cyan
            streamlit run app.py
        }
        else {
            Write-Host ""
            Write-Host "✗ Installation failed" -ForegroundColor Red
            Write-Host "Please check the error messages above" -ForegroundColor Yellow
        }
    }
}
else {
    Write-Host "✗ Virtual environment not found" -ForegroundColor Red
    Write-Host ""
    Write-Host "Running setup script..." -ForegroundColor Yellow
    & ".\setup.ps1"
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "Setup complete! Run this script again to start the app." -ForegroundColor Green
    }
    else {
        Write-Host "✗ Setup failed. Please check setup.ps1 for errors." -ForegroundColor Red
    }
}
