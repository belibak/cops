from flask import render_template

import datetime

from app import app
from app import getpoints

def set_title():
    dt = datetime.datetime.now()
    title = "Updated %s:%s" %(dt.hour, dt.minute)
    return title

def set_points():
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
    return lst

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    if ('Cache-Control' not in response.headers):
        response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.route('/')
@app.route('/index')
def map():
    title = set_title()
    lst = set_points()
    title = len(lst)
    return render_template("map.html",
                           lst = lst,
                           title=title)

if __name__ == '__main__':
    app.run()