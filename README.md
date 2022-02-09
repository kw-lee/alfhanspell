alfhanspell : Naver SpellChecker Workflow for Alfred
==============

Naver SpellChecker Workflow for Alfred

Alfred에서 네이버 맞춤법 검사를 실시하는 워크플로우

Install workflow
--------------
 `NaverSC.alfredworkflow`를 다운로드 받아서 실행한다.

Usage
--------------
* `nsc {query}` {query} 자리에 원하는 문장을 입력하면 맞춤법 수정 결과와 원본 텍스트를 복사하실 수 있습니다.

![](./nsc_test.gif)

Build
--------------
```bash
bash ./make.sh
```

Requirements
--------------

```bash
git submodule update --init --recursive
pip install -r requirements.txt -t workflow/lib
```

LICENSE
--------------
 - MIT
 - except for requests library (Apache License 2.0)