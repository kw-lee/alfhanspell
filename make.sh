#!/bin/sh

# todo: run workflow without python3
# pyinstaller --additional-hooks-dir=workflow workflow/naver_spellcheck.py

rm -rf ./NaverSC.alfredworkflow
cd workflow
rm -rf __pycache__
zip -r ../NaverSC.alfredworkflow .