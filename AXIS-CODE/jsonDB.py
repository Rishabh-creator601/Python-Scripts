import json ,os 




class JsonDB:

	def __init__(self,filename=None):

		if filename is None:
			self.file = "words.json"
		else:
			self.file = filename

		if not os.path.exists(self.file):
			self.create()


	def create(self,data={}):

		with open(self.file,"w") as f:
			json.dump(data,f)
		f.close()

	def read(self):
		with open(self.file,'r') as f:
			data = json.load(f)

		return data


	def add(self,data={}):

		old_data = self.read()
		for k , v in data.items():
			old_data[k] = v 


		self.create(old_data)


	def delete(self,title=''):

		if title == (None or ''):
			return "Please Insert a Title "
		else:

			data =self.read()

			data = dict(data)

			if title in data.keys():
				data.__delitem__(title)

		self.create(data)


