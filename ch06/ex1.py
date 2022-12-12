
from bs4 import BeautifulSoup as bs


html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html"' \
        ' class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li>' \
        '<a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'

soup = bs(html, 'html.parser')

# h1 태그 값 가져오기
tag_h1 = soup.h1
print(tag_h1)

tag_div = soup.div
print(tag_div)

# ul, a 태그가 여러개 존재할 경우 첫 번째 태그만 가져옴
tag_ul = soup.ul
print(tag_ul)

tag_a = soup.a
print(tag_a)

# find_all : 해당하는 모든 태그 가져오기
tag_ul_all = soup.find_all('ul')
for tagul in tag_ul_all:
    print('## %s' % tagul)

tag_a_all = soup.find_all('a')
for a_tag in tag_a_all:
    print('## %s' % a_tag)

# 태그의 속성 가져오기
print(tag_a.attrs)
print(tag_a['href'])
print(tag_a['class'])

print()
print()

# 특정 속성을 가진 태그 가져오기
tag_ul2 = soup.find('ul', attrs={'class':'brand'})
print(tag_ul2)

title = soup.find(id='title')
print(title)
# html 태그의 텍스트 값 가져오기
print(title.string)

# 자식 태그 값 가져오기
li_list = soup.select('div>ul.brand>li')
for li in li_list:
    print(li)
