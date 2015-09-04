d3.csv("data.csv", function (d) {
  var r9 = d.filter(function (data){return data["Region"] === "R9-Pacific Rim Region"});
  var table = d3.select('div#forecast').append("table").attr("id","forecastTable")
  table.append("thead").append("tr").append("th").text("Description")
  var tr = table.append("tbody").selectAll("tr").data(d).enter().append("tr").append('td')
  tr.html(function (d, i){ return d["Product or Service Description"]})
  $("#forecastTable").DataTable()
})
