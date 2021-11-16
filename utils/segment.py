# -*- coding: utf-8 -*-
from utils.b64pack import b64obfuscate

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

def wrap_seg_b64(source: str):
    payload = "payload += base64.b64decode(" + b64obfuscate(source) + ").decode('utf-8');"
    return payload

def payload_execute(payload):
    return (payload + "exec(payload);")

    
