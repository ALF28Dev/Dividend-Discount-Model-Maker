

function callMethod(){
  var tickerSymbol = document.getElementById("tickerSymbol").value;
  var companyName = document.getElementById("companyName").value;
  var currentPrice = document.getElementById("currentPrice").value;
  var companyFloat = document.getElementById("companyFloat").value;
  eel.createModel(tickerSymbol, companyName, currentPrice, companyFloat)(call_Back)  
}
