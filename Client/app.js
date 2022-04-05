function getClassValue() {
  var uiClass = document.getElementsByName("cltype");
  for(var i in uiClass) {
    if(uiClass[i].checked) {
        return uiClass[i].value;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var airline = document.getElementById("uiAirlines");
  var time = document.getElementById("uiTime");
  var source = document.getElementById("uiDeparture");
  var destination = document.getElementById("uiDestination");
  var class_type =  getClassValue();
  var estPrice = document.getElementById("uiEstimatedPrice");

var url = "http://localhost:5000/predict_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

$.post(url, {
   airline: airline.value,
   time: time.value,
   source: source.value,
   destination: destination.value,
	 class_type: class_type,
},function(data, status) {
    //console.log(data);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
    console.log(status);
  });
}
