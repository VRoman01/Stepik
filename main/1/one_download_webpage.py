from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html/").read()
print(html)