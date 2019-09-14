#! /bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/../config/credentials.json
python3 test.py
