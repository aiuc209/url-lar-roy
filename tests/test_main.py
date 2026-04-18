import pytest
from urllib.parse import urlparse, urlunparse

def remove_query_params(url):
    parsed_url = urlparse(url)
    return urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, '', parsed_url.fragment))

def test_remove_query_params():
    urls = [
        'https://example.com/path?a=1&b=2',
        'http://example.com/path?a=1&b=2#fragment',
        'https://example.com/path',
        'http://example.com',
    ]
    expected_results = [
        'https://example.com/path',
        'http://example.com/path#fragment',
        'https://example.com/path',
        'http://example.com',
    ]
    for url, expected_result in zip(urls, expected_results):
        assert remove_query_params(url) == expected_result

def test_remove_query_params_empty_url():
    assert remove_query_params('') == ''

def test_remove_query_params_invalid_url():
    with pytest.raises(ValueError):
        remove_query_params('invalid_url')
