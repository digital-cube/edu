from bs4 import BeautifulSoup
import urllib.request
import hashlib

search4 = \
    ['Balkan', 'Energy', 'Balkan Energy',
     'Reports', 'Business', 'services']

search4=[s.lower() for s in search4]

parsed = set()

def get(url):

    if not url:
        return False

    fname = 'cache/cache-{}'.format(hashlib.md5(url.encode('utf-8')).hexdigest())

    try:
        with open(fname,'rb') as f:
            print('reading from cache {}'.format(fname))
            return f.read()
    except:
        pass

    try:
        content = urllib.request.urlopen(url).read()

        try:
            with open(fname, 'wb') as f:
                f.write(content)
        except:
            print("Error creating cache file")

    except:
        return False

    return content

def fetch_and_parse(url, results, level):

    global parsed

    if url in parsed:
        return

    if level>1:
        return

    print('fetch_and_parse :: {}\t{}.'.format(level, url))

    content = get(url)

    if not content:
        return False

    soup = BeautifulSoup(content, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text().lower()

    occ = []
    for s in search4:
        c = text.count(s)
        if c > 0:
            occ.append((s, c))

    print(occ)

    parsed.add(url)

    results[url] = {
        'url': url,
        'occurance': occ,
        'links': {}
    }

    links = set()
    for link in set([link.get('href') for link in soup.find_all('a')]):
        if not link:
            continue
        if         link[:7].lower()  == 'mailto:' \
                or link[:11].lower() == 'javascript:' \
                or link[:4].lower()  == 'tel:' \
                or link[:24].lower( )== 'https://www.youtube.com/' \
                or link[0] == '#':
            continue
        if link[0] == '/':
            link = 'http://SITE.COM'+link

        links.add(link)

    for link in links:
        fetch_and_parse(link,
                        results[url]['links'], level+1)


def devel(uri):

    content = get(uri)

    soup = BeautifulSoup(content, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text().lower()

if __name__ == "__main__":

    results = {}

    # fetch_and_parse("http://balkangreenenergynews.com/", results, 0)

    devel('http://balkangreenenergynews.com/')

    print(results)