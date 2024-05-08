import requests
from medicover.headers import create_headers


BASE_URL = 'https://mol.medicover.pl/Users/Account/LogOn?ReturnUrl'
BASE_OAUTH_URL = 'https://oauth.medicover.pl'


def login():

    headers = create_headers()
    with requests.session() as session:

        # https://mol.medicover.pl/Users/Account/LogOn?ReturnUrl
        resp = session.get(
            url=BASE_URL,
            headers=headers,
            allow_redirects=False
        )
        print('GET: ', resp.request.url)
        resp_url = resp.headers['Location']
        print('RESPONSE: ', resp_url, '\n')

        # https://oauth.medicover.pl/connect/authorize?client_id=Mcov_Mol&response_type=code+id_token...
        resp = session.get(
            url=resp_url,
            headers=headers,
            allow_redirects=False
        )
        print('GET: ', resp.request.url)
        resp_url = resp.headers['Location']
        print('RESPONSE: ', resp_url, '\n')

        # https://oauth.medicover.pl/external?provider=IS3&signin=TOKEN&owner=Mcov_Mol&ui_locales=pl-PL
        resp = session.get(
            url=BASE_OAUTH_URL + '/external',
            headers=headers.update({'Referer': resp_url}),
            params={
                'provider': 'IS3',
                'signin': resp_url.split('=')[-1],
                'owner': 'Mcov_Mol',
                'ui_locales': 'pl-PL'
            },
            allow_redirects=False
        )
        print('GET: ', resp.request.url)
        resp_url = resp.headers['Location']
        print('RESPONSE: ', resp_url, '\n')

        # https://login.medicover.pl/connect/authorize?client_id=is3&redirect_uri=https%3A%2F%2Foauth.medicover.pl...
        resp = session.get(
            url=resp_url,
            headers=headers,
            allow_redirects=False
        )
        print('GET: ', resp.request.url)
        resp_url = resp.headers['Location']
        print('RESPONSE: ', resp_url, '\n')

        # https://login.medicover.pl/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dis3%26...
        resp = session.get(
            url=resp_url,
            headers=headers,
            allow_redirects=False
        )
        print('GET: ', resp.request.url)
        print('RESPONSE: ', resp_url, '\n')

        #print(resp.text)
        session.cookies.clear()
