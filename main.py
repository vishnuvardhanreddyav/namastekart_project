import datetime as dt
import os

today=dt.datetime.today().strftime('%Y%m%d')

files = os.listdir(f"data/incoming_files/{today}")
for file in files:
    f = open(f"data/incoming_files/{today}/{file}",'r')
    for a in f:
        print(a)
    f.close()


