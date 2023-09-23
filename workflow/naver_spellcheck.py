#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Naver SpellChecker Workflow for Alfred 4
# Copyright (c) 2022 Kyeongwon Lee <kwlee1718@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
sys.path.append("lib")
import re
from workflow.workflow import Workflow
from hanspell_break import get_spell_check_data

def main(wf):
    args = wf.args[0]

    end_mark = re.search('\s+$', args)
    if end_mark:
        checked = get_spell_check_data(args)
        out = checked.rstrip()

        wf.add_item(
            title=out,
            subtitle="맞춤법 수정 결과 복사",
            arg=out,
            autocomplete=out,
            valid=True)

        wf.add_item(title=args,
                subtitle="원본 텍스트 복사",
                autocomplete=args,
                arg=args,
                valid=True)

        wf.send_feedback()
    else:
        wf.logger.debug("args: %s" % args)
        wf.add_item(title=u'문장 마지막에 반드시 공백을 1개 이상 입력해주세요.', valid=False)
        wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
