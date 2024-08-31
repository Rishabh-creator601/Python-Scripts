import json,os 


class SnipPath:
	def __init__(self):
		self.manage_snippy_path()


	def manage_snippy_path(self):

		if not os.path.exists("C:/Users/PC/Snippy/snippy_path.json"):


			os.mkdir("C:/Users/PC/Snippy")



		with open("C:/Users/PC/Snippy/snippy_path.json","w") as f:
			json.dump({"Path":"C:/Users/PC/Snippy/snippets.json"},f)
		f.close()


	def get_snippy_path(self):

		with open("C:/Users/PC/Snippy/snippy_path.json","r") as f:
			data = json.load(f)

		return data['Path']

