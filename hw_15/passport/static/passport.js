/**
 * Created by ildyakov on 05.11.16.
 */

$(window).on('load', function () {
    $('#id_series').mask('99 99');
    $('#id_number').mask('999999');
    //$('#id_issue_date').mask('9999-99-99',{placeholder:'yyyy-mm-dd'});
    $('#id_issue_date').mask('99.99.9999',{placeholder:'dd.mm.yyyy'});
    $('#id_subdivision_code').mask('999-999',{placeholder:'___-___'});
});
