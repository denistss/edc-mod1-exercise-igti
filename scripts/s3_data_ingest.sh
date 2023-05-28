#!/usr/bin/env bash 

PACKAGE="../interact_s3.py"

echo "Baixando dependencias para virtualenv windows"

python -m venv envdados
envdados/Scripts/activate.bat
envdados/Scripts/pip.exe install -r requirements.txt

echo "Executando ingestão com arquivo python "$PACKAGE"..."
envdados/Scripts/python $PACKAGE

# echo "Excluindo virtual env local"
# envdados/Scripts/deactivate.bat
# rm -r envdados