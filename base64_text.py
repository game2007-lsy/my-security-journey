import base64#引入base64工具箱
text = "liushuoyu"#要编码的内容
encoded = base64.b64encode(text.encode('utf-8'))#编码
print("编码结果:",encoded.decode('utf-8'))#打印编码结果
decoded = base64.b64decode(encoded).decode('utf-8')#解码
print("解码结果:", decoded)#打印解码结果
