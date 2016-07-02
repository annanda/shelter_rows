$(function () {
    // Create the chart
    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Quantidade de gatos x cães no dataset de treinamento'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'category'
        },
        yAxis: {
            title: {
                text: 'Quantidade'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b><br/>'
        },

        series: [{
            name: '',
            colorByPoint: true,
            data: [{
                name: 'Gatos',
                y: 11134,
                color: 'blue'
            }, {
                name: 'Cães',
                y: 15595,
                color: 'green'
            }]
        }],      
    });
});
