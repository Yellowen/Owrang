// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

wn.provide('owrang');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	wn.app.name = "Owrang";

	var brand = ($("<div></div>").append(wn.boot.website_settings.brand_html).text() || 'owrang');
	$('.navbar-brand').html('<div style="display: inline-block;">\
			<object type="image/svg+xml" data="app/images/splash.svg" class="toolbar-splash"></object>\
		</div>' + brand)
	.attr("title", brand)
	.addClass("navbar-icon-home")
	.css({
		"max-width": "200px",
		"overflow": "hidden",
		"text-overflow": "ellipsis",
		"white-space": "nowrap"
	});
});

wn.provide('wn.ui.misc');
wn.ui.misc.about = function() {
	if(!wn.ui.misc.about_dialog) {
		var d = new wn.ui.Dialog({title:'About Owrang'})

		$(d.body).html(repl("<div>\
		<p>Owrang is an open-source web based ERP made by Yellowen Inc and is a fork\
                of Web Notes Technologies Pvt Ltd ERPNext.\
		to provide an integrated tool to manage most processes in a small organization.\
		For more information about Web Notes, or to buy hosting servies, go to \
		<a href='https://owrang.yellowen.com'>https://owrang.yellowen.com</a>.</p>\
		<p>To report an issue, go to <a href='https://github.com/Yellowen/Owrang/issues'>GitHub Issues</a></p>\
		<hr>\
		<p><a href='http://www.gnu.org/copyleft/gpl.html'>License: GNU General Public License Version 3</a></p>\
		</div>", wn.app));

		wn.ui.misc.about_dialog = d;
	}

	wn.ui.misc.about_dialog.show();
}
