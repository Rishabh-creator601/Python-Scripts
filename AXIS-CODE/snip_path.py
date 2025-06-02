import json,os 


SNIP_PATH =  "C:/depository/Snippy/"
SNIPPY_JSON_PATH ="C:/depository/Snippy/snippy_path.json"
SNIPPETS_JSON_PATH = "C:/depository/Snippy/snippets.json"


class SnipPath:
	def __init__(self):
		self.manage_snippy_path()


	def manage_snippy_path(self):

		if not os.path.exists(SNIP_PATH):
			os.mkdir(SNIP_PATH)



		with open(SNIPPY_JSON_PATH,"w") as f:
			json.dump({"Path":SNIPPETS_JSON_PATH},f)
		f.close()


	def get_snippy_path(self):

		with open(SNIPPY_JSON_PATH,"r") as f:
			data = json.load(f)

		return data['Path']




