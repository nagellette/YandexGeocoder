# -*- coding: utf-8 -*-
__author__ = 'Necip Enes Gengec'
import urllib2
import json
import YandexGeocoderDefs as geocoderDefs

# open input address data and pass the addresses into new list
f_in = open('geocode_input')
addresses = f_in.readlines()
f_in.close()

f_out = open('geocode_output', 'w')
f_out.write('Address' + '\t' + 'Results' + '\t'  + 'Found' + '\t' + 'Kind' + '\t' + 'Precision' + '\t' + 'Lat' + '\t' + 'Lon' + '\n')

# loop on the address list and send response and get geocoded responds
for address in addresses:

    geocodeURL = 'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=' + address.rstrip()

    # open response url and convert to json
    responsecontent = urllib2.urlopen(geocodeURL)
    jsonresponse = json.load(responsecontent)

    # get geocode count for single address from meta info of geocode
    geocodeCount = geocoderDefs.yandexMetaAnalysis(jsonresponse)

    # get geocode results from json if count>0 else pass empty geocode field
    if geocodeCount[1] >= 1:
        geocoded_addresses = geocoderDefs.yandexGetGeocode(jsonresponse)
        for geocoded_address in geocoded_addresses:
            f_out.write(address.rstrip() + '\t' + geocodeCount[0] + '\t'  + geocodeCount[1] + '\t' + geocoded_address[0] + '\t' + geocoded_address[1] + '\t' + geocoded_address[2] + '\t' + geocoded_address[3] + '\n')
    else:
        f_out.write(address.rstrip() + '\t' + geocodeCount[0] + '\t'  + geocodeCount[1] + '\t' + '' + '\t' + '' + '\t' + '' + ' ' + '' + '\n')


f_out.close()