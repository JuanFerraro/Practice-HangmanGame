/* Game Start by button 'Comienza' */
document.getElementById("btnComienza").addEventListener("click", function (event) {
    event.preventDefault();
    myGame();
});

/* Main Containers */
let btnComienza = document.getElementById("btnComienza");
let wordContainer = document.getElementById("wordContainer");
let keyboardContainer = document.getElementById("keyboardContainer");
let failsContainer = document.getElementById("failsContainer");
let resultContainer = document.getElementById("resultContainer");

/* Main values */
let word = document.getElementById("word").value;
let clue = document.getElementById("clue").value;
let maxAttempts = 5;

/* Global Score and Max Score */
let score = 0;
let maxScoreContainer = document.getElementById("maxScoreContainer")
let max_score = document.getElementById("maxScore").value;

/* Flag to control localStorage*/
let flag = 0;

/* Flag to control streak */
let flagStreak = 0;

/* Main Function */
function myGame() {
    /* This function run the game */
    
    /* Checking for flag value and then validate it */
    const savedFlag = localStorage.getItem("flag");
    flag = savedFlag ? parseInt(savedFlag) : 0;
    if (flag == 1){
        const savedScore = localStorage.getItem("score");
        score = savedScore ? parseInt(savedScore) : 0;
    };
    /* console.log("flag ->",flag)
    console.log("savedFlag ->", savedFlag) */

    /* Creating word input */
    let wordLetters = createInputs()
    /* Creating keyboard options */
    createKeyboard(wordLetters)
    /* Creating attemps counter */
    createAttemptsCounter()
}

function createInputs() {
    /*  This function create a special input for
        each letter in the hidden word
    */

    /* All the word letter to UPPERCASE */
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

    /* Add hidden letters */
    wordLetters.forEach(function (letter) {
        var input = document.createElement("input");
        input.type = "password";
        input.value = letter;
        wordContainer.appendChild(input);
    });

    /* Return a List of word's letters */
    return wordLetters;
}

function createKeyboard(wordLetters) {
    /*  This function create a keyboard with the spanish alphabet 
        composed by inputs in a form
    */

    /* Cleaning Container */
    keyboardContainer.innerHTML = "";

    /* Spanish Alphabet */
    let alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";

    /* Create the keyboard form */
    let keyboardForm = document.createElement("form");
    keyboardForm.setAttribute("class","keyboardForm")

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
    /*  This function create the info about
        attempts remaining and the score 
    */

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
    /*  This function check if the clicked letter in keyboardContainer
        is in the hidden word, aslo check if the player won the game,
        and deactivate the clicked letter input. 
    */

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
        flagStreak = flagStreak + 1;
        score = score + 1 * (flagStreak);
        /* Update Score */
        let scoreInput = failsContainer.querySelector(".scoreInput");
        scoreInput.value = score;
        isWinner = doYouWin();
        if (isWinner == true) {
            flag = 1;
            console.log("flag ->",flag)
            createResults("👏 Haz ganado! 👏");
            btnComienza.disabled = true;
        }

    } else {
        /* Decrease attempts counter */
        flagStreak = 0;
        maxAttempts--;
        /* Update attempts input value */
        let attemptsInput = failsContainer.querySelector(".attemptsInput");
        attemptsInput.value = maxAttempts;

        /* Check if no more attempts remaining */
        if (maxAttempts === 0) {
            /* let scoreInput = failsContainer.querySelector(".scoreInput");
            score = 0;
            scoreInput.value = score; */
            flag = 0;
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
    /*  This fuction checks if the player won the game 
        it returns true or false in win.
    */
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
    /* Create the input for score */
    /* MACHETAZO - MACHETAZO - MACHETAZO - MACHETAZO -  */
    let scoreInput = document.createElement("input");
    scoreInput.type = "hidden";
    scoreInput.value = score;
    scoreInput.setAttribute("class", "scoreInput")
    scoreInput.disabled = true;
    failsContainer.appendChild(scoreInput);
    /*  MACHETAZO - MACHETAZO - MACHETAZO - MACHETAZO - */


    /* Cleaning resultContainer */
    /* resultContainer.innerHTML = ""; */

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

    /* Div FORMS */
    let divForms = document.getElementById("divForms")

    let playAgainForm = document.getElementById("playAgainForm");
    let inputMaxScoreValue = document.getElementById("inputMaxScore").value;

    /* Check if score is > than max_score */
    if (score > inputMaxScoreValue) {
        let inputMaxScore = document.getElementById("inputMaxScore");
        inputMaxScore.innerHTML = "";
        inputMaxScore.value = score;
    }

    /* Add button new-game */
    let button = document.createElement("button");
    button.textContent = "De nuevo 🔄 ";
    button.setAttribute("type", "submit")
    button.addEventListener("click", function (event) {
        event.preventDefault();
        if(flag == 0){
            score = 0;
        }
        localStorage.setItem("score", score); // Guardar el score en el almacenamiento local
        localStorage.setItem("flag", flag); // Guardar el score en el almacenamiento local
        playAgainForm.submit(); // Recargar la página para comenzar una nueva partida
    });

    playAgainForm.appendChild(button);
    divForms.appendChild(playAgainForm);

    /* Add end game form and button */
    let endGameForm = document.getElementById("endGameForm")

    let button2 = document.createElement("button");
    button2.textContent = " Regresar 🔙 ";
    button2.setAttribute("type", "submit");

    if (score > inputMaxScoreValue) {
        let inputMaxScore = document.getElementById("inputMaxScore");
        inputMaxScore.innerHTML = "";
        inputMaxScore.value = score;
    }

    endGameForm.appendChild(button2);
    divForms.appendChild(endGameForm)

    resultContainer.appendChild(divForms)

    /* Add score message */
    var scoreParagraph = document.createElement("h1");
    scoreParagraph.textContent = "Score:" + score;
    console.log("Score -> ", score)
    resultContainer.appendChild(scoreParagraph)


    // Agrega un evento 'submit' al formulario 'endGameForm'
    endGameForm.addEventListener("submit", function (event) {
        // Detener el envío del formulario
        event.preventDefault();
        /* Restart score to 0 */
        score = 0;
        flag = 0;
        /*  */
        localStorage.setItem("score", score);
        localStorage.setItem("flag", flag);
        endGameForm.submit();
    });


}

