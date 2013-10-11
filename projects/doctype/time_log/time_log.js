// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

wn.provide("owrang.projects");

owrang.projects.TimeLog = wn.ui.form.Controller.extend({
	onload: function() {
		this.frm.set_query("task", owrang.queries.task);
	}
});

cur_frm.cscript = new owrang.projects.TimeLog({frm: cur_frm});

cur_frm.add_fetch('task','project','project');