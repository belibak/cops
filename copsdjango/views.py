import os

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect

from copsdjango.tools import current_time
from copsdjango.tools import set_title

import copsdjango.getpoints as getpoints

#points = [{'id': 10000, 'name': '11/Апр 00:13 Камера контроля скорости', 'comment': 'Камера контроля скорости', 'long': '27.4199519', 'lat': '53.9286960', 'time': 'больше дня назад', 'idcat': '2', 'is_camera': True}, {'id': 10001, 'name': '11:34 Левый ряд, средний ряд, правый ряд', 'comment': 'Левый ряд, средний ряд, правый ряд', 'long': '27.5560220', 'lat': '53.8921290', 'time': '2 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10002, 'name': '10:46 ДПС', 'comment': 'ДПС', 'long': '27.4826650', 'lat': '53.8615980', 'time': '50 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10006, 'name': '10:59 ДПС', 'comment': 'ДПС', 'long': '27.4627540', 'lat': '53.9950960', 'time': '30 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10010, 'name': '10:04 Контроль скорости', 'comment': 'Контроль скорости', 'long': '27.5085270', 'lat': '53.8811580', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10013, 'name': '11:27 Камера', 'comment': 'Камера', 'long': '27.5832310', 'lat': '53.9082510', 'time': '9 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10014, 'name': '10:11 Стоят', 'comment': 'Стоят', 'long': '27.5052880', 'lat': '53.9692320', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10019, 'name': '28/Март 13:13 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5489120', 'lat': '53.9034030', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}, {'id': 10020, 'name': '19/Фев 20:44 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5548000', 'lat': '53.8719150', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}, {'id': 10021, 'name': '08:57 Средний ряд', 'comment': 'Средний ряд', 'long': '27.5461100', 'lat': '53.9120880', 'time': '2 часа назад', 'idcat': '1', 'is_camera': False}, {'id': 10022, 'name': '10:28 ГАИ', 'comment': 'ГАИ', 'long': '27.4708690', 'lat': '53.8445110', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10024, 'name': '11:17 Копы', 'comment': 'Копы', 'long': '27.6917300', 'lat': '53.8939430', 'time': '15 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10025, 'name': '11:17 Камера', 'comment': 'Камера', 'long': '27.7223340', 'lat': '53.8399100', 'time': '15 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10026, 'name': '16/Апр 19:01 Перекрытие', 'comment': 'Перекрытие', 'long': '27.6100570', 'lat': '53.8393070', 'time': 'день назад', 'idcat': '4', 'is_camera': False}, {'id': 10029, 'name': '11:29 Доки', 'comment': 'Доки', 'long': '27.5000870', 'lat': '53.9090640', 'time': '7 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10030, 'name': '07:20 Гайцы', 'comment': 'Гайцы', 'long': '27.6435170', 'lat': '53.7766760', 'time': '4 часа назад', 'idcat': '2', 'is_camera': False}, {'id': 10031, 'name': '09/Апр 18:20 Перекрытие', 'comment': 'Перекрытие', 'long': '27.6503680', 'lat': '53.9279130', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}, {'id': 10032, 'name': '16/Апр 20:30 Средний ряд', 'comment': 'Средний ряд', 'long': '27.6667510', 'lat': '53.8440980', 'time': 'полдня назад', 'idcat': '1', 'is_camera': False}, {'id': 10035, 'name': '10:44 Камера', 'comment': 'Камера', 'long': '27.6036630', 'lat': '53.9175430', 'time': '50 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10039, 'name': '11:34 Левый ряд', 'comment': 'Левый ряд', 'long': '27.6482902', 'lat': '53.8346421', 'time': '2 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10040, 'name': '08:37 стоит на скорость с радаром.', 'comment': 'стоит на скорость с радаром.', 'long': '27.7376810', 'lat': '53.8327570', 'time': '2 часа назад', 'idcat': '2', 'is_camera': False}, {'id': 10044, 'name': '22/Янв 17:00 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5385150', 'lat': '53.8527290', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}, {'id': 10046, 'name': '05:00 Перекрытие', 'comment': 'Перекрытие', 'long': '27.6626320', 'lat': '53.7679740', 'time': 'полдня назад', 'idcat': '4', 'is_camera': False}, {'id': 10047, 'name': '08:34 Стоят', 'comment': 'Стоят', 'long': '27.6511840', 'lat': '53.9761870', 'time': '3 часа назад', 'idcat': '2', 'is_camera': False}, {'id': 10050, 'name': '11:15 Перекрыто', 'comment': 'Перекрыто', 'long': '27.6304060', 'lat': '53.8344420', 'time': '20 мин назад', 'idcat': '3', 'is_camera': False}, {'id': 10052, 'name': '08:32 доки', 'comment': 'доки', 'long': '27.4904465', 'lat': '53.8677920', 'time': '3 часа назад', 'idcat': '2', 'is_camera': False}, {'id': 10054, 'name': '09:45 Левый ряд, средний ряд', 'comment': 'Левый ряд, средний ряд', 'long': '27.5327610', 'lat': '53.9183190', 'time': 'час назад', 'idcat': '1', 'is_camera': False}, {'id': 10055, 'name': '00:00 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5566620', 'lat': '53.9832880', 'time': 'полдня назад', 'idcat': '4', 'is_camera': False}, {'id': 10057, 'name': '10:47 Правый ряд', 'comment': 'Правый ряд', 'long': '27.5944810', 'lat': '53.9263850', 'time': '40 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10058, 'name': '11/Апр 00:13 Камера контроля полосы', 'comment': 'Камера контроля полосы', 'long': '27.5622014', 'lat': '53.9020729', 'time': 'больше дня назад', 'idcat': '2', 'is_camera': False}, {'id': 10065, 'name': '10:54 ГАИ', 'comment': 'ГАИ', 'long': '27.6859450', 'lat': '53.9464500', 'time': '40 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10003, 'name': '10:57 Камера', 'comment': 'Камера', 'long': '27.6377980', 'lat': '53.8564070', 'time': '30 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10004, 'name': '11:12 Левый ряд', 'comment': 'Левый ряд', 'long': '27.6451230', 'lat': '53.8341470', 'time': '20 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10020, 'name': '08:46 Левый ряд, средний ряд, правый ряд. все перекопано.', 'comment': 'Левый ряд, средний ряд, правый ряд. все перекопано.', 'long': '27.5537042', 'lat': '53.8910591', 'time': '2 часа назад', 'idcat': '1', 'is_camera': False}, {'id': 10022, 'name': '08:41 Камера', 'comment': 'Камера', 'long': '27.5756650', 'lat': '53.9085190', 'time': '2 часа назад', 'idcat': '2', 'is_camera': False}, {'id': 10030, 'name': '10:07 ГАИ', 'comment': 'ГАИ', 'long': '27.5954820', 'lat': '53.9309910', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10045, 'name': '09:44 камера за отбойником справа на 70!!!', 'comment': 'камера за отбойником справа на 70!!!', 'long': '27.6651180', 'lat': '53.8423610', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10046, 'name': '10:23 На скорость', 'comment': 'На скорость', 'long': '27.4403720', 'lat': '53.9506640', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10058, 'name': '10:10 Гаи на документы', 'comment': 'Гаи на документы', 'long': '27.5336990', 'lat': '53.9695410', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10063, 'name': '26/Дек 08:56 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5487480', 'lat': '53.8728770', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}, {'id': 10064, 'name': '09:56 Гаер', 'comment': 'Гаер', 'long': '27.6869340', 'lat': '53.9450070', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10076, 'name': '17/Март 09:36 Ограничение скоростного режима 40 км/ч в связи с ремонтом!', 'comment': 'Ограничение скоростного режима 40 км/ч в связи с ремонтом!', 'long': '27.5630883', 'lat': '53.8985764', 'time': 'больше дня назад', 'idcat': '3', 'is_camera': False}, {'id': 10025, 'name': '09:49 дежурит гаи', 'comment': 'дежурит гаи', 'long': '27.6881200', 'lat': '53.9452960', 'time': 'час назад', 'idcat': '2', 'is_camera': False}, {'id': 10071, 'name': '10:38 Камера', 'comment': 'Камера', 'long': '27.4703230', 'lat': '53.8440019', 'time': '50 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10080, 'name': '10:44 Левый ряд', 'comment': 'Левый ряд', 'long': '27.5802470', 'lat': '53.9129010', 'time': '50 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10091, 'name': '11:23 Камера', 'comment': 'Камера', 'long': '27.4894140', 'lat': '53.8671650', 'time': '10 мин назад', 'idcat': '2', 'is_camera': False}, {'id': 10011, 'name': '11:09 Left lane', 'comment': 'Left lane', 'long': '27.6465370', 'lat': '53.8342000', 'time': '20 мин назад', 'idcat': '1', 'is_camera': False}, {'id': 10068, 'name': '28/Март 13:12 Перекрытие', 'comment': 'Перекрытие', 'long': '27.5489110', 'lat': '53.9034010', 'time': 'больше дня назад', 'idcat': '4', 'is_camera': False}]


def setpoints(request):
    t = get_template('map.html')
    '''title = set_title()
    lst = set_points()
    title = len(lst)
    lst2 = database_set_points(title)
    return render_template("map1.html",
                           lst = lst,
                           title=title,
                           lst2=lst2)'''
    points = getpoints.get_dct()
    dct = {"lst": points,
           "title" : "%d" %(len(points)),
           }
    html = t.render(dct)
    return HttpResponse(html)



def setpoints_blocks():
    print(current_time(), "Try to take dct")
    dct = getpoints.get_dct()
    #print(dct['0006']['lat'])
    lst = []
    for i in sorted(dct.keys()):
        d = dct[i]
        baloon = '%s %s' %(d['time'], d['name'])
        string = """pl%s = new ymaps.Placemark([%s, %s], {
                        balloonContent: '%s',
                        iconContent: "%s",
                    }, {
                        preset: 'islands#redStretchyIcon',
                        iconImageSize: [10, 30],
                    });
                    myMap.geoObjects.add(pl%s);""" %(i, d['lat'], d['long'], baloon, d['comment'], i)
        lst.append(string)
    print(current_time(), "Created points list")
    return lst
