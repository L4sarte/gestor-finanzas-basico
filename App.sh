#!/bin/bash

# Ruta a tu intérprete de Python (puede ser python o python3)
PYTHON_INTERPRETER="python3"

# Nombre de tu script de Python
SCRIPT_PYTHON="app.py"

echo "Ejecutando script Python..."
# Ejecuta el script
$PYTHON_INTERPRETER $SCRIPT_PYTHON

# Opcional: Si tu script .py ya tiene permisos de ejecución (#!/usr/bin/env python3)
# puedes ejecutarlo directamente con:
# ./mi_script.py

# Pausar la terminal para ver la salida si no hay otra salida (opcional)
# read -p "Presiona Enter para salir..."

