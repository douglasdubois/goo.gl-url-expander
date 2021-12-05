import re
import requests

filename = ''

def unshorten_url(url):
        response = requests.head(url, allow_redirects=True)
        return response.url

with open(filename, 'r+') as f:
        content = f.read()
        content = re.sub("https://photos.app.goo.gl/\w*", lambda x: unshorten_url(x.group()), content)
        f.seek(0)
        f.write(content)
        f.close()