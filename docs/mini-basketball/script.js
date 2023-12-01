
function addButtons() {
  const buttonsDiv = document.getElementById("buttons");

  const runButton = document.createElement("button");
  runButton.textContent = "▶Run";
  buttonsDiv.appendChild(runButton);
}

window.onload = function() {brython();}
addButtons();
