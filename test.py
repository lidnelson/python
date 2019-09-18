import shutil

from shutil import copyfileobj
status = False
if isinstance(target, string_types):
	target = open("users.txt","wb")
	status = True
try:
	copyfileobj(self.stream, target, buffer_size)
finally:
	if status:
		target.close()
