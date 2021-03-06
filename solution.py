import re
import urllib.request
import csv
import json
url='/listings?min_price=100000&max_price=200000&min_bed=2&max_bed=2&min_bath=2&max_bath=2'
m=re.search('min_price=(\d+)',url)
min=m.group(1)
m=re.search('max_price=(\d+)',url)
max=m.group(1)
m=re.search('min_bed=(\d+)',url)
min_bed=m.group(1)
m=re.search('max_bed=(\d+)',url)
max_bed=m.group(1)
m=re.search('min_bath=(\d+)',url)
min_bath=m.group(1)
m=re.search('max_bath=(\d+)',url)
max_bath=m.group(1)

url1='http://s3.amazonaws.com/opendoor-problems/listings.csv'
response=urllib.request.urlopen(url1)
csv = response.read()
csvstr = str(csv).strip("b'")
str='{"type": "FeatureCollection",\n"features": ['
lines = csvstr.split("\\n")
for line in lines:
    list=line.split(',')
    try:
        if list[3]>=min and list[3]<=max and list[4]>=min_bed and list[4]<=max_bed and list[5]>=min_bath and list[5]<=max_bath:
            str+='{\n"type": "feature",\n"geometry": {"type": "Point", "coordinates"},\n"properties": {\n"id":'+list[0]+'\n"price":'+list[3]+'\n"street":'+list[1]+',\n"bedrooms":'+list[4]+'\n"bathrooms": '+list[5]+'\n"sq_ft": '+list[6]+'\n},\n'
    except:
        break
str+=']\n}'
datastring=json.dumps(str)
print(str)
