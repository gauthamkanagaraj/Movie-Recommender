let mood;
let decade;
let streaming;

$(".q1o").on("click", function () {
    mood = $(this).attr("value");
    $(".question1").fadeOut();
    $(".question2").fadeIn();
});

$(".q2o").on("click", function () {
    decade = $(this).attr("value");
    $(".question2").fadeOut();
    $(".question3").fadeIn();
});

$(".streamingbutton").on("click", function () {
    streaming = $(this).attr("value");
    $(".question3").fadeOut();
    $(".recommendations").fadeIn();
});