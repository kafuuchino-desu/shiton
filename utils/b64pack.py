# -*- coding: utf-8 -*-
import base64
import random

header = "exec(base64.b64decode("
footer = "))"

def b64obfuscate(payload: str):
    payload = str(base64.b64encode(str(payload).encode('utf-8')))
    return payload

def b64wrap(payload: str):
    return (header + b64obfuscate(payload) + footer)

def multi_b64wrap(payload: str, maximum: int):
    for i in range(1, random.randint(0, maximum)):
        payload = b64wrap(payload) + ";"
    return payload
