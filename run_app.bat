@echo off
echo ===================================================
echo   AutoSight - Automotive Market Analysis Launcher
echo ===================================================

echo.
echo [1/2] Starting Backend Server...
start "AutoSight Backend" cmd /k "cd backend && pip install -r requirements.txt && python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

echo.
echo [2/2] Starting Frontend Application...
echo Installing dependencies (this may take a minute)...
start "AutoSight Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo ===================================================
echo   Application is starting!
echo   Backend: http://localhost:8000/docs
echo   Frontend: http://localhost:3000
echo ===================================================
echo.
pause
