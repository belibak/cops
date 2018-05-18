import asyncio
import aiohttp
import requests
from xml.etree import ElementTree

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
    points = []
    longs = []
    for string in strings:
        root = ElementTree.fromstring(string)
        for id,i in enumerate(root.findall('wpt')):
            name = i.find('name').text
            if '\n' in name:
                name = name.replace('\n', ' ')
            comment = i.find('comment').text
            if '\n' in comment:
                comment = comment.replace('\n', '')
            time = i.find('time').text
            att = i.attrib
            long = att['lon']
            lat = att['lat']
            idcat = att['catidx']
            if "Камера контроля скорости" in name:
                is_camera = True
            else:
                is_camera = False
            point = {"id" : id + 10000, 'name' : name, 'comment' : comment, 'long' : long, 'lat' : lat, 'time' : time, 'idcat' : idcat, 'is_camera' : is_camera}
            #print(point) #{'id': 10179, 'name': '27/Апр 11:39 Камера контроля скорости', 'comment': 'Камера контроля скорости', 'long': '27.7496447', 'lat': '53.9689718', 'time': 'больше дня назад', 'idcat': '2', 'is_camera': True}
            if point['long'] not in longs:
                if "Перекрытие" in point['name'] and '/' in point['name']:
                    pass
                else:
                    points.append(point)
            longs.append(long)
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
    print(get_dct())