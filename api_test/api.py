
import json
import frappe
from frappe import _
import requests
from frappe.utils import parse_json,get_link_to_form
import xmltodict


@frappe.whitelist()
def get_policy_data_from_itcrateengine():
    try:
        is_valid = False
        url='https://ratingqa.itcdataservices.com/Webservices/ITCRateEngineAPI/api/objectsamples/ITCRateEngineRequest?type=xml&useacord=true'
        r= requests.get(url)
        is_valid = True if r.status_code == 200 else False
        if is_valid==True:
            json_request=parse_json(json.dumps(xmltodict.parse(r.text)))
            ITCRateEngineRequest=json_request.get('ITCRateEngineRequest')
            account_number=ITCRateEngineRequest.get('AccountNumber')
            policy_data=ITCRateEngineRequest.get('PolicyData')
            insurance_policy_template=create_insurance_policy_template(account_number,policy_data)
            form_link = get_link_to_form('Insurance Policy Template', insurance_policy_template)
            frappe.msgprint(msg=_('{0}').format(form_link), title=_("Insurance Policy Template is created."))
        else:
            raise Exception

    except Exception as e:
        frappe.throw(_(str(e)), title=_("Something went wrong..."))

def create_insurance_policy_template(account_number,policy_data):
    try:
        insurance_policy_template = frappe.get_doc({
            "doctype": "Insurance Policy Template",
            "account_number": account_number,
            "policy_data": policy_data
        })
        insurance_policy_template.insert()
        return insurance_policy_template.name
    except Exception:
        frappe.throw(frappe.get_traceback())

