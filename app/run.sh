#! /bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/config/credentials.json
export MATHPIX_CREDENTIALS=$(pwd)/config/mathpix.json
python3 app.py
