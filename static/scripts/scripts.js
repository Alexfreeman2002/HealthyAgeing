var isSpeaking = false;

function speakText(elementId) {
    // Get the text content of the element with the specified ID
    var text = document.getElementById(elementId).textContent;

    // Create a new instance of SpeechSynthesisUtterance
    var utterance = new SpeechSynthesisUtterance(text);

    // Check if speech synthesis is currently speaking
    if (isSpeaking) {
        // If speaking, stop speaking
        speechSynthesis.cancel();
        isSpeaking = false; // Update speech status
        return; // Exit function
    }

    // Speak the text
    speechSynthesis.speak(utterance);

    // Update speech status
    isSpeaking = true;

    // Event listener to cancel speech when leaving the webpage
    window.addEventListener('beforeunload', function(event) {
        // Check if speech synthesis is currently speaking
        if (isSpeaking) {
            // If speaking, cancel the current speech
            speechSynthesis.cancel();
            isSpeaking = false; // Update speech status
        }
    });
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
