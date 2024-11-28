string=tuple("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzАаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя.,")
number=tuple("0123456789")
letter="убери \"%s\", пожалуйста"
dafuck='"%s"? Зачем это здесь? А главное- НАХУЯ?!'
gg="Йе, молодец!"
enter="Enter number \"6\":\n"
data=None
l=0
h=0
def sort(num):
	if str(num)=="6":
		print(gg)
		return "end",
	elif str(num)=="5":
		return "low",
	elif str(num)=="7":
		return "high",
	for sim in str(num):
		if not sim in number:
			return "letter", num
	else:
		if int(num)<5 or int(num) in range(8,10):
			return "mistake",
		elif int(num)>9:
			return "letter", num

def hilo(x,y):
	if y==2 or x==2 or x>0 and y>0:
		print("Да бля!")
		return "end",
	elif y>0:
		print("повторяешься!")
	elif x>0:
		print("ну может хватит мазать?")

def unident(st):
	for x in st:
		if not x in string:
			if x in number:
				if not x in "6":
					print("хотя бы циферка есть")
					if st.count(x)>1:
						print("но многовато")
						break
				elif x in "6":
					print("неплохо!")
					if st.count(x)>1:
						print("хоть и многовато")
						break
	for x in st:
		if not x in number:
			if x in string:
				for y in st:
					if y in number:
						print("НО")
						break
				print(letter %x)
			else:
				for y in st:
					if y in number:
						print("НО")
						break
				print(dafuck %x)

while data!=("end",):
	data=sort(input(enter))
	if data[0]=="low":
		print("маловато")
		data=hilo(h,l)
		l+=1
	elif data[0]=="high":
		print("перебор")
		data=hilo(l,h)
		h+=1
	elif data[0]=="letter":
		data=unident(data[1])
	elif data[0]=="mistake":
		print("Вот уж промазал так промазал!")