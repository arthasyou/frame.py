def encodeDict(d):
    return {key.encode('utf-8'): value.encode('utf-8') for (key, value) in d.items()}

def decodeDict(d):
    return {key.decode('utf-8'): value.decode('utf-8') for (key, value) in d.items()}

def decodemsg(msg):
    pass