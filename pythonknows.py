from requests_html import HTMLSession



url = 'https://pythoncaff.com/docs/pymotw'
session = HTMLSession()
r = session.get(url)
text = r.html.find('ol.sorted_table')
sets = text[0].links
lists =[]
for i in sets:
	lists.append(i)


def numb(url):
	pp = url[-6:][url[-6:].index('/')+1:]
	return int(pp)
ssss = lists.sort(key=numb)
print(type(lists))
print(lists)
for i in lists:
	print(i)