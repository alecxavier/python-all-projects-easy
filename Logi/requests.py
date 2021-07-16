

import random
import requests

# The following code below is where I experimented with the requests module

get = requests.get('https://64.media.tumblr.com/cdfba455fef9a49fd6e9876480a818d6/97d0eb8d0c272b31-14/s1280x1920/019cf47c5809f79230ca09d071a2e369ad853711.jpg')
get.headers

content_type = get.headers['Content-Type']
last_modified = get.headers['Last-Modified']
print(content_type, last_modified)

# Get Image from the links

get_img = get.content
image = open('/home/practice/Documents/GitHub/python-all-projects-easy/Logi/kendallasap.png', 'wb') 
image.write(get_img)





# New get

gets = requests.get('https://www.tumblr.com/search/asap+rocky')
json = gets.json()
print(json)

gets.encoding
gets.headers['Content-Type']



payload = {
    
    "v": "tb8gHvYlCFs",
    "ab_channel": "CoreySchafer"
    
}

headers = {
    "owner": "Alec Xavier Alba",
    "co-founder": "Travis", 
    "company": "Intel, AMD, GeForce"
}

youtube = requests.get('https://www.youtube.com/watch', params=payload)
youtube.url

add_headers = requests.get(youtube, headers=headers)
add_headers.status_code
add_headers.headers

