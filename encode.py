# -*- coding: utf-8 -*-

import traceback
from utils.b64pack import b64obfuscate
from utils.segment import split_seg 

if __name__ == "__main__":
    filePath = input("please input the file name(file path supported)\n")

    try:
        with open(filePath, 'r') as handle:
            code = handle.read()
    except:
        print(traceback.format_exc())

    segments = list(reversed(split_seg(code)))
    payload = ""

    #for seg in segments:
    #    payload = b64obfuscate(seg) + ';' + payload
    payload = b64obfuscate(code)

    #filePath = input("please specify output file(file path supported)\n")
    filePath = "out.py"

    #apply imports
    payload = "import base64;" + payload
    try:
        with open(filePath, 'w') as handle:
            handle.write(payload)
    except:
        print(traceback.format_exc())
