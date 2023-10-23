var delim = ",";
var csv = document.getElementById('csv');

/*csv.addEventListener('change', function() {
    var reader = new FileReader();
    var f = csv.files[0];
    reader.onload = function(e) {
        var csvArr = parseResult(e.target.result);
        displayTable(csvArr, 'table1');

    };
    reader.readAsText(f);
});

function parseResult(result) {
  var resultArray = [];
  result.split("\n").forEach(function(row) {
      var rowArray = [];
      row.split(delim).forEach(function(cell) {
          rowArray.push(cell);
      });
      resultArray.push(rowArray);
  });
  return resultArray;
}

function displayTable(arr, tname) {
  var table = document.getElementById(tname);
  
  arr.forEach((row) => {
    var r = document.createElement("tr");
    row.forEach((col) => {
      var c = document.createElement("th");;
      c.textContent = col;
      r.appendChild(c);
    });
    table.appendChild(r);
  });
}*/