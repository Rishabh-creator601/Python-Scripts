import codecs ,hashlib 
from encodings_name import encodings_hashlib,encodings_codecs









class Coder:
	def __init__(self,text,encoding=None,dig="hexdigest"):

		self.ans = ''

		if encoding in encodings_codecs:
			self.ans  =  self.encode_codecs(text=text,encoding=encoding)

		if encoding in encodings_hashlib.keys():
			self.ans  =  self.encode_hashlib(text=text,encoding=encoding,dig=dig)

		if  not encoding in list(encodings_hashlib.keys()) + encodings_codecs:
			self.ans = "Coding Not Found In The List"


		


	def encode_codecs(self,text,encoding):
		return codecs.encode(encoding=encoding,obj=text)


	def encode_hashlib(self,encoding,text,dig='hexdigest'):

		converted  = None
		if encoding in encodings_hashlib.keys():
			m = encodings_hashlib[encoding]()
			m.update(text.encode())
			if dig == 'hexdigest':
				converted = m.hexdigest()
			if dig == 'digest':
				converted = m.digest()

			return converted
		else:
			return "Encoding Not Found"





class DCoder:
	def __init__(self,text):
		self.ans  = ''

		self.ans  =self.decode_codecs(text=text)

		if self.ans  == '':
			self.ans  = "Cannot Be Coded"




	def decode_codecs(self,text):
		ans  = ""
		for i in encodings_codecs: 
			try:
				ans = codecs.decode(obj=text,encoding=i)
				break
				
			except:
				pass 


		return ans 


	def decode_hashlib():
		pass




