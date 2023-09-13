REM Set the desired port number here
set PORT=3000

REM Run uvicorn with the specified settings
uvicorn main:app --host 0.0.0.0 --port %PORT% --reload
