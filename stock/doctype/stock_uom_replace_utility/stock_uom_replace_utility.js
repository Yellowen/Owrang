// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

$.extend(cur_frm.cscript, {
	onload: function() {
		cur_frm.set_query("item_code", owrang.queries.item);
	},
	
	item_code: function() {
		if(cur_frm.doc.item_code) {
			return cur_frm.call({
				method: "get_stock_uom",
				args: { item_code: cur_frm.doc.item_code }
			});
		}
	}
});