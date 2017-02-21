from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import hashlib
import json
import pickle
import os

search4 = ['Serbia', 'Bosnia and Herzegovina', 'Montenegro', 'Kosovo', 'Macedonia', 'Albania', 'Turkey', 'Slovenia', 'Croatia', 'Romania', 'Bulgaria', 'Greece', 'Cyprus energy efficiency', 'renewable energy', 'climate change', 'environment', 'waste', 'water', 'wind', 'solar', 'photovoltaic', 'geothermal', 'biomass', 'biogas', 'CHP', 'cogeneration']

search4=[s.lower() for s in search4]

parsed = set()

def get(url):

    if not url:
        return False

    p = urllib.parse.urlparse(url)
    p.netloc

    os.system('mkdir -p cache/{}'.format(p.netloc))

    fname = 'cache/{}/cache-{}'.format(p.netloc, hashlib.md5(url.encode('utf-8')).hexdigest())

    try:
        with open(fname,'rb') as f:
            # print('reading from cache {}'.format(fname))
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

def fetch_and_parse(url, class2remove, results, level):

    urlparsed = urllib.parse.urlparse(url)


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

    for cls in class2remove:
        for div in soup.find_all("div", {'class': cls}):
            div.decompose()

    text = soup.get_text().lower()

    occ = []
    for s in search4:
        c = text.count(s)
        if c > 0:
            occ.append((s, c))

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
            link = urlparsed.scheme+"://"+urlparsed.netloc+"/"+link

        urlparsed_link = urllib.parse.urlparse(link)

        if urlparsed_link.netloc == urlparsed.netloc:
            links.add(link)

    for link in links:
        fetch_and_parse(link, class2remove, results[url]['links'], level+1)


def devel(uri):

    content = get(uri)

    soup = BeautifulSoup(content, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()


    text = soup.get_text().lower()


if __name__ == "__main__":

    results = {}

    class2remove = ('copyright', 'footer_bottom', 'top_header', 'footer', 'header')

    fetch_and_parse("http://renewablesnow.com", class2remove, results, 0)
    print('-'*100)

    with open('site.pck', 'wb') as f:
        pickle.dump(results, f)

    with open('site.pck', 'rb') as f:
        results = pickle.load(f)

    for i in results:
        for l in results[i]['links']:
            site = results[i]['links'][l]
            print(site['url'])
            print(site['occurance'])
            print('')



    # print(json.dumps(results, indent=4))
