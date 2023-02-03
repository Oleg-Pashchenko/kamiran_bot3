import requests

from request_misc import convert_headers, data


def scrape_item(url):
    session = requests.session()
    r = session.get(url)
    headers = convert_headers(r.headers)
    r = session.post('https://unas.ru/auth/?login=yes', headers=headers, data=data)
    resp = session.get(url)
    try:
        return int(resp.text.split("data-max='")[1].split("'")[0])
    except Exception as e:
        print(e)
        return -1


print(scrape_item("https://unas.ru/catalog/tovary-dlya-sada/poliv/shlangi-i-sistemy-poliva/00224843/"))
print(scrape_item("https://unas.ru/catalog/tovary-dlya-doma/vannaya-komnata/aksessuary-dlya-vannoy-komnaty/00220137/"))