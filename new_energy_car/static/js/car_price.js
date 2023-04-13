$(function () {
    var colorList = ['#73DDFF', '#73ACFF', '#FDD56A', '#FDB36A', '#FD866A', '#9E87FF', '#00FFFF', '#CD5C5C', '#F08080']

    $.ajax({
        type: "POST",
        url: "car_price_data",
        contentType: "application/json",
        data: JSON.stringify({}),//参数列表
        dataType: "json",
        success: function (result) {
            data_display_chart(result.car_data, result.price_data);
        },
        error: function (result) {
        }
    });

    function data_display_chart(car_data, price_data) {
        var myChart = echarts.init(document.getElementById('div_car_price'));
        var color=[
         '#008B8B','#48D1CC','#48D1CC','#20B2AA','#E6E6FA','#0000FF','#0000CD','#191970',
         '#EE82EE','#FF00FF','#98FB98','#8FBC8F','#8B008B','#BA55D3','#90EE90','#32CD32',
         '#FF7F50','#FF6347','#F08080','#FF0000',]
        var option = {
            backgroundColor: '#fff',
            title: {},
            legend: {
                icon: 'circle',
                top: '5%',
                right: '5%',
                itemWidth: 6,
                itemGap: 20,
                textStyle: {
                    color: '#556677'
                }
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    label: {
                        show: true,
                        backgroundColor: '#fff',
                        color: '#556677',
                        borderColor: 'rgba(0,0,0,0)',
                        shadowColor: 'rgba(0,0,0,0)',
                        shadowOffsetY: 0
                    },
                    lineStyle: {
                        width: 0
                    }
                },
                backgroundColor: '#fff',
                textStyle: {
                    color: '#5c6c7c'
                },
                padding: [10, 10],
                extraCssText: 'box-shadow: 1px 0 2px 0 rgba(163,163,163,0.5)'
            },
            grid: {
                top: '15%'
            },
            xAxis: [{
                type: 'category',
                name: '纯电续航里程(公里)',
                data: car_data,
                axisLine: {
                    lineStyle: {
                        color: 'rgba(107,107,107,0.37)', //x轴颜色
                    }
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    interval: 5,
                    textStyle: {
                        color: '#999' //坐标轴字颜色
                    },
                    margin: 15
                },
                axisPointer: {
                    label: {
                        padding: [11, 5, 7],
                        backgroundColor: {
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0,
                                color: '#fff' // 0% 处的颜色
                            }, {
                                offset: 0.9,
                                color: '#fff' // 0% 处的颜色
                            }, {
                                offset: 0.9,
                                color: '#33c0cd' // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: '#33c0cd' // 100% 处的颜色
                            }],
                            global: false // 缺省为 false
                        }
                    }
                },
                boundaryGap: false
            }],
            yAxis: [{
                type: 'value',
                name: '电动汽车价格(万元)',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: 'rgba(107,107,107,0.37)', //y轴颜色
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: '#999'
                    }
                },
                splitLine: {
                    show: false
                }
            }],
            series: [{
                type: 'line',
                data: price_data,
                symbolSize: 1,
                symbol: 'circle',
                smooth: true,
                yAxisIndex: 0,
                showSymbol: false,
                lineStyle: {
                    width: 5,
                    color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                        offset: 0,
                        color: '#9effff'
                    },
                        {
                            offset: 1,
                            color: '#9E87FF'
                        }
                    ]),
                    shadowColor: 'rgba(158,135,255, 0.3)',
                    shadowBlur: 10,
                    shadowOffsetY: 20
                },
                itemStyle: {
                    normal: {
                        color: colorList[0],
                        borderColor: colorList[0]
                    }
                }
            }]
        };
        myChart.setOption(option);
    }
})