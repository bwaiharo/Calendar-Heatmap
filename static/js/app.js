var c_url = "/countryData";
var cntryArray = [];

  d3.json(c_url, function(response) { 

     var cntry = response[0]['Countries']

    cntry.forEach(e => cntryArray.push(e))
  });


console.log(cntryArray)
var dateRep;
  var h_url = "/holidayData/austria";
  d3.json(h_url, function(response) {

      dateRep = response[0]["2020"];
      for(let i = 0; i < dateRep.length; i++){
      console.log(dateRep[i]['Date']);
      }
     
    });

    // var isoDate = new Date('april12020').toISOString(); 
      var cal = new CalHeatMap();
      cal.init({itemSelector: "#cal-heatmap",
                data: {"1585709627125" : 12},
                domain: "month",
                cellSize: 20,
                subDomainTextFormat: "%d",
                cellRadius: 10,
                displayLegend: false,
                onClick: function(date, nb) {
                  $("#cal-response").html("You just clicked <br/>on <b>" +
                    date + "</b> <br/>with <b>" +
                    (nb === null ? "unknown" : nb) + "</b> items"
                  );
                }});
 

    
// console.log(isoDate);

var d = new Date();
var seconds = Math.round(d.getTime() / 1000);
  
console.log(seconds);


      
 


