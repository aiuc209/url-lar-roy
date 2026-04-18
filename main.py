from urllib.parse import urlparse, urlunparse

def remove_query_params(urls):
    result = []
    for url in urls:
        parsed_url = urlparse(url)
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, '', parsed_url.fragment))
        result.append(new_url)
    return result

urls = ["https://example.com/path?a=1&b=2", "https://example.com/path2?c=3&d=4"]
print(remove_query_params(urls))
