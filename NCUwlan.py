import requests
import os
import subprocess
from urllib.error import HTTPError,URLError

def connect(url):#模拟登陆
    a=int(input('请输入你的学号：'))
    b=int(input('请输入你的密码：'))
    data = {}
    data['username'] =a
    data['password'] =b
    data['action'] = 'login'
    data['ac_id'] = '1'
    data['ajax'] = '1'
    data['save_me'] = '1'
    try:
         response = requests.post(url, data=data)
    except(HTTPError,URLError) as e:
        return "网站打不开了"
    result = response.text
    if result=='E2531: User not found.(用户不存在)':
        print('用户名或密码错误')
    elif result == 'login_ok,,bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYylaIyRwWQJyHmghiXI7rP7DovwSAKtpjehun7z0HvoBLzohAdX8jBhz%2FOfdpyICut9fm1nx%2B8U5fF%2FWc9tQHFK3IXghvBBzFG96PUVJUDNpZdZq%2FHLWFN5h%2BeBAV3kQTpKXSmUt0xpqRJf2MbdtM3Irh5eO1vBakg%3D%3D':
        print('登录成功')
    elif result == 'E2553: Password is error.(å¯ç éè¯¯)':
        print('密码错误')
    elif result == 'E2532: The two authentication interval cannot be less than 10 seconds.(ä¸¤æ¬¡è®¤è¯çé´éå¤ªç­)':
        print('2次验证不要超过10秒')
connect('http://aaa.ncu.edu.cn:804/include/auth_action.php')


fnull = open(os.devnull, 'w')#检测是否联网
result = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
fnull.close()
while result:
    connect('http://aaa.ncu.edu.cn:804/include/auth_action.php')
else:
    print('true')






















