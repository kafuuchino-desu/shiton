# -*- coding: utf-8 -*-

def split_seg(payload: str):

    segments = []
    code = ""

    for line in payload.splitlines():
        if line != "":
            code += line
            code += "\n"
        else:
            segments.append(code)
            code = ''
    if code != '':
        segments.append(code)

    return segments
