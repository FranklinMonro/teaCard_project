var choice = document.getElementById('select').value

function show(f){
  var x = f.choice;
  var tb = document.querySelector('td')


  if(x.value === "1"){
    tb.style.backgroundColor = "#66ff33"
  }else if (x.value === "2") {
    tb.style.backgroundColor = "#ff0000"
  }else if (x.value === "3") {

    tb.style.backgroundColor = "#ff9900"
  }else {
    alert("No option has been chocen")
  }




}
