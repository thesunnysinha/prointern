alert("Welcome to ProIntern");
var age = prompt("What is your age? ");
alert("Thank you for the information");
console.log("You are a cool Person!");




var agecount = null;

if (age >18){
  agecount = true;
}
else {
  agecount=false;
}

if (agecount) {
  console.log("Welcome comrade! You are above age limit");
}
else {
  console.log("Sorry,You age is " + age+" and you do not have the access.");
}

var application_header = document.querySelector("#leave_message")

function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = "#";
  for(var i=0;i<6;i++){
    color += letters[Math.floor(Math.random()*16)];
  }
  return color;
}

function changeApplicationHeaderColor(){
  colorInput = getRandomColor();
  application_header.style.color = colorInput;  

}
setInterval("changeApplicationHeaderColor()",400);





