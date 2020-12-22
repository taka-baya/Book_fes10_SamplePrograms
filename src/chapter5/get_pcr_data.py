from bs4 import BeautifulSoup as bs4
import requests

url ="https://www.mhlw.go.jp/content/pcr_positive_daily.csv"
response = requests.get(url)
soup = bs4(response.content, "lxml", from_encoding="utf-8")

data = soup.string.split("\n")
data_list=[]

for s in data:
    data_list.append(s.replace('\r', '').split(","))

print(data_list[1][1])



