/* document.getElementById("btnComienza").addEventListener("click", myGame); */
document.getElementById("btnComienza").addEventListener("click", function (event) {
    event.preventDefault();
    myGame();
});
let btnComienza = document.getElementById("btnComienza");
let wordContainer = document.getElementById("wordContainer");
let keyboardContainer = document.getElementById("keyboardContainer");
let failsContainer = document.getElementById("failsContainer");
let resultContainer = document.getElementById("resultContainer");

let word = document.getElementById("word").value;
let clue = document.getElementById("clue").value;
let maxAttempts = 5;
/* Global Score */
let score = 0;
let max_score = 0;

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
    /* Cleaning Container */
    keyboardContainer.innerHTML = "";

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

        /* Add click event */
        button.addEventListener("click", function (event) {
            event.preventDefault();
            checkLetter(button.name, wordLetters);
        });

        keyboardForm.appendChild(button);
    }

    /* Add the keyboard form to keyboardContainer */
    keyboardContainer.appendChild(keyboardForm);
}

function createAttemptsCounter() {
    /* Cleaning Container */
    failsContainer.innerHTML = "";

    /* Create the heading for attempts */
    let heading = document.createElement("h3");
    heading.textContent = "Intentos Restantes: ";

    /* Create the heading for score */
    let headingScore = document.createElement("h3");
    headingScore.textContent = "Score: ";

    /* Create the input for remaining attempts */
    let attemptsInput = document.createElement("input");
    attemptsInput.type = "text";
    attemptsInput.value = maxAttempts;
    attemptsInput.setAttribute("class", "attemptsInput")
    attemptsInput.disabled = true;

    /* Create the input for score */
    let scoreInput = document.createElement("input");
    scoreInput.type = "text";
    scoreInput.value = score;
    scoreInput.setAttribute("class", "scoreInput")
    scoreInput.disabled = true;


    /* Append heading and input to attempts counter */
    failsContainer.appendChild(heading);
    failsContainer.appendChild(attemptsInput);
    failsContainer.appendChild(headingScore);
    failsContainer.appendChild(scoreInput);

}

function checkLetter(letter, wordLetters) {
    /* Get wordLetters inputs */
    var wordInputs = wordContainer.getElementsByTagName("input");

    /* Verify if letter is in inputs */
    if (wordLetters.includes(letter)) {
        for (var i = 0; i < wordLetters.length; i++) {
            if (wordLetters[i] === letter) {
                /* Change type to text */
                wordInputs[i].type = "text";
            }
        }
        score = score + 10;
        /* Update Score */
        let scoreInput = failsContainer.querySelector(".scoreInput");
        scoreInput.value = score;
        isWinner = doYouWin();
        if (isWinner == true) {
            createResults("👏 Haz ganado! 👏");
            btnComienza.disabled = true;
        }

    } else {
        /* Decrease attempts counter */
        maxAttempts--;
        /* Update attempts input value */
        let attemptsInput = failsContainer.querySelector(".attemptsInput");
        attemptsInput.value = maxAttempts;

        /* Check if no more attempts remaining */
        if (maxAttempts === 0) {
            createResults("🥺 Haz perdido 🥺");
            btnComienza.disabled = true;
        }
    }

    /* Disable the pressed letter button */
    var keyboardButtons = keyboardContainer.getElementsByTagName("button");
    for (var j = 0; j < keyboardButtons.length; j++) {
        if (keyboardButtons[j].value === letter) {
            keyboardButtons[j].disabled = true;
            break;
        }
    }
}

function doYouWin() {
    let wordInputs = wordContainer.getElementsByTagName("input");
    let win = true;

    for (let index = 0; index < wordInputs.length; index++) {
        if (wordInputs[index].type !== "text") {
            win = false;
            break;
        }
    }
    return win;
}

function createResults(message) {
    /* Cleaning wordContainer */
    wordContainer.innerHTML = "";

    /* Cleaning clueContainer */
    clueContainer.innerHTML = "";

    /* Cleaning keyboardContainer */
    keyboardContainer.innerHTML = "";

    /* Cleaning failsContainer */
    failsContainer.innerHTML = "";

    /* Cleaning resultContainer */
    resultContainer.innerHTML = "";

    /* List with the letters in word */
    var wordLetters = word.split("");
    wordLetters.forEach(function (letter) {
        var input = document.createElement("input");
        input.type = "text";
        input.value = letter;
        input.setAttribute("class", "wordResult")
        wordContainer.appendChild(input);
    });

    /* Add message paragraph */
    var messageParagraph = document.createElement("h1");
    messageParagraph.textContent = message;
    resultContainer.appendChild(messageParagraph);

    /* Add button new-game */
    let button = document.createElement("button");
    button.textContent = "Juega de Nuevo";
    button.addEventListener("click", function (event) {
        event.preventDefault();
        /* Almacenar puntaje actual en el almacenamiento local */
        localStorage.setItem("score", score);
        /* Recargar la página */
        location.reload();
    });
    resultContainer.appendChild(button);

    /* Add score message */
    var scoreParagraph = document.createElement("h1");
    scoreParagraph.textContent = "Score:" + score;
    console.log("Score -> ", score)
    resultContainer.appendChild(scoreParagraph)
}

