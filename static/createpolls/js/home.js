$(document).ready(function(){
    registerInput();
});


function registerInput() {
    $("#btn_survey").click(sendAjax)
}

function sendAjax() {
    var myname = 'vikas', myage=20;
    $.ajax({
    url:'/',
    type: "POST",
    data: {name: myname, age: myage},
    success:function(response){
        console.log("Successfully post the data");
        console.log("data is"+response.name+":"+response.age);
    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        console.log("Error Occured"+thrownError+xhr+textStatus);
    }
});
}