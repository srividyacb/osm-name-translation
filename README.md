## tilereduce-translation

### Localization of `name` tags using tilereduce
- Uses tilereduce - [osm-tag-stats](https://github.com/mapbox/osm-tag-stats) to extract `name` tags which don't have `name:kn tags` (see `tags.json` file for filters).
- Uses geojson output of tilereduce and converts to csv for easy translation.
- Uses [osmapi](http://osmapi.metaodi.ch/) a python module to upload the changed `name:kn` tags to OPenStreetMap. (add user credentials in `upload.py` script)


### Upload to OpenStreetMp from `csv`

**Arguments required**

1. inputFile : Input `csv` file with translations
2. inputLanguage : Language-code tag to which the translations are updated (example `name:kn`)
3. logFile : A log file which logs all the activities

**How to execute**

```
python upload.py <inputfile.csv> <languagecode> <outputLog>
```
