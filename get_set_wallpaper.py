import urllib, urllib2
import os
import datetime
import random
from bs4 import BeautifulSoup
from appscript import app, mactypes, its

#===============================================================================

Dir = "/Users/seriousbuns/Desktop/Wallpapers/" + str(datetime.date.today())
response = urllib2.urlopen("http://reddit.com/r/wallpapers/top/?sort=top&t=month")


def make_sure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def write_image(out, Image):
    output = open(out, "wb")
    output.write(Image.read())
    output.close()

def set_desktop_background(filename):
    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for d in desktops:
        desk = se.desktops[its.display_name == d]
        desk.picture.set(mactypes.File(out))

soup = BeautifulSoup(response.read())
link_list = soup.find_all('a', {'class':'title '})
link_len = len(link_list)
rand = random.randrange(1,link_len,1)
make_sure_path_exists(Dir)

for j, link in enumerate(link_list):
    imglink = link.get('href')
    if (imglink.endswith('.jpg') or imglink.endswith('.png')):
        #save to a folder on desktop
        Image = urllib.urlopen(imglink)
        out = Dir + imglink[imglink.rfind('/') :]
        write_image(out, Image)
        if rand == j:
            set_desktop_background(out)
