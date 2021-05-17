// Copyright (c) 2021, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('API Test', {
	get_erpnext_doc: function(frm) {
		let doc_resource='/api/resource/Insurance Policy Template/'
		let doc_name='?filters=[["Insurance Policy Template","name","=","'+frm.doc.insurance_policy_template_id+'"]]'
		let doc_fields='&fields=["name","account_number","policy_data"]'
		let api_url=frm.doc.url+doc_resource+doc_name+doc_fields
		window.open(api_url);
	}
});
