function speakText(elementId) {
    // Get the text content of the element with the specified ID
    var text = document.getElementById(elementId).textContent;

    // Create a new instance of SpeechSynthesisUtterance
    var utterance = new SpeechSynthesisUtterance(text);

    // Speak the text
    speechSynthesis.speak(utterance);
}

// to show side menu when window is too small
const icon = document.querySelector(".menu-icon");
const nav_mobile = document.getElementById('nav-mobile');

icon.addEventListener("click", () => {
  icon.classList.toggle("clicked");
  nav_mobile.classList.toggle("show");
});

// slider script
var rangeslider = document.getElementById("sliderRange");
var output = document.getElementById("value");
var hiddenInput = document.getElementById("sliderValue");

output.innerHTML = rangeslider.value;
hiddenInput.value = rangeslider.value;

rangeslider.oninput = function() {
    output.innerHTML = this.value;
    hiddenInput.value = this.value;
}
