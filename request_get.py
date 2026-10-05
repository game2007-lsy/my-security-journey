import requests
url="https://www.baidu.com"
response=requests.get(url)
print("状态码是：",response.status_code)
print("响应头是：",response.headers)
