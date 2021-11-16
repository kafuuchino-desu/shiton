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

    encodeTime = input("please specify encode times(default 1, enter to use default: ")
    if encodeTime == "":
        encodeTime = 1
    else:
        try:
            encodeTime = int(encodeTime)
        except:
            print("input error, using default")
            encodeTime = 1

    for i in range(0, encodeTime):
        if (i == 0):
            payload = b64obfuscate(code)
        else:
            payload = b64obfuscate(payload)

    #filePath = input("please specify output file(file path supported)\n")
    filePath = "out.py"

    #apply imports
    payload = "import base64;" + payload

    try:
        with open(filePath, 'w') as handle:
            handle.write(payload)
    except:
        print(traceback.format_exc())
