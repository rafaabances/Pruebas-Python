# Para ello requerimos usar urllib2:

import time, urllib2
 
def gethtml(url):
try:
req = urllib2.Request(url)
return urllib2.urlopen(req).read()
except Exception, e:
time.sleep(2)
return ''
url = 'https://www.manejandodatos.es'
print gethtml(url)