#!/bin/bash

echo "Criando venv..."
python3 -m venv venv

echo "Ativando venv..."
source venv/bin/activate

echo "Pip install..."
pip install --upgrade pip
pip install -r requirements.txt

# Passo 5: Rodar o aplicativo FastAPI
echo "Running FastAPI..."
python3 app.py