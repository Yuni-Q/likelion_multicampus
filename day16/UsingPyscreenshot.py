# pip install pyscreenshot
# https://github.com/ponty/pyscreenshot

import pyscreenshot as ImageGrab

if __name__ == "__main__":
	# im = ImageGrab.grab()
	# im.save('screenshot.jpg')
	# im.show()

	im = ImageGrab.grab(bbox=(10,10,510,510))
	im.show()