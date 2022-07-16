import datetime
def reload():
    with open('daniil_85_ver.txt', "r") as file:
        txt = "daniil_85 v" + file.readlines(100)
        file.close()
    with open('time.txt', 'w') as f:
        now = datetime.datetime.now()
        # d = now.day + "." + now.month + "." + now.year
        d = now.strftime("%d.%m.%Y")
        f.write(d)
        f.close()