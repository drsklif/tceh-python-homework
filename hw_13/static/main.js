$(document).on('ready', function () {

    var post_id = 0;

    $('.button-comment').magnificPopup({
		type: 'inline',
		preloader: false,
		focus: '#text',

		// When elemened is focused, some mobile browsers in some cases zoom in
		// It looks not nice, so we disable it:
		callbacks: {
			beforeOpen: function() {
				if($(window).width() < 700) {
					this.st.focus = false;
				} else {
					this.st.focus = '#text';
				}

				post_id = $(this.st.el[0]).closest('.post').data('post_id');
			}
		}
	});

    $('#comment_form').on('submit', function (event) {
        event.preventDefault();
        var form = $(this);
		$('input[name=post_id]', form).val(post_id);

        $.post(form.attr('action'), form.serialize())
            .done(function(data) {
                $.magnificPopup.close();
				var comment = $('<div class="comment"><p class="comment-text">' + data.text + '</p><p class="comment-author">' + data.author + '</p></div>');
				$('#post_' + post_id + ' .post-comments').append(comment);
            })
			.fail(function () {
				alert('Error while saving comment! Please, try later');
			});
    });

});