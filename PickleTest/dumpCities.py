#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: PickleTest.dumpCities

@email: 412425870@qq.com
'''

def transferCities(file_path):
    file_name, file_ext = file_path.split('.')
    new_file_path = file_name + '_bak.' + file_ext 
    with open(file_path, 'r') as f1:
        with open(new_file_path, 'w') as f2:
            for line in f1:
                code, city = line.rstrip('\n').split('=')
                new_line = '\"' +  city + '\":\"' + code + '\",\n'
                f2.write(new_line)
    pass

if __name__ == '__main__':
    transferCities('cities.txt')
    