# Goes to a img site (in this case a blog), searches for a category of photos (in this case the comics) and
# downloads all the resulting images

import requests, os, bs4

# Downloads the URL.
url = 'http://cersibonforever.blogspot.com/'
i = 1
res = requests.get(url)
res.raise_for_status()
# Create the folder in path.
os.makedirs('cersibon', exist_ok = True)
# Find the images.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
all_post = soup.select('img[src]')
for post in all_post:
    src = post.get('src')
    if not src:
        print('Could not find image.')
    # Download the images.
    else:
        res = requests.get(src)
        res.raise_for_status()
        # Saves the images to cersibon folder.
        print('Downloading %s to folder...' % (post))
        imageFile = open(os.path.join('cersibon', 'tirinha' + str(i) + '.jpg'), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        i += 1
        print(imageFile)
    print('Done.')