let mood;
let streaming;

$(".q1o").on("click", function () {
    mood = $(this).attr("value");
    $(".question1").fadeOut();
    $(".question3").fadeIn();
});

$(".streamingbutton").on("click", function () {
    streaming = $(this).attr("value");
    $(".question3").fadeOut();
    $.ajax({
        url: "getResults",
        type: "GET",
        data: {mood, streaming},
        success: function (data) {
            $(".recommendations").fadeIn();
            parsedData = JSON.parse(data);
            console.log(parsedData);
            $(".rec1").text(parsedData[0]);
            $(".rec2").text(parsedData[1]);
            $(".rec3").text(parsedData[2]);
            

      }
    });
});