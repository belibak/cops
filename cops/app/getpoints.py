import requests
from xml.etree import ElementTree

from app import Points
from app import db

db.create_all()

def set_url_list():
    tl_lat, br_lat = 54.0, 53.7
    tl_lon, br_lon = 27.2, 27.8
    urls = []
    for i in range(6,13):
        zoom = i
        url = "http://mobile.navi.yandex.net/userpoi/getpoints?uuid=&scalefactor=1.50&zoom=%s&tl_lat=%s&tl_lon=%s&br_lat=%s&br_lon=%s&catlist=1,2,3,4,5,6&ver=2&utf&lang=ru-RU" %(zoom, tl_lat, tl_lon, br_lat, br_lon)
        urls.append(url)
    return urls

def get_xml_string():
    urls = set_url_list()
    headers = {"User-Agent": "ApacheHttpClient/UNAVAILABLE (java 1.4)"}
    strings = []
    for url in urls:
        r = requests.get(url, headers=headers)
        string = r.content
        strings.append(string)
    return strings

def get_dct():
    strings = get_xml_string()
    points = {}
    for string in strings:
        root = ElementTree.fromstring(string)
        for id,i in enumerate(root.findall('wpt')):
            name = i.find('name').text
            comment = i.find('comment').text
            time = i.find('time').text
            att = i.attrib
            long = att['lon']
            lat = att['lat']
            idcat = att['catidx']
            points['%04d'%id] = {'name' : name, 'comment' : comment, 'long' : long, 'lat' : lat, 'time' : time, 'idcat' : idcat}
            ddb = Points(lat, long, name, comment, idcat, time)
            db.session.add(ddb)
            db.session.commit()
    return points


if __name__ == "__main__":
    dct = get_dct()
    print(len(dct))
