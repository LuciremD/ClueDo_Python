#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install tkinter

python3 prepare.py

deactivate