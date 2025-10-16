# ========================================
# Complete Dependency Installation Script
# ========================================

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   TRUTH LENS - Complete Dependency Installation       ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Ensure we're in the correct directory
$projectDir = "c:\Users\saif7\OneDrive\Desktop\Fake news Detector"
Set-Location $projectDir

# Activate virtual environment
Write-Host "[1/5] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "[2/5] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet

# Install PyTorch (CPU version for compatibility)
Write-Host "[3/5] Installing PyTorch (this may take 5-10 minutes)..." -ForegroundColor Yellow
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install Transformers
Write-Host "[4/5] Installing Hugging Face Transformers..." -ForegroundColor Yellow
pip install transformers

# Install remaining packages
Write-Host "[5/5] Installing remaining dependencies..." -ForegroundColor Yellow
pip install streamlit opencv-python pillow newspaper3k lxml beautifulsoup4 requests python-dateutil pytest pytest-cov

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║              ✓ Installation Complete!                 ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Verify installation
Write-Host "Verifying installation..." -ForegroundColor Cyan
Write-Host ""

$packages = @("streamlit", "transformers", "torch", "cv2", "newspaper")
foreach ($pkg in $packages) {
    $pkgName = $pkg.Replace("cv2", "opencv-python")
    $importName = $pkg.Replace('-', '_').Replace('3k', '')
    python -c "import $importName" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ $pkgName" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $pkgName" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  Ready to launch! Run: .\launch.ps1" -ForegroundColor White
Write-Host "════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
