# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


__version__ = "1.x.x"


def notify(**kwargs):
    import frappe

    frappe.publish_realtime(
        event="insights_notification",
        user=frappe.session.user,
        message={
            "message": kwargs.get("message"),
            "title": kwargs.get("title"),
            "type": kwargs.get("type", "success"),
            "user": frappe.session.user,
        },
    )
