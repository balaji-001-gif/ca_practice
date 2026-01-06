frappe.query_reports["Client Service Status"] = {
    "filters": [
        {
            "fieldname": "client",
            "label": __("Client"),
            "fieldtype": "Link",
            "options": "CA Client",
            "reqd": 1
        }
    ]
};
