var fs = require('fs');
var json = fs.readFileSync('./nkn.geojson', 'utf8', function (err, data) {
  if (err) throw err;
});
var obj = JSON.parse(json);
var headers = 'id,name,place‍‍,name:kn';
var output =  headers + '\n';
for (i=0; i<obj.features.length; i++) {
  var tags = [
    obj.features[i].properties["@id"],
    obj.features[i].properties["name"],
    obj.features[i].properties["place"]
  ];
  for (j=0; j<tags.length; j++) {
    if (j+1 == tags.length) {
      output = output + tags[j] + '\n';
    } else {
      output = output + tags[j] + ',';
    }
      }
  }
  console.log(output);
