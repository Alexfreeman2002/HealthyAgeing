function speakText(elementId) {
    var text = document.getElementById(elementId).innerText;

    // Create a new instance of SpeechSynthesisUtterance
    var utterance = new SpeechSynthesisUtterance(text);

    // Set voice
    utterance.voice = speechSynthesis.getVoices()[0]; // Change index to select different voices

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
var output = document.getElementById("demo");
var hiddenInput = document.getElementById("sliderValue");

output.innerHTML = rangeslider.value;
hiddenInput.value = rangeslider.value;

rangeslider.oninput = function() {
    output.innerHTML = this.value;
    hiddenInput.value = this.value;
}