// const story = document.body.querySelector(".story");

// const setText = document.body.querySelector("#set-text");
// setText.addEventListener("click", () => {
//     story.textContent = "It was a dark and stormy night...";
//     story.value = "It was a dark and stormy night...";
// });

// const clearText = document.body.querySelector("#clear-text");
// clearText.addEventListener("click", () => {
//     story.textContent = "";
//     story.value = "";
// });

// https://stackoverflow.com/questions/9916747/why-is-document-body-null-in-my-javascript


document.addEventListener("DOMContentLoaded", function () {
    const story = document.body.querySelector(".story");

    const setText = document.body.querySelector("#set-text");
    setText.addEventListener("click", () => {
        story.textContent = "It was a dark and stormy night...";
        story.value = "It was a dark and stormy night...";
    });
    
    const clearText = document.body.querySelector("#clear-text");
    clearText.addEventListener("click", () => {
        story.textContent = "";
        story.value = "";
    });
});

