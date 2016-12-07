## tilereduce-translation

**Note**

Scripted imports and automated edits should only be carried out by those with experience and understanding of the way the OpenStreetMap community. See the [Import/Guidelines](http://wiki.openstreetmap.org/wiki/Import/Guidelines) and [Automated Edits/Code of Conduct](http://wiki.openstreetmap.org/wiki/Automated_Edits/Code_of_Conduct) for more information.

### Localization of `name` tags using tilereduce
- Uses tilereduce - [osm-tag-stats](https://github.com/mapbox/osm-tag-stats) to extract `name` tags which don't have `name:kn tags` (see `tags.json` file for filters).
- Uses geojson output of tilereduce and converts to csv for easy translation.
- Uses [osmapi](http://osmapi.metaodi.ch/) a python module to upload the changed `name:kn` tags to OPenStreetMap. (add user credentials in `upload.py` script)


### Upload language tags to OpenStreetMap from `csv`

**Sample CSV**

```
id,type,name:kn
4305340953,node,<your-translation>
.....
```
**Arguments required**

1. `username` : [OpenStreetMap](https://www.openstreetmap.org/login?referer=%2F) username </br>
(*Note: Create your test account in [OSM dev server](http://master.apis.dev.openstreetmap.org/login?referer=%2F) if you are testing. You need to create your custom data while testing*)
2. `userPassword` : Your associated account password (****)
3. `inputFile` : Input `csv` file with translations
4. `inputLanguage` : Language-code tag to which the translations are updated (example `kn`)
5. `logFile` : A log file which logs all the activities

**How to execute**

```
python upload.py <osm-username> <password> <inputfile.csv> <languagecode> <outputLog>
```
