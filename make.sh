#!/bin/sh

# todo?: run workflow without python3
# pyinstaller --additional-hooks-dir=workflow workflow/naver_spellcheck.py

rm -rf ./NaverSC.alfredworkflow
cd workflow
echo "" > TOKEN.txt
zip -r ../NaverSC.alfredworkflow . -x "__pycache__/*" "**/__pycache__/*"