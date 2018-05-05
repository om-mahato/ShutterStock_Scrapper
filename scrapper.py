import urllib.request
from urllib.request import urlretrieve
import urllib.parse

from bs4 import BeautifulSoup

try:
    for j in range(1, 5):
        url='https://www.shutterstock.com/search?searchterm=programming&sort=popular&image_type=all&search_source=base_landing_page&language=en&page='+str(j)

        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        print("connection ok")
        respData = resp.read()
        resp.close()
        print('Done')
        soup = BeautifulSoup(respData, "html.parser")

        div = soup.find_all('div',{'class':'img-wrap'})
        for i in range(0, len(div)-1):
            img = div[i].find_all('img')
            
            image_src = img[0].get('src')
            name = image_src.rsplit('/',1)[-1]
            try:
                urlretrieve(image_src, name)
                print('Downloaded image of ' + name)
            except Exception as ee:
                print(str(ee))
                pass
        
except Exception as e:
    print(str(e))
    