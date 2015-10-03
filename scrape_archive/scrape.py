# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import copy
import os
import re
import functioncache

URLS = [
    'https://web.archive.org/web/20140809062217/http://dwiel.net/',
    'https://web.archive.org/web/20131103095441/http://dwiel.net/page/2/',
    'https://web.archive.org/web/20100806193852/http://dwiel.net/page/3/',
    'https://web.archive.org/web/20131103151226/http://dwiel.net/blog/category/howto/',
    'https://web.archive.org/web/20131102232007/http://dwiel.net/blog/category/axpress/',
    'https://web.archive.org/web/20131103054625/http://dwiel.net/blog/category/bug-fix/',
    'https://web.archive.org/web/20131103195106/http://dwiel.net/blog/category/house/ceb-press/',
    'https://web.archive.org/web/20131103115437/http://dwiel.net/blog/category/code/',
    'https://web.archive.org/web/20131103144836/http://dwiel.net/blog/category/data-exploration/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/family/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/food/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/house/foundation/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/fyi/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/howto/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/linux/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/music/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/house/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/politics/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/reflection/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/code/script/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/uncategorized/',
    'https://web.archive.org/web/20131103052531/http://dwiel.net/blog/category/house/windows/',
    'https://web.archive.org/web/20131103134101/http://dwiel.net/axpress/',
]

def innerHTML(element):
    return element.decode_contents(formatter="html")    


def extract_archive_url(href):
    return href[href.find('http'):]


def convert_a(el):
    href = el.get('href')
    href = extract_archive_url(href)
    title = el.get('title')
    if el.contents:
        text = el.contents[0] or ''
    else:
        text = ''
    title_part = ' "%s"' % title.replace('"', r'\"') if title else ''
    return '[%s](%s%s)' % (text, href, title_part) if href else text


def convert_img(img):
    src = img.get('src')
    newname = src.split('/')[-1]
    # os.system('wget web.archive.org{src} -O {newname}'.format(
    #     src=src,
    #     newname=newname,
    # ))
    
    # src = extract_archive_url(src)
    
    src = '/images/' + newname
    
    alt = img.get('alt')
    return '![{alt}]({src})'.format(
        alt=alt, src=src
    )


@functioncache.filecache()
def get_html(url):
    return requests.get(url).text


for url in URLS:
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    for block in soup.find_all(class_='block'):
        if block.attrs['class'] != ['block']:
            continue
        
        block = copy.copy(block)
        block_original = copy.copy(block)
        
        title_a = block.find('a')
        if not title_a:
            continue

        title = title_a.contents[0]

        if title == 'Home':
            continue

        tags = set([
            a.contents[0]
            for a in block.find_all('a', attrs={'rel': 'category tag'})
        ])

        title_a.extract()

        for caption in block.find_all(class_='wp-caption'):
            caption.extract()

        for img in block.find_all('img'):
            img.replace_with(convert_img(img))

        # replace all links with markdown
        for a in block.find_all('a'):
            a.replace_with(convert_a(a))

        for p in block.find_all('p'):
            #p.replace_with(p.contents[0] + '\n\n')
            p.insert_after('\n\n')
            p.unwrap()

        for h1 in block.find_all('h1'):
            string = ''.join(unicode(h1sub) for h1sub in h1.children).strip()
            if len(string) > 0:
                h1.insert_before('# ')
            h1.unwrap()

        for h1 in block.find_all('h2'):
            h1.insert_before('## ')
            h1.unwrap()

        for pre in block.find_all('pre'):
            pre.insert_before('```\n')
            pre.insert_after('```')
            for li in pre.find_all('li'):
                li.insert_after('\n')
                li.unwrap()
            pre.unwrap()

        for strong in block.find_all('strong'):
            strong.insert_before('*')
            strong.insert_after('*')
            strong.unwrap()

        for li in block.find_all('li'):
            li.insert_before('- ')
            li.unwrap()

        opts = block.find(class_='opts')
        if opts:
            opts.extract()

        for clear in block.find_all(class_='clear'):
            clear.extract()

        for info in block.find_all(class_='info'):
            info.extract()

        for br in block.find_all('br'):
            br.extract()

        for iframe in block.find_all('iframe'):
            iframe.attrs['src'] = extract_archive_url(iframe.attrs['src'])

        for embed in block.find_all('embed'):
            embed.attrs['src'] = extract_archive_url(iframe.attrs['src'])

        for name in ('span', 'center', 'ul', 'ol', 'div', 'code'):
            for el in block.find_all(name):
                el.unwrap()

        string = re.sub('\n\n+', '\n\n', innerHTML(block))
        string = re.sub('&nbsp;', ' ', string)
        string = re.sub('# \n', '# ', string)
        string = re.sub('&gt;', '>', string)
        string = re.sub('&lt;', '<', string)
        
        # if '>' in string:
        #     print string

        filename = re.sub('[^\w\s-]', '', title.replace(' ', '-').lower())

        f = open('../source/_posts/'+filename+'.md', 'w')
        title = title.replace(u'’', "'")
        title = title.replace(u'–', '--')

        print >>f, 'title: "', title, '"'
        print >>f, 'tags:'
        for tag in tags:
            print >>f, '-', tag
        print >>f, '---'
        print >>f, string.encode('utf8')

        if title == 'python random timezone':
            print '#'*120
            print string
            print '-'*120
            print block_original
