



import requests
import random



# Img loop

baby = requests.get('https://static.highsnobiety.com/thumbor/4ZRx65cmjtH5ikiVH7HwsuTzwYE=/1600x1067/static.highsnobiety.com/wp-content/uploads/2020/03/05104438/lil-baby-highschool-scholarship-fund-01.jpg')
baby1_img = baby.content

create_img = open('/home/practice/Documents/GitHub/python-all-projects-easy/baby.jpg', 'wb')
create_img.write(baby1_img)

baby.status_code
baby.ok
baby.headers
print(baby.headers['Cache-Control'], end='\n\n')



payload = {
    'username': 'Alec',
    'password': 'testing',
}

basic = requests.post('https://httpbin.org/post', data=payload)
basic_json = basic.json()

print(basic_json['form'])




auth = requests.get('https://httpbin.org/basic-auth/alecxavier/bigdata', auth=('alecxavier', 'bigdata'))
print(auth.text)


# get = requests.get('https://www.thejackforge.com/')
# get_text = get.text

# convert_html = open('/home/practice/Documents/GitHub/python-all-projects-easy/get_text.html', 'w')
# convert_html.write(get_text)
# print(convert_html)



# Get img, 

# ghostemane = requests.get('https://64.media.tumblr.com/99b8d24a85ba198d017ec1954939c21d/c102aff32e3e9c11-8c/s1280x1920/a63981ff6aa751a53eaf4063207af45da5c9e1a3.jpg')
# ghosteimg = ghostemane.content()

# img = open('/home/practice/Documents/GitHub/python-all-projects-easy/ghoste.png', 'wb')
# img.write(ghosteimg)
