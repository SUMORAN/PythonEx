# coding=utf-8
from requests import get
from lxml.html import fromstring
import pandas as pd
from bs4 import BeautifulSoup
from random import choice
import time
# import sys
# reload(sys) 
# sys.setdefaultencoding('utf-8') 

# 设置多个agent选择
uas = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]
    
# 设置代理IP
# def get_ip():
#     """获取代理IP"""
#     url1 = "http://www.xicidaili.com/nn"
#     headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
#                 "Accept-Encoding":"gzip, deflate, sdch",
#                 "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
#                 "Referer":"http://www.xicidaili.com",
#                 "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
#                 }
#     r = get(url1,headers=headers)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     data = soup.table.find_all("td")
#     ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
#     port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
#     ip = re.findall(ip_compile,str(data))       # 获取所有IP
#     port = re.findall(port_compile,str(data))   # 获取所有端口
#     return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080

# proxies = {
#             "http":ip,
#         }

header = {'User-Agent':choice(uas),'Connection': 'close'}
# file = open('52donkey.meniwen.txt','wb','utf-8')
df = pd.DataFrame(columns = ["paragraph", "tags"]) #create a dataframe

for page in range(1,7):
    ### get article url in each page
    url = 'http://www.52donkey.com/meiwen/page/'+ str(page) +'/'
    print('url: '+ url + '\n')
    response = ''
    #下述while解决由于请求失败而由程序本身发送重连连接的速度过快导致产生的Max retries exceeded问题
    while response == '':
        try:
            response = get(url,headers = header).text
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    page_response = fromstring(response)
    print('page'+str(page_response)+':\n')
    articles = page_response.findall(".//h2[@class='entry-title']//a")
    num = 0
    for item in articles:
        num+=1
        print('article ' + str(num) +'\n')
        article_href = item.get('href')

        ### open every article html page, get each paragrapf and tags
        article_response = ''
         #下述while解决由于请求失败而由程序本身发送重连连接的速度过快导致产生的Max retries exceeded问题
        while article_response == '':
            try:
                article_response = get(article_href, headers = header).text
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        # article_response = get(article_href, headers = headers,proxies=proxies).text
        article_content = fromstring(article_response)
        paragraph = article_content.findall(".//div[@class='single-content']//p")
        tags = article_content.findall(".//div[@class='single-tag']//ul//li//a")

        ### concat tags
        tags_content = ""
        for tag in tags:
            tags_content = tag.text + ',' + tags_content
        for para in paragraph:
            # print(para.text_content().encode('gbk','ignore').decode('gbk'))
            df.loc[df.shape[0]+1] = {'paragraph':para.text_content(),'tags':tags_content}
            # file.write(para.text_content() + '\n')
df.to_csv('52donkey.meiwen.csv',sep='\t', encoding="utf-8")
# file.close()
print('Done!')