import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

js_aa='''
var Title="海贼王第1卷";var Clid="2";var mhurl="2/Vol_001/001aa.jpg";var Url="Vol_001";var nexturl="Vol_002";var CTitle="海贼王";var mhss=getCookie("picHost");if(mhss==""){mhss="p1.xiaoshidi.net"}if(mhurl.indexOf("2016")==-1&&mhurl.indexOf("2017")==-1&&mhurl.indexOf("2018")==-1&&mhurl.indexOf("2019")==-1){mhss="p0.xiaoshidi.net"}var mhpicurl=mhss+"/"+mhurl;if(mhurl.indexOf("http")!=-1){mhpicurl=mhurl}function nofind(){var i=event.srcElement?event.srcElement:event.target;i.src="http://p1.xiaoshidi.net/"+mhurl;var t=new Date;t.setTime(t.getTime()-1);document.cookie="picHost=0;path=/;domain=fzdm.com;expires="+t.toGMTString();i.onerror=null;toastr.success("已更换为最快服务器～",{timeOut:5e3})}  ;document.write('<img src="http://'+mhpicurl+'" width="0" height="0" />');
'''

url = 'https://www.fzdm.com/manhua/002/Vol_001/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
session = HTMLSession()
r = session.get(url)

print(r.html)