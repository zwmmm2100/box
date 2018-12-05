from requests_html import HTMLSession



url = 'https://www.fzdm.com/manhua/002/Vol_001/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
session = HTMLSession()
r = session.get(url)
r.html.render()

print(r.html.html)