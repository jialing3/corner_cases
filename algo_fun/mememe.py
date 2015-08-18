from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, requests, bs4
from collections import Counter

random.seed(random.randint(0, 100))



browser = webdriver.Firefox()
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

from re import compile as _Re

_unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)' ).split

def get_topics(site):
    soup = bs4.BeautifulSoup(requests.request('GET', site).text)
    words = soup.text.strip().split()
    words = [w for w, c in Counter(words).items() if c <= 2 and 4 <= len(w) <= 7 and w.isalpha() and w.istitle()]
    random.shuffle(words)
    len_words = len(words)
    words = [' '.join(pair) for pair in zip(words[:len_words//2], words[len_words//2:])]
    return words

def scroll_down(browser):
    for i in range(5 + random.choice([1,2,3,4,5])):
        browser.execute_script("window.scrollTo(0, " + str(i * (40 + random.choice([3,6,0]) + int(random.expovariate(20)))) + ")")
        browser.execute_script("window.scrollTo(0, " + str(i * (60 + random.choice([3,6,0]) + int(random.expovariate(20)))) + ")")
        browser.execute_script("window.scrollTo(0, " + str(i * (80 + random.choice([3,6,0]) + int(random.expovariate(20)))) + ")")
        time.sleep(1.5 + max(0, random.normalvariate(0.1, 0.6)))
        if random.random() > .8:
            browser.execute_script("window.scrollTo(0, " + str(i * (60 - random.choice([3,6,0]))) + ")")


def browse(q, browser):
    counter = 0
    for i in range(random.choice([1,5])):
        browser.get("https://www.google.com/search?q=" + q + "&start=" + str(counter))
        body = browser.find_element_by_tag_name("body")
        scroll_down(browser)
        links = browser.find_elements_by_partial_link_text(q)
        links[min(random.choice([0,0,1,4,1,0,3,2]), len(links) - 1)].click()
        scroll_down(browser)
        if random.random() > .7:
            time.sleep(10 + random.random() * 5 * random.random())
        elif random.random() > .8:
            while random.random() > .5:
                browser.find_element_by_partial_link_text(random.choice('abcedgtgijr4')).click()
                scroll_down(browser)
                time.sleep(random.random() * 6)
        counter += 10
        time.sleep(3)
        browser.back()
        time.sleep(random.expovariate(.1))

    if random.random() > .9:
        return get_topics("https://www.google.com/search?q=" + q)
    else:
        return []


topics = []
sites = ['http://popurls.com/entertainment', 'https://en.wikipedia.org/wiki/Gibberish', 'https://nl.wikipedia.org/wiki/Computerbeveiliging', 'https://en.wikipedia.org/wiki/Computer_security', 'https://en.wikipedia.org/wiki/Embryology', 'https://en.wikipedia.org/wiki/Particle_physics', 'https://de.wikipedia.org/wiki/Kauderwelsch', 'https://es.wikipedia.org/wiki/Wikipedia:Portada', 'https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal', 'https://www.wikipedia.org', 'http://finance.yahoo.com', 'https://www.yahoo.com', 'http://popurls.com/entertainment', 'http://popurls.com/politics', 'http://popurls.com/design', 'http://www.reddit.com', 'http://www.sciencemag.org/content/current', 'http://www.rottentomatoes.com', 'http://www.latinpost.com', 'http://www.cs.cmu.edu/~bingbin/', 'http://mentalfloss.com', 'https://www.twitter.com', 'https://www.nytimes.com', 'https://www.newyorker.com', 'https://www.yelp.com', 'http://www.cnn.com', 'https://www.venturebeat.com', 'http://www.ycombinator.com']
for site in sites:
    try:
        topics.extend(get_topics(site))
    except:
        print(site)
topics.extend(['fifty shades of grey', 'linkedin', 'facebook', 'Happily', 'Firefly', 'Russian', 'Campfile', 'mitbbs', 'huaren.us'])

new_topics = []
with open('../Desktop/mac_desktop/corner_cases/algo_fun/沈大成/你如此热爱生活.txt') as f:
    for row in f.readlines():
        row = row.strip()
        row = _unicode_chr_splitter(row)
        for i in range(0, len(row), 8):
            new_topics.append(''.join(row[i:i+8]))
new_topics.extend(['Python', 'Ruby', 'Ruby on Rails', 'Spark', 'Java', 'MATLAB', 'Octave', 'C++', 'C', 'Scala'])
print(new_topics)

for _ in range(1000):
    q = random.choice(topics + ['election 2016', 'GOP', 'Clinton', 'election 2016', 'GOP', 'Clinton'])
    if random.random() > .4:
        q = random.choice([q] + [random.choice(new_topics)])
        print(q)
    try:
        topics.extend(browse(q, browser))
    except:
        print(q)
    time.sleep(random.expovariate(13))
    if random.random() > .9:
        print('long sleep')
        time.sleep(60 * 8 * random.random())
    elif random.random() > .2:
        browser.get(random.choice(sites))
        scroll_down(browser)
        browser.get("https://en.wikipedia.org/wiki/Chief_executive_officer")
        scroll_down(browser)
        while random.random() > .2:
            browser.find_element_by_partial_link_text(random.choice('abcedgtg4')).click()
            scroll_down(browser)
            time.sleep(random.random() * 8)
    elif random.random() > .6:
        browser.get(random.choice(["https://www.nytimes.com", 'https://www.stackoverflow.com']))
        scroll_down(browser)
        browser.find_element_by_partial_link_text(random.choice('abcedgtg4')).click()
        scroll_down(browser)
        time.sleep(random.random() * 10)
    elif random.random() > .5:
        browser.get(random.choice(["https://finance.yahoo.com", 'https://www.facebook.com', 'http://sfbay.craigslist.org']))
        scroll_down(browser)
        browser.get("https://en.wikipedia.org/wiki/Chief_executive_officer")
        scroll_down(browser)
        while random.random() > .2:
            browser.find_element_by_partial_link_text(random.choice('abcedgtg4')).click()
            scroll_down(browser)
            time.sleep(random.random() * 8)

browser.quit()
