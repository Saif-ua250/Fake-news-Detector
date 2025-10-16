# ========================================
# NEURO-VERIFY AI - Automated Setup Script
# ========================================
# This script will install all dependencies and start the dev server

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🚀 NEURO-VERIFY AI - FRONTEND SETUP" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if Node.js is installed
Write-Host "📦 Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js is not installed!" -ForegroundColor Red
    Write-Host "Please install Node.js 18+ from: https://nodejs.org" -ForegroundColor Red
    exit 1
}

# Check if npm is installed
try {
    $npmVersion = npm --version
    Write-Host "✅ npm found: v$npmVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ npm is not installed!" -ForegroundColor Red
    exit 1
}

Write-Host "`n📥 Installing dependencies..." -ForegroundColor Yellow
Write-Host "(This may take 2-3 minutes on first run)`n" -ForegroundColor Gray

# Install dependencies
npm install

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Dependencies installed successfully!" -ForegroundColor Green
    
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "🎯 SETUP COMPLETE!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    
    Write-Host "`nTo start the development server, run:" -ForegroundColor Yellow
    Write-Host "  npm run dev" -ForegroundColor Cyan
    
    Write-Host "`nThen open your browser to:" -ForegroundColor Yellow
    Write-Host "  http://localhost:3000" -ForegroundColor Cyan
    
    Write-Host "`n📚 For more info, check:" -ForegroundColor Yellow
    Write-Host "  - README.md (full documentation)" -ForegroundColor Gray
    Write-Host "  - QUICKSTART.md (5-minute guide)" -ForegroundColor Gray
    
    Write-Host "`n" -ForegroundColor White
    
    # Ask if user wants to start dev server now
    $response = Read-Host "Start development server now? (Y/n)"
    if ($response -eq "" -or $response -eq "Y" -or $response -eq "y") {
        Write-Host "`n🚀 Starting development server...`n" -ForegroundColor Green
        npm run dev
    } else {
        Write-Host "`n👋 Run 'npm run dev' when you're ready!`n" -ForegroundColor Yellow
    }
    
} else {
    Write-Host "`n❌ Installation failed!" -ForegroundColor Red
    Write-Host "Please check the error messages above and try again." -ForegroundColor Red
    Write-Host "`nCommon fixes:" -ForegroundColor Yellow
    Write-Host "  1. Delete node_modules: rm -r node_modules" -ForegroundColor Gray
    Write-Host "  2. Delete package-lock.json: rm package-lock.json" -ForegroundColor Gray
    Write-Host "  3. Run: npm install" -ForegroundColor Gray
    exit 1
}
