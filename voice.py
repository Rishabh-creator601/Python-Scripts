import speech_recognition as sr 
import pyttsx3


def take_cmd():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		r.pause_threshold = 1
		audio = r.listen(source)
		print(audio)

		try:
			print('Recognizing...')
			query = r.recognize_google(audio,language='en-in')
			print(f'user said : {query}')
		except:
			print('please say that Again ')
			return 'None'
		return query 

def speak(cmd):
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[0].id)
	engine.say(cmd)
	engine.runAndWait()



if __name__ == '__main__':
	




   query = take_cmd().lower()
   print(query)