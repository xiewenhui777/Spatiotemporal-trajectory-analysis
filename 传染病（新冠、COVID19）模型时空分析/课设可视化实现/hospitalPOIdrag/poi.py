# -*-coding:UTF-8-*-
'''根据行政区域查询'''
import json
import csv
import sys
import requests  # 导入requests库，这是一个第三方库，把网页上的内容爬下来用的

ty = sys.getfilesystemencoding()
import time

las = 1  # 给las一个值1
#ak处需要输入自己的ak值，该ak值可以在百度地图开放平台上去申请
ak = 'ZLLWjwBTj3Ux5eyGqMfob3hFKccstQXV'
out = open('j_str.csv', 'a', newline='')
csv_write = csv.writer(out, dialect='excel')
print(time.time())
print('开始')
urls = []  # 声明一个数组列表
que = '' \
      '医院'
ta = ''   #	检索分类偏好，与q组合进行检索，多个分类以","分隔
for i in range(0, 20):      #此处设置了20个URL
    page_num = str(i)
    url = 'http://api.map.baidu.com/place/v2/search?query=' + que + '&' \
                                                                    'tag=' + ta + '&region=石家庄&page_size=20&page_num=' + str(
        page_num) + '&output=json&ak=' + ak
    urls.append(url)
print('url列表读取完成')
for url in urls:
    time.sleep(5)  # 为了防止并发量报警，设置了一个5秒的休眠。
    print(url)
    html = requests.get(url)  # 获取网页信息
    data = html.json()  # 获取网页信息的json格式数据
    print(data)
    for item in data['results']:
        jname1 = item['province']
        jname2 = item['city']
        jname3 = item['area']
        jname4 = item['name']
        jname = jname1 + jname2 + jname3 + jname4 
        j_uid = item['uid']
        jstreet_id = item.get('street_id')
        jlat = item['location']['lat']
        jlon = item['location']['lng']
        jaddress = item['address']
        jphone = item.get('telephone')
        j_str = (jname, j_uid, jstreet_id, str(jlat), str(jlon), jaddress, jphone)
        print(j_str)
        csv_write.writerow(j_str)
        print("write over")
    print(time.time())
print('完成')
