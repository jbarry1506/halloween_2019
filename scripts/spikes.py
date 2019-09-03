import datetime

# file structure
    # https://realpython.com/python-application-layouts/

dt = datetime.datetime.now()
# https://tecadmin.net/get-current-date-time-python/
# https://docs.python.org/3/library/datetime.html
# print(dt)
# print ("Current Year is: %d" % dt.year)
# print ("Current Month is: %d" % dt.month)
# print ("Current Day is: %d" % dt.day)
# print ("Current Hour is: %d" % dt.hour)
# print ("Current Minute is: %d" % dt.minute)
# print ("Current Second is: %d" % dt.second)

camtime = str(dt.year) + "_"\
    +str(dt.month) + "_"\
    +str(dt.day) + "_"\
    +str(dt.hour) + "_"\
    +str(dt.minute) + "_"\
    +str(dt.second)

fileloc = "~/Pictures/Halloween_2019/"
camfile = fileloc+'_'+camtime
print(camfile)