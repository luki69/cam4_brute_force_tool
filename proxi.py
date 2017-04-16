import requests
from bs4 import BeautifulSoup

out = ""
urls = ["http://www.us-proxy.org/","http://free-proxy-list.net/uk-proxy.html","http://free-proxy-list.net/anonymous-proxy.html"]
for url in urls:
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, "html.parser")
  tr = soup.find_all("tr")
  for t in tr:
    td = t.find_all("td")
    if (td):
      if (td[6].text=="no"): # If you change "no" to "yes" you get https
        out+=(td[0].text+":"+td[1].text+"\n")
f = open("proxy.txt", "w")
f.write(out)
f.close()
