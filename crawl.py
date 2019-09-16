"""import os
import requests
from bs4 import BeautifulSoup

url = 'https://swexpertacademy.com/main/identity/anonymous/login.do'
user = 'newmin123@naver.com'
password = ''

session = requests.session()

params = dict()
params['id'] = user
params['pwd'] = password

res = session.post(url, data = params)
res.raise_for_status()
res = session.get('https://swexpertacademy.com/main/sst/common/userTestList.do?')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
he_coinA1 = soup.select_one('body > div.sub-m > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.status')
he_coinA2 = soup.select_one('body > div.sub-m > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.status')
he_coinB1 = soup.select_one('body > div.sub-m > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.status')
he_coinB2 = soup.select_one('body > div.sub-m > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.status')

print('삼성전자 인재개발원 A형 : ', he_coinA1.get_text())
print('삼성전자 서울대 A형 : ', he_coinA2.get_text())
print('삼성전자 인재개발원 B형 : ', he_coinB1.get_text())
print('삼성전자 서울대 B형 : ', he_coinB2.get_text())
os.system('pause')"""

import requests
from bs4 import BeautifulSoup

def get_dic_search(word):
    url = "http://endic.naver.com/search.nhn?query="+word
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

    comp = ""
    result = ""
    try:
        comp += soup.find('dl',{'class':'list_e2'}).find('dt', {'class':'first'}).find('span', {'class':'fnt_e30'}).find('strong').get_text()
        result += soup.find('dl',{'class':'list_e2'}).find('dd').find('span', {'class':'fnt_k05'}).get_text()
        if(comp != result) :
            result = "없습니다"
    except:
        result = "없습니다"
    return result

dic = dict()
f = open('ingredientsdictionary.txt', encoding='utf-8')
for line in f:
    word = line.split('\n')[0]
    dic[word] = True
f.close()

while(True):
    word = input("word : ")
    result = dic.get(word)
    if result == None :
        print("ingredient list에 없습니다")
        print("사전 : " + get_dic_search(word))
    else :
        print("ingredient list에 있습니다")
