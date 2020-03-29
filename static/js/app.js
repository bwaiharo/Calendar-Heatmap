var c_url = "/countryData";
var cntryArray = [];

  d3.json(c_url, function(response) { 

     var cntry = response[0]['Countries']

    cntry.forEach(e => cntryArray.push(e))
  });



var dateRep;
  var h_url = "/holidayData";
  d3.json(h_url, function(response) {
//   d3.json(h_url).then(function(response) { 
      // console.log(response[0]["2020"][0]['afghanistan'][0]['Date'])
      dateRep = response[0]["2020"];
      // for(let i = 0; i < cntryArray.length; i++){
            // console.log(cntryArray[i])
            dateRep.forEach(e=>{
          
              console.log(e.kenya)
            
            });
     

    });


      var cal = new CalHeatMap();
      cal.init({itemSelector: "#cal-heatmap",
                data: {946705035: 25},
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
              

    



  



      
 


