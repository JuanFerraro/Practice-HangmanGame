/* document.getElementById("btnComienza").addEventListener("click", myGame); */
document.getElementById("btnComienza").addEventListener("click", function (event) {
    event.preventDefault();
    myGame();
});
let btnComienza = document.getElementById("btnComienza");
let wordContainer = document.getElementById("wordContainer");
let keyboardContainer = document.getElementById("keyboardContainer");
let failsContainer = document.getElementById("failsContainer");
let word = document.getElementById("word").value;
let clue = document.getElementById("clue").value;
let maxAttempts = 5;


function myGame() {
    /* Creating word input */
    let wordLetters = createInputs()
    /* Creating keyboard options */
    createKeyboard(wordLetters)
    /* Creating attemps counter */
    createAttemptsCounter()
}

function createInputs() {
    word = word.toUpperCase()

    /* List with the letters in word */
    var wordLetters = word.split("");

    /* Cleaning containers */
    wordContainer.innerHTML = "";
    clueContainer.innerHTML = "";

    /* Add clue paragraph  */
    var clueParagraph = document.createElement("p");
    clueParagraph.textContent = clue;
    clueContainer.appendChild(clueParagraph)

    wordLetters.forEach(function (letter) {
        var input = document.createElement("input");
        input.type = "password";
        input.value = letter;
        wordContainer.appendChild(input);
    });

    return wordLetters;
}

function createKeyboard(wordLetters) {
    /* Spanish Alphabet */
    let alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";

    /* Create the keyboard form */
    let keyboardForm = document.createElement("form");

    /* Creating button for every letter */
    for (let i = 0; i < alphabet.length; i++) {
        let letter = alphabet[i];
        let button = document.createElement("button");
        button.textContent = letter;
        button.value = letter;
        button.setAttribute('name', letter)
        console.log(button.name)

        /* Add click event */
        button.addEventListener("click", function (event) {
            event.preventDefault();
            console.log('click')
            console.log(button.name)
            checkLetter(button.name, wordLetters);
        });

        keyboardForm.appendChild(button);
    }

    /* Add the keyboard form to keyboardContainer */
    keyboardContainer.appendChild(keyboardForm);
}

function checkLetter(letter, wordLetters) {
    /* Get wordLetters inputs */
    var wordInputs = wordContainer.getElementsByTagName("input");
    console.log('checkLetter->', letter)
    /*  console.log(typeof(wordInputs))
     console.log(wordInputs.length) */
    /* Verify if letter is in inputs */
    if (wordLetters.includes(letter)) {
        for (var i = 0; i < wordLetters.length; i++) {
            if (wordLetters[i] === letter) {
                /* Change type to text */
                wordInputs[i].type = "text";
            }
        }
    } else {
        /* Decrease attempts counter */
        maxAttempts--;
        /* Update attempts input value */
        let attemptsInput = failsContainer.querySelector(".attemptsInput");
        console.log('Attempts -> ',maxAttempts)
        attemptsInput.value = maxAttempts;

        /* Check if no more attempts remaining */
        if (maxAttempts === 0) {
            // Handle game over logic
        }
    }
}

function createAttemptsCounter() {
    /* Create the heading for attempts */
    let heading = document.createElement("h3");
    heading.textContent = "Intentos Restantes: ";

    /* Create the input for remaining attempts */
    let attemptsInput = document.createElement("input");
    attemptsInput.type = "text";
    attemptsInput.value = maxAttempts;
    attemptsInput.setAttribute("class", "attemptsInput")
    attemptsInput.disabled = true;

    /* Append heading and input to attempts counter */
    failsContainer.appendChild(heading);
    failsContainer.appendChild(attemptsInput);

}
