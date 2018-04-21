import requests
import lxml.html
import re


def append_prefix(prefix, link):
    if ('http' in link):
        return link
    else:
        return prefix + link


def extract_ss_info(url, previous):
    ss = requests.get(url)
    ss.encoding = 'utf-8'
    doc = lxml.html.fromstring(ss.text)
    titles = doc.xpath('//h3/span/text()')

    if titles:
        title = titles[0]
    else:
        title = doc.xpath('//h3/text()')[0]

    expected = "S{}.".format(previous + 1)

    if expected not in title:
        return

    titles = doc.xpath("//em[contains(text(),'Organizador')]")
    assert (len(titles) == 1)
    elem = titles[0].getparent()

    while elem.tag != 'p':
        elem = elem.getparent()

    ul = elem.getnext()
    authors = [author.text_content() for author in ul.xpath('li')]
    info = [title]

    for author in authors:
        m = re.search('(.*)\s*\(\s*(.*)\s*\)', author)

        if not m:
            m = re.search('(.*)\s*E-mail:\s*(.*)\s*', author)

        name = m.group(1).strip()
        link = m.group(2)
        info = info + [name, link]

    print("\t".join(info))


def main(url):
    m = re.search('(.*\.es)/(.*)', url)
    prefix = m.group(1)
    html = requests.get(url)
    doc = lxml.html.fromstring(html.text)
    links = doc.xpath("//a/@href")
    ss_links = [link for link in links if "Sesiones_Especiales___S" in link]

    for pos, ss_link in enumerate(ss_links):
        extract_ss_info(append_prefix(prefix, ss_link), pos)


if __name__ == '__main__':
    urls = [
        'http://www.eweb.unex.es/eweb/maeb2015/?Conferencia___Sesiones_Especiales'
    ]
    for url in urls:
        main(url)
