__author__ = 'Necip Enes Gengec'
# -*- coding: utf-8 -*-
import urllib2
import json

content = urllib2.urlopen("http://geocode-maps.yandex.ru/1.x/?format=json&geocode=Sultanahmet+Camii+İç+Yolları&lang=en-US")
data = json.load(content)

data = data['response']
data = data['GeoObjectCollection']
data = data['metaDataProperty']
data = data['GeocoderResponseMetaData']
data = data['found']

print data