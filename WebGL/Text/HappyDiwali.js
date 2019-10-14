// look up the elements we want to affect
var timeElement = document.getElementById("time");
var angleElement = document.getElementById("angle");
 
// Create text nodes to save some time for the browser.
var timeNode = document.createTextNode("");
var angleNode = document.createTextNode("");
 
// Add those text nodes where they need to go
timeElement.appendChild(timeNode);
angleElement.appendChild(angleNode);