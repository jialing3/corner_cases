import urllib2
import bs4
from random import shuffle
import os
#from unicodedata import normalize

url_base = 'http://www.weeklysh.com/eNews/Wap.aspx?ID='
ids = range(150340, 151531)
shuffle(ids)
i = ids.index(151414)
ids = [ids[i]] + ids[:i] + ids[i+1:]

os.chdir('/Users/jialing/Shanghai')

for id in ids:
    page = urllib2.urlopen(url_base + str(id))
    soup = bs4.BeautifulSoup(page.read())
    try:
        title, content = soup.findAll('div')
    except:
        continue
    title = title.getText().strip()
    content = content.getText('\n' * 2).strip()
    try:
        author, content = content.split('\n', 1)
    except:
        continue
    filename = author + '/' + title + '.txt'
    #filename = normalize('NFC', filename).encode('utf-8')
    if len(author) > 10: # skip long names
        continue
    if not os.path.exists(author):
        try:
            os.makedirs(author)
        except:
            continue
    try:
        with open(filename, 'w') as f:
            to_write = title + '\n' * 2 + author + '\n' * 2 + content + '\n' * 2
            to_write = to_write.encode('utf-8')
            f.write(to_write)
    except:
        continue
    print id, author, title
