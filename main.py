import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
#the web that your want to get
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r.url)
print(r.status_code)
soup=BeautifulSoup(r.content,'html.parser')
#get link

#finding a P in the web 
#type any tag tha you want to get in the ""content = s.find_all('p')""

#get title
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

#find the "P"
s=soup.find('div',class_='entry-content')
lines=s.find_all('p')
#remove the tag. with the ".text"
#type any tag tha you want to get in the ""content = s.find_all('p')""
for line in lines:
    print(line.text)

#links
for link in soup.find_all('a'):
    print(link.get('href'))
    if link<10:
        print(link.get('href'))


#get image
images_list=[]
images = soup.select('img')
for image in images:
    src=image.get('src')
    alt=image.get('alt')
    images_list.append({"src":src,"alt":alt})

for images in images_list:
    print(images)