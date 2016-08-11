import osmapi
import sys
import csv

api = osmapi.OsmApi(username = u"username", password = u"****")
api.ChangesetCreate({u"comment": u"adding kannada name tags"})

with open('translate.csv', 'rb') as csvfile:
    # csv.reader(csvfile)
    for row in csvfile:
        osm_id = row.split(',')[0]
        translation = row.split(',')[3]
        translation = translation.decode("utf-8")
        try:
            node = api.NodeGet(int(osm_id))
        except ValueError:
            continue
        print node
        node["tag"]["name:kn"] = translation
        node = api.NodeUpdate(node)
api.ChangesetClose()
