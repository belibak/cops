import asyncio
import aiohttp
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
    strings = run()
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
            if "Камера контроля скорости" in name:
                is_camera = True
            else:
                is_camera = False
            points['%04d'%id] = {'name' : name, 'comment' : comment, 'long' : long, 'lat' : lat, 'time' : time, 'idcat' : idcat, 'is_camera' : is_camera}
            ddb = Points(lat, long, name, comment, idcat, time, is_camera)
            db.session.add(ddb)
            db.session.commit()
    return points

async def gettext(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			return await resp.text()


async def getsources(lst = set_url_list()):
	res = []
	urls = [gettext(i) for i in lst]
	completed, pending = await asyncio.wait(urls)
	for comp in completed:
		res.append(comp.result())
	return res

def run():
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	cars_src = loop.run_until_complete(getsources())
	loop.close()
	return cars_src


if __name__ == "__main__":
	dct = get_dct()
	for i, v in dct.items():
		print(i, v)
