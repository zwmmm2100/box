url = 'http://ws3.sinaimg.cn/mw600/87dfc041ly1fxbgfc5t8dj20m80xcabi.jpg'
#查找开始于22之后的‘/’字符
sss = url.index('/',22)
#分割字符串
print(url[:22])
print(url[27:])
print(sss)