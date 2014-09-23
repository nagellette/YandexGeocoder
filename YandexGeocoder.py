# -*- coding: utf-8 -*-
__author__ = 'Necip Enes Gengec'
import urllib2
import json
import YandexGeocoderDefs as geocoderDefs

# open input address data and pass the addresses into new list
f = open('geocode_addresses')
addresses = f.readlines()
f.close()

# loop on the address list and send response and get geocoded responds
for address in addresses:

    geocodeURL = 'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=' + address
    #print geocodeURL

    # open response url and convert to json
    responsecontent = urllib2.urlopen(geocodeURL)
    jsonresponse = json.load(responsecontent)

    # get geocode count for single address from meta info of geocode
    geocodeCount = geocoderDefs.yandexMetaAnalysis(jsonresponse)

    # get geocode results from json if count>0 else pass empty geocode field
    if geocodeCount >= 1:
        geocoderDefs.yandexGetGeocode(jsonresponse)
        print geocoderDefs.yandexGetGeocode(jsonresponse)
    else:
        pass