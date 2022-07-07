import requests
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
PREFIX = "https://ru.wikipedia.org/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
BORDER1 = "Предыдущая страница"
BORDER2 = "Следующая страница"


def counter(url=URL):
    # the function finds animal names by url and
    # counts the number of animals for each letter of the alphabet
    res_counter = dict()
    url = URL
    finish = False
    while not finish:
        # page parsing
        req = requests.get(url, headers=HEADERS)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        tags = soup.find_all("a")
        flag = False
        border_cnt = 0
        for tag in tags:
            if flag:
                if tag.text == BORDER1:
                    border_cnt += 1
                    continue
                if tag.text.startswith(PREFIX):
                    # check whether the current page is final
                    if border_cnt == 1:
                        finish = True
                    break
                if tag.text == BORDER2:
                    border_cnt -= 1
                    # url of the next page
                    url = "https://ru.wikipedia.org/" + tag.get("href")
                else:
                    cur_animal = tag.text
                    letter = cur_animal[0]
                    # counter
                    if letter not in res_counter:
                        res_counter[letter] = 1
                    else:
                        res_counter[letter] += 1
            elif tag.text == BORDER1 or tag.text == BORDER2:
                flag = True
    return res_counter


print(counter())
