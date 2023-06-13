fetch('/chart-data')
    .then(response => response.json())
    .then(data => {
        const labels = data.response.slice(1).map(entry => entry[0]);
        const values = data.response.slice(1).map(entry => entry[1]);

        var options = {
            chart: {
                height: 350,
                type: 'line',
                stacked: false
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: 'Total Spend',
                type: 'column',
                data: values
            }, {
                name: 'Total Spend',
                type: 'line',
                data: values
            }],
            stroke: {
                width: [1, 4]
            },
            xaxis: {
                categories: labels
            },
            yaxis: [{
                axisTicks: {
                    show: true
                },
                axisBorder: {
                    show: true,
                    color: '#008FFB'
                },
                labels: {
                    style: {
                        colors: '#008FFB'
                    }
                },
                title: {
                    text: "Total Spend (USD)",
                    style: {
                        color: '#008FFB'
                    }
                },
                tooltip: {
                    enabled: true
                }
            }],
            tooltip: {
                fixed: {
                    enabled: true,
                    position: 'topLeft', // topRight, topLeft, bottomRight, bottomLeft
                    offsetY: 30,
                    offsetX: 60
                }
            },
            legend: {
                horizontalAlign: 'left',
                offsetX: 40
            }
        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
    });
