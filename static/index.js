let mood;
let streaming;
let sort;

$(".q1o").on("click", function () {
    mood = $(this).attr("value");
    $(".question1").fadeOut();
    $(".question3").fadeIn();
});

$(".streamingbutton").on("click", function () {
    streaming = $(this).attr("value");
    $(".question3").fadeOut();
    $(".question4").fadeIn();
});

$(".q4o").on("click", function () {
    sort = $(this).attr("value");
    $(".question4").fadeOut();
    $.ajax({
        url: "getResults",
        type: "GET",
        data: {mood, streaming, sort},
        success: function (data) {
            $(".recommendations").fadeIn();
            parsedData = JSON.parse(data);
            console.log(parsedData);
            if(sort == 'random') {
                $(".rec1").text(parsedData[0]);
                $(".rec2").text(parsedData[1]);
                $(".rec3").text(parsedData[2]);
            }
            else if(sort == 'rating') {
                $(".rec1").text(parsedData[1][0] + " (" + parsedData[0][0] + ")");
                $(".rec2").text(parsedData[1][1] + " (" + parsedData[0][1] + ")");
                $(".rec3").text(parsedData[1][2] + " (" + parsedData[0][2] + ")");
            }
            

      }
    });
});