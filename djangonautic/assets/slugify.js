const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = function(val) {
	//trim() trims any white space
	return val.toString().toLowerCase().trim()
	.replace(/&/g,'-and-')	//replace & with -and
	.replace(/[\s\W-]+/g,'-')	//replace spaces,non word chars and dashes with a single dash
};

titleInput.addEventListener('keyup',function(event) {
	slugInput.setAttribute('value',slugify(titleInput.value));
});