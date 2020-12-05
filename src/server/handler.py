
def head(stream):
    data = await stream.read_bytes(2)
    return data
    