import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

url = 'http://data.10jqka.com.cn/rank/cxg/board/1/field/stockcode/ajax/1/free/1/'
r = requests.get(url)
r.encoding = 'gbk'
print(type(r.text))
print(r.text)


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)
#
#     def handle_endtag(self, tag):
#         print("End tag  :", tag)
#
#     def handle_data(self, data):
#         print("Data     :", data)
#
#     def handle_comment(self, data):
#         print("Comment  :", data)
#
#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)
#
#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)
#
#     def handle_decl(self, data):
#         print("Decl     :", data)
#
#
# parser = MyHTMLParser()
# parser.feed(r.text)
