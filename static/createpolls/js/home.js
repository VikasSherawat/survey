    google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
    //google.charts.setOnLoadCallback(drawChart);
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
            drawChart(response.values);
        },
        complete:function(){},
        error:function (xhr, textStatus, thrownError){
            console.log("Error Occured"+thrownError+xhr+textStatus);
        }
    });
}

function chart(response) {
    var data = response.values;
    drawChart(data);
}

function drawChart(values) {

    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows(values);
    // Set chart options
    var options = {'title':'How Much Pizza I Ate Last Night',
        'width':500,
        'height':500};

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}