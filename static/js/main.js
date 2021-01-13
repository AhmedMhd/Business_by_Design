var options = {
  series: [{
  name: 'Net Profit',
  data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
}, {
  name: 'Revenue',
  data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
}, {
  name: 'Free Cash Flow',
  data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
}],
  chart: {
  type: 'bar',
  height: 350
},
plotOptions: {
  bar: {
    horizontal: false,
    columnWidth: '55%',
    endingShape: 'rounded'
  },
},
dataLabels: {
  enabled: false
},
stroke: {
  show: true,
  width: 2,
  colors: ['transparent']
},
xaxis: {
  categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
},
yaxis: {
  title: {
    text: '$ (thousands)'
  }
},
fill: {
  opacity: 1
},
tooltip: {
  y: {
    formatter: function (val) {
      return "$ " + val + " thousands"
    }
  }
}
};

var chart = new ApexCharts(document.querySelector("#chart1"), options);
chart.render();



// Chart-2

var options = {
  series: [{
  name: 'PRODUCT A',
  data: [44, 55, 41, 67, 22, 43]
}, {
  name: 'PRODUCT B',
  data: [13, 23, 20, 8, 13, 27]
}, {
  name: 'PRODUCT C',
  data: [11, 17, 15, 15, 21, 14]
}, {
  name: 'PRODUCT D',
  data: [21, 7, 25, 13, 22, 8]
}],
  chart: {
  type: 'bar',
  height: 350,
  stacked: true,
  toolbar: {
    show: true
  },
  zoom: {
    enabled: true
  }
},
responsive: [{
  breakpoint: 480,
  options: {
    legend: {
      position: 'bottom',
      offsetX: -10,
      offsetY: 0
    }
  }
}],
plotOptions: {
  bar: {
    horizontal: false,
  },
},
xaxis: {
  type: 'datetime',
  categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
    '01/05/2011 GMT', '01/06/2011 GMT'
  ],
},
legend: {
  position: 'right',
  offsetY: 40
},
fill: {
  opacity: 1
}
};

var chart = new ApexCharts(document.querySelector("#ch"), options);
chart.render();



// Chart 3
var options = {
  series: [44, 55, 67, 83],
  chart: {
  height: 350,
  type: 'radialBar',
},
plotOptions: {
  radialBar: {
    dataLabels: {
      name: {
        fontSize: '22px',
      },
      value: {
        fontSize: '16px',
      },
      total: {
        show: true,
        label: 'Total',
        formatter: function (w) {
          // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
          return 249
        }
      }
    }
  }
},
labels: ['Apples', 'Oranges', 'Bananas', 'Berries'],
};

var chart = new ApexCharts(document.querySelector("#c"), options);
chart.render();



// chart4

var options = {
  series: [{
  name: "SAMPLE A",
  data: [
  [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 0], [10.9, 8.2], [16.4, 0], [16.4, 1.8], [13.6, 0.3], [13.6, 0], [29.9, 0], [27.1, 2.3], [16.4, 0], [13.6, 3.7], [10.9, 5.2], [16.4, 6.5], [10.9, 0], [24.5, 7.1], [10.9, 0], [8.1, 4.7], [19, 0], [21.7, 1.8], [27.1, 0], [24.5, 0], [27.1, 0], [29.9, 1.5], [27.1, 0.8], [22.1, 2]]
},{
  name: "SAMPLE B",
  data: [
  [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 9], [1.9, 13.2], [1.4, 7], [6.4, 8.8], [3.6, 4.3], [1.6, 10], [9.9, 2], [7.1, 15], [1.4, 0], [3.6, 13.7], [1.9, 15.2], [6.4, 16.5], [0.9, 10], [4.5, 17.1], [10.9, 10], [0.1, 14.7], [9, 10], [12.7, 11.8], [2.1, 10], [2.5, 10], [27.1, 10], [2.9, 11.5], [7.1, 10.8], [2.1, 12]]
},{
  name: "SAMPLE C",
  data: [
  [21.7, 3], [23.6, 3.5], [24.6, 3], [29.9, 3], [21.7, 20], [23, 2], [10.9, 3], [28, 4], [27.1, 0.3], [16.4, 4], [13.6, 0], [19, 5], [22.4, 3], [24.5, 3], [32.6, 3], [27.1, 4], [29.6, 6], [31.6, 8], [21.6, 5], [20.9, 4], [22.4, 0], [32.6, 10.3], [29.7, 20.8], [24.5, 0.8], [21.4, 0], [21.7, 6.9], [28.6, 7.7], [15.4, 0], [18.1, 0], [33.4, 0], [16.4, 0]]
}],
  chart: {
  height: 350,
  type: 'scatter',
  zoom: {
    enabled: true,
    type: 'xy'
  }
},
xaxis: {
  tickAmount: 10,
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1)
    }
  }
},
yaxis: {
  tickAmount: 7
}
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();


