from flask import Flask,render_template
from flask import Flask
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)


def fip(url):
     request=urllib.request.Request(url)
     response=urllib.request.urlopen(request)
     html=response.read().decode('utf-8')
     result0 = BeautifulSoup(html, 'html.parser')
     result1 = result0.find_all('ul', {'class': {'newslist'}})
     result2 = result0.find_all('ul', {'class': {'txt'}})
     return result1
     return result2
result3=fip('http://news.ncu.edu.cn/')


with open('标题.txt','w') as f:
    for i in result3:
        f.writelines(str(i.get_text()))
    f.close()

@app.route('/')
def index():
    f=open('标题.txt','r')
    a=f.readline()
    b=[]
    while a:
        b.append(a)
        a=f.readline()
    f.close()
    return render_template('for in.html',b=b)

if __name__ == '__main__':
    app.run()







