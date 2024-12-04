number=tuple("0123456789")
letter="убери \"%s\", пожалуйста"
gg="Йе, молодец!"
enter="Enter number \"6\":\n"
db=[True,0,0]
def sort(num,l,h):
	for sim in num:
		if not sim in number or len(num)>1:
			unident(num)
			return True,l,h
	if num=="6":
		print(gg)
		return num,l,h
	elif num=="5":
		print("маловато")
		dat=hilo(db[2],db[1])
		l+=1
		return dat,l,h
	elif num=="7":
		print("перебор")
		dat=hilo(db[1],db[2])
		h+=1
		return dat,l,h
	else:
		if int(num)<5 or int(num) in range(8,10):
			print("Вот уж промазал так промазал!")
			return None,l,h

def hilo(x,y):#промах
	if y==2 or x==2 or x>0 and y>0:
		print("Да бля!")
		dumb(input("Are you durachok? (Y/N)\n"))
		return "6"
	elif y>0:
		print("повторяешься!")
	elif x>0:
		print("ну может хватит мазать?")

def unident(st):#больше одной цифры/неизвестный символ
	try:
		int(st)
		for x in st:
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
	except ValueError:
		print("Чую, что-то ты не то ввёл =_=")
		for x in st:
			if not x in number:
				print(letter %x)

def dumb(ans):#тест на глупость
	if ans== "Y" or ans=="y":
		print("Правильный ответ!")
	elif ans=="N" or ans=="n":
		print("Иии... Ты опять ошибся!")
	else:
		print("О хосспаде, можно было и не спрашивать...")
	
while db[0]!="6":
	db=sort(input(enter),db[1],db[2])