import re,string 



__all__ = ["TextUtil"]





class TextUtil:
	def __init__(
		self,text,
		lower=False,upper=False,
		trim=False,remove_puncs=False,
		remove_numbers=False,
		space_by_one=False):


		""" 
		lower          :   Lower The values 
		upper          :   Uppers the values 
		trim           :   Remove Whitespaces
		remove_puncs   :   Removes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
		remove_numbers :   Removes 0123456789
		space_by_ones  :   add one space in non -linear text 

		Example {space_by_one}: 
		from : Hello world   Text
		to : Hello world Text 





		"""
		self.text = text

		self.text = self.text.lower() if lower ==True else self.text
		self.text = self.text.upper() if upper ==True else self.text
		


		if trim == True:
			self.rstrip()


		if remove_puncs == True:
			self.filter()

		if remove_numbers == True:
			self.remove_numbers()


		if space_by_one ==True:
			self.add_one_space()
		



	def remove(self,values=[]):

		""" 
		Remove Custom Values 

		Example:
		remove(["#","*"])
		"""


		self.text  = re.sub(f"""[{"".join(values)}]""","",self.text)

	def filter(self):

		""" Remove string.punctuation """


		to_remove = string.punctuation

		for i in to_remove:
			if i in self.text:
				self.text = self.text.replace(i,"")



	def remove_numbers(self):
		digits = string.digits

		for i in digits:
			if i in self.text:
				self.text = self.text.replace(i,"")


	def rstrip(self):

		self.text = self.text.split(" ")
		self.text = "".join(self.text)


	def add_one_space(self,token="<>"):
		
		for i in self.text:
			if i == " ":
				self.text = self.text.replace(i,token)

		self.text = self.text.split(token)
		self.text  = [i for i in self.text if i != '']
		self.text =  " ".join(self.text)




	def __repr__(self):
		return self.text












