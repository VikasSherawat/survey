$(document).ready(function(){
    registerInput();
});


function registerInput() {
    $("#save").click(sendAjax)
}

function sendAjax() {
    var qnum = document.getElementById("q_num").value;
    var choiceVal = $("input[name='choice']:checked").val();
    $.ajax({
    url:'/polls/'+qnum+'/vote/',
    type: "POST",
    data: {choice:choiceVal},
    success:function(response){
        location.replace(response.url)

    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        console.log("Error Occured"+thrownError+xhr+textStatus);
    }
});
}