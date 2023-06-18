	/*  Wizard */
	jQuery(function ($) {
		);
		//  progress bar
		$("#progressbar").progressbar();
		$("#wizard_container").wizard({
			afterSelect: function (event, state) {
				$("#progressbar").progressbar("value", state.percentComplete);
				$("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
			}
		});
		// Validate select
		$('#wrapped').validate({
			ignore: [],
			rules: {
				select: {
					required: true
				}
			},
			errorPlacement: function (error, element) {
				if (element.is('select:hidden')) {
					error.insertAfter(element.next('.nice-select'));
				} else {
					error.insertAfter(element);
				}
			}
		});
	});

	// Summary
	function getVals(formControl, controlType) {
		switch (controlType) {

			case 'first_name':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#first_name").text(value);
				break;

			case 'last_name':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#last_name").text(value);
				break;

			case 'email':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#email").text(value);
				break;

			case 'testing':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#testing").text(value);
				break;

			 case 'country':
				// Get the value for a select
				var value = $(formControl).val();
				$("#country").text(value);
				break;

			case 'user_name':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#user_name").text(value);
				break;
			case 'send_time':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#send_time").text(value);
				break;

			case 'password':
				// Get the value for a input text
				var value = $(formControl).val();
				$("#password").text(value);
				break;
		}
	}