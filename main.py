import re
import requests

filename = 'input.txt'

def unshorten_url(url):
        response = requests.head(url, allow_redirects=True)
        return response.url

url_re = re.compile(r'(https?:\/{2})?.*goo.gl\/\w*')
key_re = re.compile(r'\?key=\w*')

with open(filename, 'r+') as f:
        content = f.read()
        content = url_re.sub(lambda x: unshorten_url(x.group()), content)
        content = key_re.sub('', content)
        f.seek(0)
        f.truncate(0)
        f.write(content)
