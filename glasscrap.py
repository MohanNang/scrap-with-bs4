import requests
from bs4 import BeautifulSoup as bs
import csv
import json

website="https://www.glassdoor.co.in/Job/jobs.htm?location-redirect=true"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "_t_ds=1272d90d1678189793-21272d90d-01272d90d; _abck=133750897717882D35A44EBC4E8E78A7~0~YAAQP60cuB8eQQ+HAQAALe7OIQnBqhkaXBwUj5yyV8uZCR/vqNlRws281K4N5rGa0D7M9mKa0tpMgokew799xTcjIf8SfGxRLGvztSj1myyrt4achfB9vGb0KzpiUzf7xpW9KA3Ml/mCDJ65Mv8xUXmnEDB1fIYLa2YmpONxRgyE54Qh3JrNoCgEeorAgObrqfz4CeB3ix/nJuKri4PnbT1PCeR12gLLkvHgzv/BPWHto14ltU2PZECNkfB4A3S8KsNtHdhDGEdtlqcli870Koc5eNoxQMmbVssmL5HJj8bX0/VIFRPqSO0gu7s/B8wL2tblRIq53Bq7MJ0CDnTeqql1Mt+/UEYu8kHkSH6zVF+RAyKVuz+K1YpC1qLrygjYNVsJBE01ccLgdjWKJlWnGFvrfaJ/IR4A~-1~-1~-1; _gcl_au=1.1.140474594.1678189805; _ga_K2YBNZVRLL=GS1.1.1678249122.2.0.1678249122.0.0.0; _ga=GA1.2.699126308.1678189806; _gac_UA-182658-1=1.1678189810.CjwKCAiA3pugBhAwEiwAWFzwdeim6v1PbF-pFvLtscLDkwfI_m1ZKTfe88Fc09i1qTk91angbw70DRoC-sUQAvD_BwE; _fbp=fb.1.1678189812680.1821581287; test=naukri.com; __gads=ID=a6c47f13521a927e:T=1678189889:S=ALNI_MazpGFkRS7RQIQ6dOKZMDiXsMaH8g; __gpi=UID=00000bd34b8a9826:T=1678189889:RT=1678189889:S=ALNI_MZkwcEZIlsqqSqIYKrq0fFgtxPBfA; ak_bmsc=B957165592C3053045367BE15695B439~000000000000000000000000000000~YAAQP60cuCAeQQ+HAQAALe7OIRNxWsHVM6qCitlZWuDC+IvTMcySg4qHa9na38hn1IPvwPuaCrVnlTRqD2rNx7hy9g1pLlRa3bCM5XwtWOvYoSb6/dqRrpl/wYgLn9Gt3iF26/LEKlKU+hhdKiHGYfAyCISr2XdIXaerOBw3CYk5V80CnADcFJ4CLNvLH0NwAXWi6CfLFtPR/zuvIe9wVtP+AUf2aMrDc7gUpMxieCMLQof2ErsaqC4UBYbA6s5y9y4u1ZZG50Xl1VDlTmszpK1MqVyDF1IcG1jd63pEwO6H3A+PmxmeravF4FE8yQDy+nKK8VDfCu34UPc6XGNyHp4J/w3xPnEUhI7u0rRhmh7G4za2W2cjgtEFreuH/q7+GJb5wa1+VAJ1; bm_sz=636C154D1F17AF4E304376877E67C2C0~YAAQP60cuCEeQQ+HAQAALe7OIRMZxpciTEx0wr7XobXb4o9cJM2dL/V41j3iKt9kcja9rdKugNe2UEx/goOCLn/9VxXYEA0JUdL22QOCvf0pZP/rskcHbMxRFb28HDMx/+USa73jzgtCFwfUypsyVG2v2okYOHYy0I35TBnf5YD45K6mnx0wcR2/ZiiHgxORVyAljvYvqsJnn03pE27u6DBLs4KrVJxsdfwe/shuaeuX2yD434J46zSHCDnh9QiysnkN73+IQ3XC12zKOCJRi9+zjLM02sogjl6Nmpjh5L9RSiY=~3224389~3753283",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers"
    }
Scrap_data=requests.get(url=website,headers=headers)
Source_code=bs(Scrap_data.content, "html.parser")
# total_pages = 30
# for pages in range(total_pages+1):
# with open("sourcefile.csv","a") as f:
# # web_data = open('data_file.csv', 'a+',newline="")
#     # f.write(str(Source_code))

# Opening a csv file to wrie
op= open("sourcefile.csv", 'w')
writer=csv.writer(op)

job_title=[]

# Collecting data to a list
job_title = Source_code.find_all("li",{"class":"eigr9kq3"})
i = {}
row = i['title'],i["location"] = "title","location"
writer.writerow(row)
# looping through the job_title data
for i in job_title:

    # assigning values to title, location
    title=i.find("a",{"class":"eigr9kq2"}).string
    location=i.find("span",{"class":"e1rrn5ka0"}).string
    
    # Declaring a dictionary to save the data as objects
    i = {}

    # Assigning values to keys title, location
    i['title'],i["location"] = title,location

    # Forming a coma seperated row
    row = i['title'],i['location']

    # Writing the dictionary data as rows
    writer.writerow(row)

def create_json():
    csvfile = open('sourcefile.csv', 'r')
    jsonfile = open('twenty_five.json', 'w')
    fieldnames = ('title','location')
    reader = csv.DictReader( csvfile, fieldnames)
    out = json.dumps( [ row for row in reader ] )
    jsonfile.write(out)


create_json()

