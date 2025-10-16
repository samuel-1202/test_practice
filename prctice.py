import sys
print(sys.version_info)
print(sys.version)

def do_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

print(repr(do_str(b'foo')))
print(repr(do_str('bar')))
print(repr(do_str(b'foo\xffbar')))
print(repr(do_str('foo\xffbar')))