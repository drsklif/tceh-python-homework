/**
 * Created by ildyakov on 05.11.16.
 */

$(window).on('load', function () {
    $('#id_delivery_date').mask('99.99.9999',{placeholder:'dd.mm.yyyy'});

    $('.js-kladr-inline-input').closest('.row').kladrInline({
        'token': '574fec4e42aa48a2ac22841a3f6def1d',
        'input': '.js-kladr-inline-input',
        'flatRequired': false,
        'geoLocation': true
    });
});
