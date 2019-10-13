#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/config/credentials.json
export MATHPIX_CREDENTIALS=$(pwd)/config/mathpix.json
#export TEXINPUTS=.:/opt/tex/cur/texmf-dist/tex/latex/latexconfig/

./terminal.py $1 > output.tex

exit_status=$?

if [ $exit_status -eq 0 ]; then
    pdflatex output.tex
    zathura output.pdf
#    rm output.tex
fi
