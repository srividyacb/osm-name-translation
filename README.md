## tilereduce-translation

Localization of `name` tags using tilereduce
- Uses tilereduce - [osm-tag-stats](https://github.com/mapbox/osm-tag-stats) to extract `name` tags which don't have `name:kn tags` (see `tags.json` file for filters).
- Uses geojson output of tilereduce and converts to csv for easy translation.
- Uses [osmapi](http://osmapi.metaodi.ch/) a python module to upload the changed `name:kn` tags to OPenStreetMap. (add user credentials in `upload.py` script)
