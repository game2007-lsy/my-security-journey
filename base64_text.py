import base64#引入base64工具箱

text = "liushuoyu"
encoded = base64.b64encode(text.encode('utf-8'))
print("编码结果:",encoded.decode('utf-8'))

decoded = base64.b64decode(encoded).decode('utf-8')
print("解码结果:", decoded)