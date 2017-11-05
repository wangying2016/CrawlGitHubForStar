# This version just crawl stars.
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup
#
#
# print('Please input github user name:')
# userName = input()
# url = userName + '?tab=repositories'
# openFailed = False
# count = 0
#
# while True:
#     # 1. Open repositories page.
#     try:
#         html = urlopen('https://github.com/' + url)
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except HTTPError as e:
#         print('open ' + 'https://github.com/' + url + ' failed.')
#         openFailed = True
#         break
#
#     # 2. Count stars at one page.
#     for star in bsObj.findAll('svg', {'aria-label': 'star'}):
#         count += int(star.parent.get_text().replace(',', ''))
#
#     # 3. Find next page.
#     nextPage = bsObj.find('a', {'class': 'next_page'})
#     if nextPage is None:
#         break
#     else:
#         url = nextPage.attrs['href']
#
# if openFailed is False:
#     print(userName + ' has ' + str(count) + ' stars.')


# This version crawl stars and forks, in addition output repository name.
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


print('Please input github user name:')
userName = input()
url = userName + '?tab=repositories'
openFailed = False
countStars = 0
countForks = 0

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
        # i. Count star numbers.
        starNumber = int(star.parent.get_text().replace(',', ''))
        countStars += starNumber

        # ii. Input repository name.
        print(star.parent.parent.parent.h3.a['href'] + ' has ' + str(starNumber)
              + ' stars.')

    # 3. Count forks at one page.
    for fork in bsObj.findAll('svg', {'aria-label': 'fork'}):
        # i. Count fork numbers.
        forkNumber = int(fork.parent.get_text().replace(',', ''))
        countForks += forkNumber

        # ii. Input repository name.
        print(fork.parent.parent.parent.h3.a['href'] + ' has ' + str(forkNumber)
              + 'forks.')

    # 3. Find next page.
    nextPage = bsObj.find('a', {'class': 'next_page'})
    if nextPage is None:
        break
    else:
        url = nextPage.attrs['href']

if openFailed is False:
    print()
    print('In totally:')
    print(userName + ' has ' + str(countStars) + ' stars.')
    print(userName + ' has ' + str(countForks) + ' forks.')
