from fake_useragent import UserAgent


def create_headers() -> dict:
    headers = {
        'User-Agent': UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml,*/*',
        'Accept-Language': 'pl,en-US,en',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    return headers
