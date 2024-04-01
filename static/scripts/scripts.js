function speakText(elementId) {
    var text = document.getElementById(elementId).innerText;

    // Create a new instance of SpeechSynthesisUtterance
    var utterance = new SpeechSynthesisUtterance(text);

    // Set voice
    utterance.voice = speechSynthesis.getVoices()[0]; // Change index to select different voices

    // Speak the text
    speechSynthesis.speak(utterance);
}