#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: WeatherSearch.WeatherSearch

@email: 412425870@qq.com
'''
import pickle
import urllib.request
import json
#from html.parser import HTMLParser

cities = {}

qoute = {'&lt;':'<','&gt;':'>','&le;':'<=','&ge;':'>='}

def replaceChars(s):
    for q in qoute:
        s = s.replace(q, qoute[q])
    return s

class WeatherSearch():
    _url_prefix = 'http://d1.weather.com.cn/sk_2d/' 
    def __init__(self, city):
        loadPickle('../cities.pkl')
        self._city = city
        self._code = cities[self._city] 
        
    def search(self):
        url = self._url_prefix + self._code + '.html'
        #print(url)
        request = urllib.request.Request(url)
        request.add_header('referer', 'http://www.weather.com.cn')
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0')
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #var dataSK = {"nameen":"shanghai","cityname":"上海","city":"101020100","temp":"29","tempf":"84","WD":"东北风","wde":"NE ","WS":"1级","wse":"&lt;12km/h","SD":"78%","time":"11:14","weather":"雨","weathere":"Shower","weathercode":"d03","qy":"1002","njd":"暂无实况","sd":"78%","rain":"0","rain24h":"0.9","aqi":"32","limitnumber":"","aqi_pm25":"57","date":"07月01日(星期五)"}
        #var dataSK = {}
        #print(html)
        weatherJson = json.loads(html[html.find('{'):])
#         
               
        return weatherJson
    

def loadPickle(pkl_path):
    pickle_file = open(pkl_path,'rb')
    global cities
    cities = pickle.load(pickle_file)


if __name__ == '__main__':
    #loadPickle('../cities.pkl')
    city = input('请输入城市的名称: ')
    weatherJson = WeatherSearch(city).search()
    print('英文: ' ,weatherJson['nameen'].capitalize())
    print('城市名: ' ,weatherJson['cityname'])
    print('城市天气编号: ' ,weatherJson['city'])
    print('摄氏度: ' ,weatherJson['temp'], '℃')
    print('华氏度: ' ,weatherJson['tempf'], '℉')
    print('风向: ' ,weatherJson['WD'])
    #print('wde: ' ,weatherJson['wde'])
    print('风级: ' ,weatherJson['WS'])
    #print('风速: ' ,HTMLParser().unescape(weatherJson['wse']))
    print('风速: ' ,replaceChars(weatherJson['wse']).strip())
    print('相对湿度: ' ,weatherJson['SD'])
    print('更新时间: ' ,weatherJson['time'])
    print('天气: ' ,weatherJson['weather'])
    #print('weathere: ' ,weatherJson['weathere'])
    #print('weathercode: ' ,weatherJson['weathercode'])
    #print('qy: ' ,weatherJson['qy'])
    #print('sd: ' ,weatherJson['sd'])
    #print('rain: ' ,weatherJson['rain'])
    #print('rain24h: ' ,weatherJson['rain24h'])
    print('空气质量指数: ' ,weatherJson['aqi'])
    #print('limitnumber: ' ,weatherJson['limitnumber'])
    print('PM2.5: ' ,weatherJson['aqi_pm25'])
    print('日期: ' ,weatherJson['date'])