import webbrowser ,os 


def open_(url,index=0):

	""" 0 : new window | 1 : new tab"""
	chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
	browser  = webbrowser.get('chrome')

	if index == 0:
		os.system("chrome --new-window {}".format(url))

	if index == 1:
		browser.open_new_tab(url)


