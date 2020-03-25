var c_url = "/countryData";
//   d3.json(c_url).then(function(response) { 
//       console.log(response)




//   });


  var h_url = "/holidayData";
  d3.json(h_url, function(response) {
//   d3.json(h_url).then(function(response) { 
      console.log(response[0]["2020"][0]['afghanistan'][0]['Date'])

      var cal = new CalHeatMap();
      cal.init({itemSelector: "#cal-heatmap",
                data: response[0]["2020"][0]['afghanistan'][0]['Date'],
                domain: "month"});
              

    });



  



      
 


