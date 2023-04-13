$(function () {
    var colorList = ['#73DDFF', '#73ACFF', '#FDD56A', '#FDB36A', '#FD866A', '#9E87FF', '#00FFFF', '#CD5C5C', '#F08080']

    $.ajax({
        type: "POST",
        url: "energy_range_min_price_data",
        contentType: "application/json",
        data: JSON.stringify({}),//参数列表
        dataType: "json",
        success: function (result) {
            data_display_chart(result.legend_data, result.series_data);
        },
        error: function (result) {
        }
    });

    function data_display_chart(legend_data, series_data) {
        var myChart = echarts.init(document.getElementById('div_energy_range_min_price'));
        var color=[
         '#008B8B','#48D1CC','#48D1CC','#20B2AA','#E6E6FA','#0000FF','#0000CD','#191970',
         '#EE82EE','#FF00FF','#98FB98','#8FBC8F','#8B008B','#BA55D3','#90EE90','#32CD32',
         '#FF7F50','#FF6347','#F08080','#FF0000',]
        option = {
            tooltip:{show:true,
            },
            grid:{
                top:'15%',
            },
            xAxis:{},
            yAxis: [{
                max: 100,//设置最大值
                min: 0,//设置最小值
                interval:10,
            }],
            legend:{
                data: legend_data
            },
            series: series_data
        };
        myChart.setOption(option);
    }
})