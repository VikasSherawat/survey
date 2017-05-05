numTextBox = 4;
$(document).ready(function(){
    var csrf = jQuery("[name=csrfmiddlewaretoken]").val();
    console.log(csrf);
    registerInput();
    hideDivision();
});

function hideDivision() {
    $(".secdiv").hide();
    $("#divForm1").show();
}

function registerInput() {
    $("#btn_choice").click(addTextBox);
    $("#btn_reset").click(removeTextBox);
    $("#btn_next").click(toggleDiv);
    $("#btn_prev").click(toggleDiv);
    $("#btn_submit").click(sendData);
    $("#heading").dblclick(filldata);
}

function filldata() {
    $("#question").val("Some Random Question?");
    $("#textbox1").val("Choice 1");
    $("#textbox2").val("Choice  2");
}

function sendData() {
    var email = $("#email");
    var emailArray = email.val().split(",");
    if(!email.val()){
        email.after('<div><label class="error">Invalid Email, Please enter the email</label></div>');
        return false;
    }else{
        $(".error").remove();
    }
    var i;
    for(i=0;i<emailArray.length; i++){
        if(!isEmail(emailArray[i])){
            console.log("Invalid Email"+emailArray[i]);
            email.after('<div><label class="error">Invalid Email, Please correct the email '+emailArray[i]+'</label></div>');
            return false;
        }
    }
    $(".error").remove();
    $("#pollform").submit();
}

function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function toggleQuestion(){
    var questionField = $('#question');
    var readOnly = questionField.is('[readonly]');
    questionField.attr("readOnly",!readOnly);
}

function toggleDiv() {
    var question =$("#question");
    var choice1 = $("#textbox1");
    var choice2 = $("#textbox2");
    if (!question.val()) {
        question.focus();
        $(".error").remove();
        question.after('<div><label class="error">Question is Mandatory</label></div>');
    }else if (!choice1.val()) {
        choice1.focus();
        $(".error").remove();
        choice1.after('<div id="error1"><label class="error">Choice 1 is Mandatory</label></div>');
    }else if (!choice2.val()) {
        choice2.focus();
        $(".error").remove();
        choice2.after('<div id="error2"><label class="error">Choice 2 is Mandatory</label></div>');
    }else {
        $(".error").remove();
        toggleQuestion();
        $(".secdiv").toggle()
    }
}

function removeTextBox() {
    while(numTextBox>4){
        $("#TextBoxDiv" + numTextBox).remove();
        numTextBox--;
    }
    if(numTextBox===4){
        $(".txt_choice:not(:first)").val("");
        return false;
    }
}

function addTextBox() {

    if(numTextBox>=20){
        alert("Oops! Sorry Can't add more than 20 choices");
        return false;
    }
    for(i = 0;i<3;i++){
        numTextBox++;
        var newTextBoxDiv = $(document.createElement('div'))
            .attr({"id": 'TextBoxDiv' + numTextBox,"class":'mydiv'});
        newTextBoxDiv.after().html('<input type="text" name="textbox' + numTextBox +
            '" id="textbox' + numTextBox + '" value="" ' +
            'class="form-control input-lg txt_choice" placeholder="Choice '+numTextBox+'">');
        newTextBoxDiv.appendTo("#TextBoxesGroup");
        if(numTextBox>=20){
        alert("Oops! Sorry Can't add more than 20 choices");
        return false;
    }

    }
}