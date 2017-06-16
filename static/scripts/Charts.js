/**
 * Created by Kedepo on 16-6-2017.
 */

function makeChart(id_canvas, time_list, value_list, color) {
    const CHART = document.getElementById(id_canvas);
    var line_chart = new Chart(CHART, {
        type: 'line',
        data: data = {
            labels: time_list,
            datasets: [{
                label: "Time Lapse drink in Bowl",
                fill: false,
                lineTension: 0.1,
                backgroundColor: color,
                borderColor: color,
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'milter',
                pointBorderColor: "rbga(75, 192, 192, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: color,
                pointHoverBorderColor: color,
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: value_list
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    stacked: true
                }]
            }
        }
    });
}

