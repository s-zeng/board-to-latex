#!/bin/bash
 export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/config/credentials.json
 export MATHPIX_CREDENTIALS=$(pwd)/config/mathpix.json

 ./terminal.py $1 > output.tex

 exit_status=$?

 if [ $exit_status -eq 0 ]; then
     pdflatex output.tex
     evince output.pdf
     rm output.tex
 fi
