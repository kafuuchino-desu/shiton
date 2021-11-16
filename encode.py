# -*- coding: utf-8 -*-

import traceback
import utils.b64pack as b64pack
import utils.segment as segment

if __name__ == "__main__":
    filePath = input("please input the file name(file path supported)\n")

    try:
        with open(filePath, 'r') as handle:
            code = handle.read()
    except:
        print(traceback.format_exc())

    encodeTime = input("please specify maximum random encode times(default 5, enter to use default, 0 to disable): ")
    if encodeTime == "":
        encodeTime = 5
    else:
        try:
            encodeTime = int(encodeTime)
            if encodeTime < 0:
                print("negative is not allowed, using default")
                encodeTime = 5
        except:
            print("input error, using default")
            encodeTime = 5

    segs = segment.split_seg(code)
    payload = 'payload = \'\';'

    for seg in segs:
        if encodeTime == 0:
            payload += segment.wrap_seg_b64(seg)
        else:
            payload += b64pack.multi_b64wrap(segment.wrap_seg_b64(seg), encodeTime)
    payload = segment.payload_execute(payload)
    #print(payload)

    #apply executor
    segment.payload_execute(payload)

    if encodeTime != 0:
        for i in range(0, encodeTime):
            payload = b64pack.b64wrap(payload)

    #filePath = input("please specify output file(file path supported)\n")
    filePath = "out.py"

    #apply imports
    payload = "import base64;" + payload

    try:
        with open(filePath, 'w') as handle:
            handle.write(payload)
    except:
        print(traceback.format_exc())
