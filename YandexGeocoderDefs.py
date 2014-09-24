# -*- coding: utf-8 -*-
__author__ = 'Necip Enes Gengec'
'''
Get Yandex response meta deta
determine response count
'''
def yandexMetaAnalysis(yandexjson):

    return_count = []

    analysisjson = yandexjson
    analysisjson = analysisjson['response']
    analysisjson = analysisjson['GeoObjectCollection']
    analysisjson = analysisjson['metaDataProperty']
    analysisjson = analysisjson['GeocoderResponseMetaData']
    return_count.append(analysisjson['results'])
    return_count.append(analysisjson['found'])

    return return_count

'''
get and return geocoded coordinates
and geocode meta with a list
'''
def yandexGetGeocode(yandexjson):


    analysisjson = yandexjson
    analysisjson = analysisjson['response']
    analysisjson = analysisjson['GeoObjectCollection']
    analysisjson = analysisjson['featureMember']

    temp1 = []
    temp2 = []
    temp3 = []
    counter = 0
    geocodedresponse = []

    for feature in analysisjson:
        #get geocode meta info
        temp1 = feature
        temp1 = temp1['GeoObject']
        temp1 = temp1['metaDataProperty']
        temp1 = temp1['GeocoderMetaData']
        temp2.append(temp1['kind'])
        temp2.append(temp1['precision'])

        #get geocoded coordinates
        temp1 = feature
        temp1 = temp1['GeoObject']
        temp1 = temp1['Point']
        temp3 = temp1['pos'].split()
        temp2.append(temp3[0])
        temp2.append(temp3[1])
        geocodedresponse.append(temp2)
        temp1 = []
        temp2 = []
        temp3 = []
        counter += 1


    return geocodedresponse