@ECHO OFF
setlocal
set PYTHONPATH=%CD%
python -m unittest discover -p "*_experiment.py"
endlocal