import requests
from xml.etree import ElementTree

from app import Points
from app import db

db.create_all()

dct_try = {'0034': {'time': '50 мин назад', 'long': '27.4745059', 'name': '11:48 Ловят на пешахидов', 'idcat': '2', 'lat': '53.8583409', 'comment': 'Ловят на пешахидов'}, '0015': {'time': '30 мин назад', 'long': '27.5638260', 'name': '12:02 Регулировщик', 'idcat': '2', 'lat': '53.9166670', 'comment': 'Регулировщик'}, '0005': {'time': '30 мин назад', 'long': '27.6920160', 'name': '12:04 просто стоят гаи', 'idcat': '2', 'lat': '54.0549910', 'comment': 'просто стоят гаи'}, '0024': {'time': 'больше дня назад', 'long': '27.5637677', 'name': '22/Ноя 08:12 Левый ряд', 'idcat': '1', 'lat': '53.8722189', 'comment': 'Левый ряд'}, '0016': {'time': 'больше дня назад', 'long': '27.6806074', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9223955', 'comment': 'Камера контроля скорости'}, '0041': {'time': '40 мин назад', 'long': '27.5970610', 'name': '11:50 ГАИ на автомойке)', 'idcat': '2', 'lat': '53.8808570', 'comment': 'ГАИ на автомойке)'}, '0035': {'time': 'час назад', 'long': '27.4900380', 'name': '10:40 ГАИ', 'idcat': '2', 'lat': '53.9277470', 'comment': 'ГАИ'}, '0014': {'time': 'больше дня назад', 'long': '27.5364986', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9736278', 'comment': 'Камера контроля скорости'}, '0003': {'time': 'больше дня назад', 'long': '27.7493334', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9690783', 'comment': 'Камера контроля скорости'}, '0007': {'time': 'больше дня назад', 'long': '27.4449367', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9502023', 'comment': 'Камера контроля скорости'}, '0010': {'time': '30 мин назад', 'long': '27.7089230', 'name': '12:03 ГАИ', 'idcat': '2', 'lat': '54.0545450', 'comment': 'ГАИ'}, '0000': {'time': '20 мин назад', 'long': '27.5456990', 'name': '12:18 Камера', 'idcat': '2', 'lat': '53.9120570', 'comment': 'Камера'}, '0013': {'time': 'час назад', 'long': '27.6495730', 'name': '10:42 доки', 'idcat': '2', 'lat': '53.9758610', 'comment': 'доки'}, '0030': {'time': '2 часа назад', 'long': '27.5251440', 'name': '10:36 доки', 'idcat': '2', 'lat': '53.8713530', 'comment': 'доки'}, '0008': {'time': '30 мин назад', 'long': '27.5441560', 'name': '12:03 гаи доки', 'idcat': '2', 'lat': '53.8930100', 'comment': 'гаи доки'}, '0004': {'time': '40 мин назад', 'long': '27.6552640', 'name': '11:57 ГАИ', 'idcat': '2', 'lat': '54.0041360', 'comment': 'ГАИ'}, '0036': {'time': 'день назад', 'long': '27.5428380', 'name': '22/Ноя 17:48 Левый ряд, средний ряд, правый ряд', 'idcat': '1', 'lat': '53.9066840', 'comment': 'Левый ряд, средний ряд, правый ряд'}, '0001': {'time': 'час назад', 'long': '27.5801260', 'name': '11:33 Камера', 'idcat': '2', 'lat': '53.9304100', 'comment': 'Камера'}, '0021': {'time': '2 часа назад', 'long': '27.6119650', 'name': '10:38 стоит с палкой', 'idcat': '2', 'lat': '53.8892150', 'comment': 'стоит с палкой'}, '0028': {'time': '3 часа назад', 'long': '27.4158157', 'name': '09:33 Right lane', 'idcat': '1', 'lat': '53.9230720', 'comment': 'Right lane'}, '0032': {'time': '10 мин назад', 'long': '27.4576760', 'name': '12:28 Стоят и улыбаются', 'idcat': '2', 'lat': '53.9170430', 'comment': 'Стоят и улыбаются'}, '0018': {'time': '50 мин назад', 'long': '27.5479520', 'name': '11:44 На скорость', 'idcat': '2', 'lat': '53.8857530', 'comment': 'На скорость'}, '0006': {'time': 'больше дня назад', 'long': '27.7007338', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8503677', 'comment': 'Камера контроля скорости'}, '0011': {'time': 'больше дня назад', 'long': '27.7230846', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9569019', 'comment': 'Камера контроля скорости'}, '0037': {'time': 'час назад', 'long': '27.5953280', 'name': '10:55 Правый ряд', 'idcat': '1', 'lat': '53.9105910', 'comment': 'Правый ряд'}, '0020': {'time': '3 часа назад', 'long': '27.6029820', 'name': '09:00 парковка', 'idcat': '2', 'lat': '53.8600120', 'comment': 'парковка'}, '0043': {'time': 'больше дня назад', 'long': '27.5334916', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8324107', 'comment': 'Камера контроля скорости'}, '0009': {'time': 'час назад', 'long': '27.6677130', 'name': '11:01 Стоят', 'idcat': '2', 'lat': '54.0363850', 'comment': 'Стоят'}, '0042': {'time': 'больше дня назад', 'long': '27.6732509', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9406342', 'comment': 'Камера контроля скорости'}, '0017': {'time': 'час назад', 'long': '27.4842850', 'name': '11:01 стоит палит', 'idcat': '2', 'lat': '53.8499900', 'comment': 'стоит палит'}, '0002': {'time': 'больше дня назад', 'long': '27.6356334', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9618884', 'comment': 'Камера контроля скорости'}, '0022': {'time': '2 часа назад', 'long': '27.6244410', 'name': '10:00 с палкой', 'idcat': '2', 'lat': '53.9594015', 'comment': 'с палкой'}, '0026': {'time': 'больше дня назад', 'long': '27.5429700', 'name': '14/Окт 20:00 Перекрытие', 'idcat': '4', 'lat': '53.9012320', 'comment': 'Перекрытие'}, '0027': {'time': '9 мин назад', 'long': '27.4350150', 'name': '12:30 Стоят', 'idcat': '2', 'lat': '53.8993000', 'comment': 'Стоят'}, '0029': {'time': 'больше дня назад', 'long': '27.7343899', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8342025', 'comment': 'Камера контроля скорости'}, '0012': {'time': 'час назад', 'long': '27.5757560', 'name': '11:32 Спрятались', 'idcat': '2', 'lat': '53.9008800', 'comment': 'Спрятались'}, '0044': {'time': 'час назад', 'long': '27.6961730', 'name': '11:09 Средний ряд', 'idcat': '1', 'lat': '53.8778150', 'comment': 'Средний ряд'}, '0033': {'time': 'больше дня назад', 'long': '27.8232735', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9974721', 'comment': 'Камера контроля скорости'}, '0019': {'time': 'больше дня назад', 'long': '27.6709190', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8487657', 'comment': 'Камера контроля скорости'}, '0045': {'time': 'больше дня назад', 'long': '27.4652307', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8387802', 'comment': 'Камера контроля скорости'}, '0023': {'time': '3 часа назад', 'long': '27.6233220', 'name': '09:34 Волки', 'idcat': '2', 'lat': '53.8815080', 'comment': 'Волки'}, '0025': {'time': 'больше дня назад', 'long': '27.4279828', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.9473018', 'comment': 'Камера контроля скорости'}, '0039': {'time': 'больше дня назад', 'long': '27.8132734', 'name': '21/Ноя 13:41 Камера контроля скорости', 'idcat': '2', 'lat': '53.8134305', 'comment': 'Камера контроля скорости'}, '0038': {'time': 'час назад', 'long': '27.5602760', 'name': '11:26 Стоят доки', 'idcat': '2', 'lat': '53.9235480', 'comment': 'Стоят доки'}, '0040': {'time': '40 мин назад', 'long': '27.5995120', 'name': '11:56 ГАИ', 'idcat': '2', 'lat': '53.9693120', 'comment': 'ГАИ'}, '0031': {'time': 'час назад', 'long': '27.4720060', 'name': '11:15 Стоит', 'idcat': '2', 'lat': '53.8679580', 'comment': 'Стоит'}}

def set_url():
    tl_lat, br_lat = 54.0, 53.7
    tl_lon, br_lon = 27.2, 27.8 
    zoom = 12
    url = "http://mobile.navi.yandex.net/userpoi/getpoints?uuid=&scalefactor=1.50&zoom=%s&tl_lat=%s&tl_lon=%s&br_lat=%s&br_lon=%s&catlist=1,2,3,4,5,6&ver=2&utf&lang=ru-RU" %(zoom, tl_lat, tl_lon, br_lat, br_lon)
    return url

def get_xml_string(url = set_url()):
    headers = {"User-Agent": "ApacheHttpClient/UNAVAILABLE (java 1.4)"}
    r = requests.get(url, headers=headers)
    string = r.content
    return r.content

def get_dct(string = get_xml_string()):
    points = {}
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
    print(len(dct), len(dct_try))
