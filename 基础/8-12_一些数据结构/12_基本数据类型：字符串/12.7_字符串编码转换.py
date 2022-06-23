'''编码
    encode()方法 参数是编码格式'''
s='天涯共此时'
print(s.encode(encoding='GBK')) #在gbk这种编码格式中 一个中文占两个字节  b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s.encode(encoding='UTF-8')) #在utf——8这种编码格式中 一个中文占三个字节  b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'
'''解码
    byte.decode()方法
    编码格式和解码格式要一致
    '''
byte = s.encode('GBK') #编码
print(byte.decode(encoding='GBK')) #天涯共此时 解码