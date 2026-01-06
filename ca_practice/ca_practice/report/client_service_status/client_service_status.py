import frappe
from frappe import _

def execute(filters=None):
	columns = [
		{
			"fieldname": "service_type",
			"label": _("Service Type"),
			"fieldtype": "Data",
			"width": 150
		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "start_date",
			"label": _("Start Date"),
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "end_date",
			"label": _("End Date"),
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "billing_type",
			"label": _("Billing Type"),
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname": "responsible_person",
			"label": _("Responsible Person"),
			"fieldtype": "Link",
			"options": "User",
			"width": 150
		},
		{
			"fieldname": "rate",
			"label": _("Rate"),
			"fieldtype": "Currency",
			"width": 100
		}
	]

	data = []
	
	if filters.get("client"):
		data = frappe.db.get_all(
			"CA Client Service",
			filters={"parent": filters.get("client")},
			fields=["service_type", "status", "start_date", "end_date", "billing_type", "responsible_person", "rate"]
		)

	return columns, data
