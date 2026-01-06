const texts = document.querySelectorAll(".bigon");

texts.forEach(function (text) {
  text.addEventListener("mouseover", function () {
    text.style.fontSize = "20px";
  });

  text.addEventListener("mouseout", function () {
    text.style.fontSize = "16px";
  });
});

function addLesson() {
    const lessonsDiv = document.getElementById("lessons");

    const lessonRow = document.createElement("div");
    lessonRow.className = "row mb-2 lesson";

    const nameCol = document.createElement("div");
    nameCol.className = "col";

    const nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.name = "lesson_name";
    nameInput.className = "form-control";
    nameInput.placeholder = "Lesson name";
    nameInput.required = true;

    nameCol.appendChild(nameInput);

    const scoreCol = document.createElement("div");
    scoreCol.className = "col";

    const scoreInput = document.createElement("input");
    scoreInput.type = "number";
    scoreInput.name = "score";
    scoreInput.className = "form-control";
    scoreInput.placeholder = "Your score";
    scoreInput.required = true;

    scoreCol.appendChild(scoreInput);

    lessonRow.appendChild(nameCol);
    lessonRow.appendChild(scoreCol);

    lessonsDiv.appendChild(lessonRow);
}