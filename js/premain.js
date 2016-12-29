	// randomize owl carrocel
	//Sort random function
	function random(owlSelector) {
		owlSelector.children().sort(function () {
			return Math.round(Math.random()) - 0.5;
		}).each(function () {
			$(this).appendTo(owlSelector);
		});
	}