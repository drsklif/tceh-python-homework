/**
 * Created by ildyakov on 05.11.16.
 */

/**
	Работает на DaData
	https://confluence.hflabs.ru/pages/viewpage.action?pageId=426639416
*/

(function ($) {

	$.fn.kladrInline = function (options) {

		var settings = $.extend({
			'serviceUrl': 'https://api.bcs.ru/kladr/v3',
			'type': 'ADDRESS',
			'token': '',
			'input': '',
			'flatRequired': false, // flat validation
			'geoLocation': true // true/false/{kladr_id: '63000001'}
		}, options);

		return this.each(function () {

			var $input = $(settings.input, this),
				$inputHidden = $input.next('input'),
				$inputError = $input.parent().find('.js-kladr-inline-error'),
				$region_name = $input.parent().find('.js-kladr-inline-regname'),
				$region_code = $input.parent().find('.js-kladr-inline-regcode');

			var showError = function (msg, color) {
				if (msg === '') {
					$inputError.html('');
					return;
				} else {
					$inputError.html('<span class="_' + color + '">' + msg + '</span>');
				}
			};

			$input.suggestions({
				serviceUrl: settings.serviceUrl,
				token: settings.token,
				type: settings.type,
				autoSelectFirst: true,
				hint: false,
				mobileWidth: 420,
				geoLocation: settings.geoLocation,
				onSelect: function (suggestion) {
					var data = suggestion.data;
					$region_name.val(data.region);
					$region_code.val(data.region_kladr_id);
					//console.log(suggestion);

					if (!data.city && !data.settlement) {
						showError('Введите название населенного пункта', 'red');
						$inputHidden.val('').change();
					} else if (data.city && !data.street) {
						showError('Необходимо указать улицу', 'red');
						$inputHidden.val('').change();
					} else if (data.city && data.street && !data.house) {
						showError('Нужно указать номер дома', 'red');
						$inputHidden.val('').change();
					} else if (data.city && data.street && data.house && !data.flat) {
						if (settings.flatRequired) {
							showError('Укажите номер квартиры', 'red');
							$inputHidden.val('').change();
						} else {
							showError('Укажите номер квартиры, если есть', 'gray');
							$inputHidden.val(suggestion.value).change();
							$inputError.next().html('');
						}
					} else {
						showError('');
						$inputHidden.val(suggestion.value).change();
						$inputError.next().html('');
					}

				},
				onSelectNothing: function () {
					showError('');
					$inputHidden.val('').change();
				}
			});

		});

	};

}(jQuery));
