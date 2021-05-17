# -*- coding: utf-8 -*-
# Copyright (c) 2021, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from api_test.api import get_policy_data_from_itcrateengine

class APITest(Document):
	@frappe.whitelist()
	def fetch_itcrateengine(self):
		get_policy_data_from_itcrateengine()
