import sys
print(sys.version_info)
print(sys.version)

def do_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        try:
            value = bytes_or_str.decode('utf-8')
        except UnicodeDecodeError:
            # UTF-8로 디코딩할 수 없는 경우 다른 인코딩 시도
            try:
                value = bytes_or_str.decode('latin-1')
            except UnicodeDecodeError:
                # 그래도 안 되면 'replace' 사용 ( 문자로 대체)
                value = bytes_or_str.decode('utf-8', errors='replace')
    else:
        value = bytes_or_str
    return value # str 인스턴스

print("=== 정상적인 UTF-8 바이트 ===")
print(repr(do_str(b'foo')))
print(repr(do_str('bar')))

print("\n=== 잘못된 UTF-8 바이트 (UnicodeDecodeError 발생) ===")
print(repr(do_str(b'foo\xffbar')))

print("\n=== 다른 잘못된 바이트 예제 ===")
print(repr(do_str(b'\xff\xfe\xfd')))
print(repr(do_str(b'안녕하세요'.encode('utf-8'))))  # 올바른 UTF-8
print(repr(do_str(b'\xe4\xb8\xad\xe6\x96\x87')))  # UTF-8로 인코딩된 '中文'