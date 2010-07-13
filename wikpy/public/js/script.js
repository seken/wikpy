function replaceText(field, from, to) {
	if (field.value == from) {
		field.value = to;
	}
}

function initSearchbox() {
	var searchbox = document.getElementById("search");

	searchbox.onfocus = function(event) {
		replaceText(searchbox, "Search", "");
	}
	searchbox.onblur = function (event) {
		replaceText(searchbox, "", "Search");
	}
}

window.onload = function(event) {
	initSearchbox();
}
