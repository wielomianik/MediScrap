import requests
from dotenv import load_dotenv
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random
load_dotenv()

base_url = 'https://mol.medicover.pl/Users/Account/LogOn?ReturnUrl=%2F'
headers = {
    'User-Agent': agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml,*/*',
    'Accept-Language': 'pl,en-US,en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
}

resp = requests.get(
    url=base_url,
    headers=headers,
    allow_redirects=False
)
resp_url = resp.headers["Location"]
print(resp_url)

resp = requests.get(
    url=resp_url,
    headers=headers,
    allow_redirects=False
)
resp_url = resp.headers["Location"]
print(resp_url)

resp = requests.get(
    url=resp_url,
    headers=headers.update({
        'Accept': 'text/html,application/xhtml+xml,application/xml,image/avif,image/webp,*/*',
        'TE': 'trailers',
        'Referer': 'https://mol.medicover.pl/',
    }),
    allow_redirects=False
)
resp_url = resp.headers
print(resp_url)


