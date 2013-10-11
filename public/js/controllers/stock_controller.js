// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

wn.provide("owrang.stock");

owrang.stock.StockController = wn.ui.form.Controller.extend({
	show_stock_ledger: function() {
		var me = this;
		if(this.frm.doc.docstatus===1) {
			this.frm.add_custom_button("Stock Ledger", function() {
				wn.route_options = {
					voucher_no: me.frm.doc.name,
					from_date: me.frm.doc.posting_date,
					to_date: me.frm.doc.posting_date
				};
				wn.set_route('stock-ledger');
			}, "icon-bar-chart");
		}
		
	},
	show_general_ledger: function() {
		var me = this;
		if(this.frm.doc.docstatus===1 && cint(wn.defaults.get_default("auto_accounting_for_stock"))) { 
			cur_frm.add_custom_button('Accounting Ledger', function() {
				wn.route_options = {
					"voucher_no": me.frm.doc.name,
					"from_date": me.frm.doc.posting_date,
					"to_date": me.frm.doc.posting_date,
				};
				wn.set_route("general-ledger");
			});
		}
	}
});