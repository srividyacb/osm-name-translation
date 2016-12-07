# -*- coding: utf-8 -*-
import osmapi
import sys
import csv
import json

inputFile = sys.argv[1]
inputLanguage = sys.argv[2]
log = sys.argv[3]

api = osmapi.OsmApi(api="api06.dev.openstreetmap.org", username = "stest", password = "yspasswdys")
api.ChangesetCreate({u"comment": u"adding kn name tags"})

def get_osm_type (osm_id, osm_type):
    if osm_type == 'node':
        node = api.NodeGet(int(osm_id))
        return node
    elif osm_type == 'way':
        way = api.WayGet(int(osm_id))
        return way
    elif osm_type == 'relation':
        relation = api.RelationGet(osm_id)
        return relation
    else:
        print "invalid type %s" % osm_type

def osm_upload (osm_type, osm_object):
    if osm_type == 'node':
        node = api.NodeUpdate(osm_object)
        return node
    elif osm_type == 'way':
        way = api.WayUpdate(osm_object)
        return way
    elif osm_type == 'relation':
        relation = api.RelationUpdate(osm_object)
        return relation

with open(inputFile, 'r') as csvfile:
    logFile = open(log, 'w')
    rows = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in rows:
        if i == 0:
            i = i+1
            continue
        osm_id = row[0]
        osm_type = str(row[1])
        translation = str(row[2]).strip('\n')
        translation = translation.decode('utf-8')
        try:
            typeContent = get_osm_type (osm_id, osm_type)
            if ('name:'+ inputLanguage in typeContent['tag']):
                osmContent = typeContent['tag']['name:'+ inputLanguage]
                if osmContent == translation:
                    print (osmContent, translation)
                    print ('Translation present in OpenStreetMap')
                    logFile.write('Translation present in OSM' + '\n')
                else:
                    print (osmContent, translation)
                    print ('MisMatched Translation in OpenStreetMap')
                    logFile.write('MisMatched Translation in OpenStreetMap' +'\n')
            else:
                typeContent['tag']['name:'+ inputLanguage] = translation
                osm_upload(osm_type, typeContent)
                print ('Uploaded new translation to OpenStreetMap')
                logFile.write('Uploaded new translation to OpenStreetMap' + '\n')
        except ValueError:
            print "ValueError occurred"
            continue
api.ChangesetClose()
