/**
 * Created by ildyakov on 05.11.16.
 */

$(window).on('load', function () {
    //$('#id_date_to').mask('99.99.9999',{placeholder:'dd.mm.yyyy'});
    $('#datetimepicker1').datetimepicker({
        format: 'DD.MM.YYYY',
        locale: 'ru'
    });
    /*$('#id_date_to').datepicker({
        language: 'ru'
    });*/

    $('#graph').highcharts('StockChart', {
            rangeSelector: {
                selected: 1
            },
            title: {
                text: 'USD to RUB exchange'
            },
            series: [{
                name: 'USD to RUB',
                data: quotes,
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });

});
