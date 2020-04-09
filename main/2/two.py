from urllib.request import urlopen
import re
import collections

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
pattern = r'<code>(.*?)</code>'
print(collections.Counter(sorted(re.findall(pattern, html))))


