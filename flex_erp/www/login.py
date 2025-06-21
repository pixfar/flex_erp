import frappe
from frappe import _
from frappe.auth import LoginManager

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = False
    context.title = _("Login")

    if frappe.session.user != "Guest":
        # Already logged in, redirect
        frappe.local.flags.redirect_location = "/app"
        raise frappe.Redirect

    context.redirect_after_login = False  # default

    if frappe.request.method == "POST":
        usr = frappe.form_dict.get("usr")
        pwd = frappe.form_dict.get("pwd")

        try:
            # Authenticate user
            login_manager = LoginManager()
            login_manager.authenticate(usr, pwd)
            login_manager.post_login()

            # Set context flag for client-side redirect
            context.redirect_after_login = True

        except frappe.AuthenticationError:
            context.message = _("Invalid login credentials")

    return context
