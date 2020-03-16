frappe.ui.form.on("Sales Invoice", {
	refresh: frm => {
		events = ["set_queries", "generar_ncf"]
		$.map(events, event => {
			frm.trigger("set_queries");
		})
	},
	set_queries: frm => {
		frm.set_query("invoice_type", event => {
			return {
				filters:{
					"transaction_type": "Sale"
				}
			}
		})
	},
	generar_ncf: frm => {
		frm.toggle_enable("ncf", !frm.doc.generar_ncf);
	},
	ncf: frm => {
		if (frm.doc.ncf.length != 11){
			frappe.msgprint("El Numero de comprobante no tiene la cantidad de caracteres requeridos!");
			frm.set_value("ncf", "");
		}

	},
	invoice_type: frm => {
		if (frm.doc.invoice_type != "Jornadas")
			frm.set_value("institution", "");
	},
	institution: frm => {
		const {institution, items} = frm.doc;
		
		description = institution ? "Jornada " + institution : "";

		$.map(items, item => {
			frappe.model.set_value(
				item.doctype,
				item.name,
				"description",
				description
			);
		})
	}
})

frappe.ui.form.on("Sales Invoice Item", {
	item_code: (frm, cdt, cdn) => {
		setTimeout(event => {
			frm.trigger("institution");
		},500);
	}
})