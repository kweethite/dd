import requests
url = 'http://phyuphyuhtwe.rf.gd/log.php'

data = {'user':'thite','pass':'thitethite'}


site = requests.post(url,data=data)

print (site.text)

