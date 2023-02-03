def convert_headers(first_headers):
    second_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": '202',
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "",  # You need to fill this value
        "origin": "https://unas.ru",
        "referer": "https://unas.ru/catalog/tovary-dlya-sada/poliv/shlangi-i-sistemy-poliva/00224843/",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    # Fill the "cookie" value
    cookie = first_headers.get("Set-Cookie")
    if cookie:
        second_headers["cookie"] = cookie

    return second_headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-CH-UA": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "Linux",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
LOGIN = "anastasia.yakova@gmail.com"
PASSWORD = "Moloko12."
data = {
    "backurl": "/catalog/tovary-dlya-sada/poliv/shlangi-i-sistemy-poliva/00224843/",
    "AUTH_FORM": "Y",
    "TYPE": "AUTH",
    "POPUP_AUTH": "Y",
    "USER_LOGIN": LOGIN,
    "USER_PASSWORD": PASSWORD,
    "Login": "Y",
    "Login1": "Y"
}