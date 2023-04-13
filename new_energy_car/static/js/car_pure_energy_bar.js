$(function () {
    var colorList = ['#73DDFF', '#73ACFF', '#FDD56A', '#FDB36A', '#FD866A', '#9E87FF', '#00FFFF', '#CD5C5C', '#F08080']

    $.ajax({
        type: "POST",
        url: "car_pure_energy_bar_data",
        contentType: "application/json",
        data: JSON.stringify({}),//参数列表
        dataType: "json",
        success: function (result) {
            draw_car_pure_energy_bar(result.legend_data, result.series_data);
        },
        error: function (result) {
        }
    });

    function draw_car_pure_energy_bar(x1, y1) {
        // 基于准备好的dom，初始化echarts实例
        //内置主题样式：默认，‘light’，‘dark’
        var myChart = echarts.init(document.getElementById('div_car_pure_energy_bar'),'light');

        itemStyle={
            normal: {
                color: '#ff8635',
                // 阴影的大小
                shadowBlur: 10,
                // 阴影水平方向上的偏移
                shadowOffsetX: 5,
                // 阴影垂直方向上的偏移
                shadowOffsetY: 5,
                // 阴影颜色
                shadowColor: 'rgba(0, 0, 0, 0.7)'
            },
            //鼠标 hover 的时候
            emphasis: {
                shadowBlur: 10,
                color:'#ff5d4d',
                shadowColor: 'rgba(0, 200, 20, 0.7)',
                label:{
                    show:true,
                }
            }
        }

        // 指定图表的配置项和数据
        var option = {
            tooltip: {},
            toolbox:{
                show:true,
                feature:{
                    dataView: {readOnly: false},
                    magicType: {type: ['line', 'bar']},
                    restore: {},
                    //图片下载名称
                    saveAsImage: {name:'车型数量'},
                }
            },
            legend: {
                data:['车型数量']
            },
            xAxis: {
                axisLabel:{
                    color:'#ff8015',
                    fontFamily:'微软雅黑',
                    //fontWeight:'bold',
                    fontSize:15,
                    rotate:0
                },
                data: x1
            },
            yAxis: {},
            series: [{
                name: '车型数量',
                type: 'bar',
                itemStyle:itemStyle,
                data: y1
            }]
        };

        console.log(echarts.version);
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
}

 })