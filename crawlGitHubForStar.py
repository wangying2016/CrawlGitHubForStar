from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


print('Please input github user name:')
userName = input()
url = userName + '?tab=repositories'
openFailed = False
count = 0

while True:
    # 1. Open repositories page.
    try:
        html = urlopen('https://github.com/' + url)
        bsObj = BeautifulSoup(html, 'html.parser')
    except HTTPError as e:
        print('open ' + 'https://github.com/' + url + ' failed.')
        openFailed = True
        break

    # 2. Count stars at one page.
    for star in bsObj.findAll('svg', {'aria-label': 'star'}):
        count += int(star.parent.get_text().replace(',', ''))

    # 3. Find next page.
    nextPage = bsObj.find('a', {'class': 'next_page'})
    if nextPage is None:
        break
    else:
        url = nextPage.attrs['href']

if openFailed is False:
    print(userName + ' has ' + str(count) + ' stars.')