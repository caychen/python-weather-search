#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: Graphic.GraphicWeatherSearch

@email: 412425870@qq.com
'''
import tkinter
from WeatherSearch.WeatherSearch import WeatherSearch
from html.parser import HTMLParser

def insert_after(area, s):
    area.insert(tkinter.END, s + '\n')

def searchWeather(city, area):
    area.delete(0.0,tkinter.END)
    weatherJson = WeatherSearch(city).search()
    insert_after(area, str('英文: ' + weatherJson['nameen'].capitalize()))
    insert_after(area, str('城市名: ' + weatherJson['cityname']))
    insert_after(area,str('城市天气编号: ' + weatherJson['city']))
    insert_after(area,str('摄氏度: ' + weatherJson['temp'] + '℃'))
    insert_after(area,str('华氏度: ' + weatherJson['tempf'] + '℉'))
    insert_after(area,str('风向: ' + weatherJson['WD']))
    insert_after(area,str('风级: ' + weatherJson['WS']))
    insert_after(area,str('风速: ' + HTMLParser().unescape(weatherJson['wse'])))
    insert_after(area,str('相对湿度: ' + weatherJson['SD']))
    insert_after(area,str('更新时间: ' + weatherJson['time']))
    insert_after(area,str('天气: ' + weatherJson['weather']))
    insert_after(area,str('空气质量指数: ' + weatherJson['aqi']))
    insert_after(area,str('PM2.5: ' + weatherJson['aqi_pm25']))
    insert_after(area,str('日期: ' + weatherJson['date']))
    pass

def aaa():
    print('....')

def initGraphic():
    app = tkinter.Tk()
    app.title('天气查询')
    label = tkinter.Label(app, text='请输入需要查询的城市: ')
    city = tkinter.Entry(app, width='40')
    search = tkinter.Button(app, text='查询', width='10', command=lambda:searchWeather(city.get(),area))
    area = tkinter.Text(app,width='40',height='14')
    
    #search.bind('<Return>', lambda:searchWeather(city.get(),area))
    label.pack()
    city.pack()
    search.pack()
    area.pack()
    city.focus()
    app.mainloop()
    pass

if __name__ == '__main__':
    initGraphic()