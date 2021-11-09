# -*- coding: utf-8 -*-
import base64

header = "exec(base64.b64decode("
footer = "))"

def b64obfuscate(payload: str):
    payload = header + str(base64.b64encode(str(payload).encode('utf-8'))) + footer
    return payload
