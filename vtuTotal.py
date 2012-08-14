import urllib
import urllib2
from bs4 import BeautifulSoup
import json

#the URL
url = 'http://www.vtupwn.appspot.com/json/results'
print 'Enter USN : '
usn = raw_input()
usn = usn.strip().upper()
values = {"usn":usn}
data = urllib.urlencode(values)
request = urllib2.Request(url,data)
print 'Fetching data...'
response = urllib2.urlopen(request)
page = response.read()
json_res = json.loads(page)
if json_res['isOut'] != True:
  print 'Call failed! Check the USN or the results are not out yet'
  exit()
soup = BeautifulSoup('<html>'+json_res['table']+'</html>')
lst_table = soup.find_all('table')
total_tab = lst_table[len(lst_table)-1]
soup1 = BeautifulSoup('<html>'+str(total_tab)+'</html>')
lst_td = soup1.find_all('td')
total = lst_td[3]
total = str(lst_td[3].text.strip())
print 'Total Marks : '+total
