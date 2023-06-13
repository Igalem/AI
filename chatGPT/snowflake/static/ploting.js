// Check the number of fields and execute the relevant function for creating the graph
function createGraph(data, element) {
    const numFields = data[0].length;
    console.log('**** Number of fields fot data = ', numFields)
    if (numFields === 1) {
        createBarGraphSingleField(data, element);
    } else if (numFields === 2) {
        createBarAndLineGraph(data, element);
    } else if (numFields === 3) {
        createLineChartThreeFields(data, element);
    } else {
        console.error('Unsupported number of fields.');
    }
}


// Function to create a bar graph for data with a single field
function createBarGraphSingleField(response, element) {
    const [label, value] = response;

    // Create a new bar chart instance
    new Chart(element, {
      type: 'bar',
      data: {
        labels: [label],
        datasets: [
          {
            label: label,
            data: [value],
            backgroundColor: getRandomColor(), // Adjust the color as needed
            barThickness: 20, // Adjust the bar width here (in pixels)
            barPercentage: 0.5 // Adjust the bar size relative to the available space (0.1 to 1)
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: false
          }
        }
      }
    });

};

 // Function to create a bar graph for data with multiple fields
function createBarGraphMultiFields(response,element) {
    console.log("2 FIELD PLOT");
    // Convert data into separate arrays for labels and values
    const labels = response.map(entry => entry[0]);
    const values = response.map(entry => entry[1]);

    // Remove the first index (header) from labels and values
    labels.shift();
    values.shift();

    var chart = new Chart(element, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Chart Data',
                data: values,
                backgroundColor: getRandomColor(), //'rgba(0, 123, 255, 0.5)'
                // borderWidth: 6,
                barThickness: 20, // Adjust the bar width here (in pixels)
                barPercentage: 0.5 // Adjust the bar size relative to the available space (0.1 to 1)
            }]
        },
        options: {
            legend: {
                display: true,
                position: 'top',
                labels: {
                    fontColor: '#333',
                    fontSize: 14
                    }
                },
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false
                    }
            }
        }
    });
};

// ----------------------------------------
function createBarAndLineGraph(response, element) {
    console.log("2 FIELD PLOT");
    // Convert data into separate arrays for labels and values
    const labels = response.map(entry => entry[0]);
    const barValues = response.map(entry => entry[1]);
  
    // Remove the first index (header) from labels and values
    labels.shift();
    barValues.shift();

    var barData = {
        labels: labels,
        datasets: [{
        label: 'Bar Data',
        data: barValues,
        backgroundColor: getRandomColor(),
        barThickness: 20,
        barPercentage: 0.5
        }]
    };

    var lineData = {
    labels: labels,
    datasets: [{
        label: 'Line Data',
        data: barValues,
        borderColor: getRandomColor(),
        fill: false
      }]
    };
  
    var chart = new Chart(element, {
      type: 'bar',
      data: barData,
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: false,
            position: 'left'
          },
          y1: {
            beginAtZero: false,
            position: 'right',
            grid: {
              drawOnChartArea: true
            }
          }
        },
        plugins: {
          tooltip: {
            mode: 'index',
            intersect: false
          }
        }
      }
    });
  
    chart.data.datasets.push({
      ...lineData.datasets[0],
      type: 'line',
      yAxisID: 'y1'
    });
    chart.update();
};

// ----------------------------------------




// Function to create a line chart for data with three fields
function createLineChartThreeFields(data, element) {
    const labels = [];
    const datasets = [];
  
    const years = [];
    const fields = data[0].slice(2);
  
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const year = String(row[0]);
    //   const month = parseInt(row[1]);
    const month = row[1];
  
      if (!years.includes(year)) {
        years.push(year);
        datasets.push({
          label: year,
          data: [],
          fill: false,
          borderColor: getRandomColor(),
          borderWidth: 2
        });
      }
  
      const value = row[2];
      datasets[years.indexOf(year)].data.push({ x: month, y: value });
      if (!labels.includes(month)) {
        labels.push(month);
      }
    }
  
    new Chart(element, {
      type: 'line',
      data: {
        labels: labels.map(String),
        datasets: datasets
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: false
          }
        }
      }
    });
  }

// Helper function to generate random colors
// function getRandomColor() {
//     const letters = '0123456789ABCDEF';
//     let color = '#';
//     for (let i = 0; i < 6; i++) {
//         color += letters[Math.floor(Math.random() * 16)];
//     }
//     return color;
// }
function getRandomColor() {
    const colors = [
        'rgb(75, 0, 192)',
        'rgb(0, 147, 192)',
        'rgb(0, 192, 160)',
        'rgb(192, 122, 0)',
        'rgb(192, 48, 0)',
        'rgb(192, 0, 138)', 
        'rgb(76, 40, 128)',
        'rgb(34, 122, 100)',
        'rgb(75, 117, 75)', 
        'rgb(125, 114, 11)'
        ];

        const randomIndex = Math.floor(Math.random() * colors.length);
    // console.log("color picked: ", colors[randomIndex]);
    return colors[randomIndex];
}
