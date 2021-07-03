from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import pyautogui

class YT_Killer:
	def __init__(self):
		pass
	def getActiveWindow(self):
		return GetWindowText(GetForegroundWindow())
	def main(self):
		while True:
			window = self.getActiveWindow()
			if "Google Chrome" in window:
				if 'YouTube' in window:
					pyautogui.hotkey('ctrl', 'w')
			time.sleep(5)


if __name__ == '__main__':
	main = YT_Killer()
	main.main()