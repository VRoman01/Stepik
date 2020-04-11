from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп

pattern = r'<td>(.*)</td>'
sum_td = 0
for td in soup.find_all('td'):
    b = re.search(pattern, str(td)).groups()
    sum_td += int(b[0])
print(sum_td)



