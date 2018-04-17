import datetime

def current_time():
    now = datetime.datetime.now()
    ct = "%04d-%02d-%02d %02d:%02d:%02d" %(now.year, now.month, now.day,
                                          now.hour, now.minute, now.second)
    return ct

def set_title():
    dt = datetime.datetime.now()
    title = "Updated %02d:%02d" %(dt.hour, dt.minute)
    return title