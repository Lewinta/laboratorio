# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "laboratorio"
app_title = "Laboratorio"
app_publisher = "Lewin Villar"
app_description = "A Clinic Laboratory App"
app_icon = "fa fa-flask"
app_color = "#7578f6"
app_email = "lewin.villar@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/laboratorio/css/laboratorio.css"
# app_include_js = "/assets/laboratorio/js/laboratorio.js"

# include js, css files in header of web template
# web_include_css = "/assets/laboratorio/css/laboratorio.css"
# web_include_js = "/assets/laboratorio/js/laboratorio.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "laboratorio.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "laboratorio.install.before_install"
# after_install = "laboratorio.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "laboratorio.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"laboratorio.tasks.all"
# 	],
# 	"daily": [
# 		"laboratorio.tasks.daily"
# 	],
# 	"hourly": [
# 		"laboratorio.tasks.hourly"
# 	],
# 	"weekly": [
# 		"laboratorio.tasks.weekly"
# 	]
# 	"monthly": [
# 		"laboratorio.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "laboratorio.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "laboratorio.event.get_events"
# }

