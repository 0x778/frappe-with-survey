# Copyright (c) 2023, Greycube and contributors
# For license information, please see license.txt
import json
import frappe
from frappe.model.document import Document

class Survey(Document):
			global my_dict
			my_dict = {
 				"pages": [
  					{
  					  "name" : "Page 1",
 					  "elements": [
 					   ],
 					  "title": "dsaf"
 					 }
 					]
					}
			def before_save(self):
				for i in self.questions:
					my_dict["pages"][0]["elements"].append({
							'type': i.type,
							"name": i.title,
							'title': i.title
								},)
					json_dict = json.dumps(my_dict)
					self.survey_json = json_dict


