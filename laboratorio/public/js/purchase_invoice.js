frappe.ui.form.on("Purchase Invoice", {
	refresh: frm => {
		frm.trigger("set_queries");
	},
	set_queries: frm => {
		frm.set_query("invoice_type", event => {
			return {
				filters: {
					"transaction_type": "Purchase"
				}
			}
		});
	}
})