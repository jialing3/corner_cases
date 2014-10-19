import urllib2
import bs4

r = urllib2.urlopen('http://pythonhackers.com/open-source/')
soup = bs4.BeautifulSoup(r)

data = []
for element in soup.find_all('div', class_='row link-box ositem'):
  try:
    link = element.find_all('a', href=True)[1]['href']
    project = element.find('a', class_='project').text
    count = element.find('div', class_='row description').a.text
    description = element.find('div', class_='row description').p.text
    rank = element.find('span').text
    data.append([project, count, link, description, rank])
  except:
    print element

with open('top400pkgs.tsv', 'w') as f:
    f.write('project\tcount\tlink\tdescription\trank\n')
    for row in data:
        f.write('\t'.join([s.encode("utf-8") for s in row]) + '\n')


data = []
for page in range(1, 21):
  r = urllib2.urlopen('http://pypi-ranking.info/alltime?page=' + str(page))
  soup = bs4.BeautifulSoup(r)

  for tr in soup.find('table').find_all('tr'):
    rank = tr.td.text
    project = tr.span.text
    description = tr.p.text
    count = tr.find('td', class_='count').span.text
    s1 = bs4.BeautifulSoup(urllib2.urlopen('http://pypi-ranking.info/' + tr.a['href']))
    link = s1.h2.a['href']
    if tr.find('td', class_='attributes').img:
        fast_growth = 'true'
    else:
        fast_growth = 'false'
    data.append([project, count, link, description, rank, fast_growth])

with open('top1000pkgs_pypi.tsv', 'w') as f:
    f.write('project\tcount\tlink\tdescription\trank\tgrowing_fast\n')
    for row in data:
        f.write('\t'.join([s.encode("utf-8") for s in row]) + '\n')
