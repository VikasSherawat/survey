// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(sendAjax);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
$(document).ready(function(){
    registerInput();
});

function registerInput() {
    $("#btn_chart").click(sendAjax)
}
function sendAjax() {
    console.log("sending request")
    var qnum = $("#q_num").val();
    $.ajax({
    url:'/polls/'+qnum+'/chart/',
    type: "GET",
    success:function(response){
        drawChart(response);
    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        console.log("Error Occured"+thrownError+xhr+textStatus);
    }
});
}

function drawChart(response) {

    // Create the data table.
    var data = new google.visualization.DataTable();

    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows(response.values);

    // Set chart options
    var options = {'title': '',//response.question.toUpperCase(),
        'width':500,
        'height':500};

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}