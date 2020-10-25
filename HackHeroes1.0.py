from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Productivity Hacker")
ico = Image.open('logoHH2.png')
photo = ImageTk.PhotoImage(ico)
root.iconphoto(False, photo)
root.geometry("1280x720")
background = ImageTk.PhotoImage(Image.open("bg222.png"))
background_label = Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)

canvtodo = ImageTk.PhotoImage(Image.open("canvtodo.png"))
todoCanvas = Canvas(root, width=243, height=322, highlightthickness=0, borderwidth=0)
todoCanvas.place(x=56, y=357)
todoCanvas.create_image(1, 1, image=canvtodo, anchor=NW)
canvhabit = ImageTk.PhotoImage(Image.open("canvhabit.png"))
habitCanvas = Canvas(root, width=243, height=322, highlightthickness=0, borderwidth=0)
habitCanvas.place(x=328, y=357)
habitCanvas.create_image(1, 1, image=canvhabit, anchor=NW)
canvtimer = ImageTk.PhotoImage(Image.open("canvtimer.png"))
timerCanvas = Canvas(root, width=243, height=322, highlightthickness=0, borderwidth=0)
timerCanvas.place(x=601, y=357)
timerCanvas.create_image(1, 1, image=canvtimer, anchor=NW)

timerTime = ImageTk.PhotoImage(Image.open("timerTimeL.png"))
timerName = ImageTk.PhotoImage(Image.open("timerNameL.png"))
timerT = ImageTk.PhotoImage(Image.open("timerTB.png"))
timerE = ImageTk.PhotoImage(Image.open("timerEB.png"))
timerD = ImageTk.PhotoImage(Image.open("timerDB.png"))
timerStop = ImageTk.PhotoImage(Image.open("timerStopB.png"))
timerStart = ImageTk.PhotoImage(Image.open("timerStartB.png"))


taskL = ImageTk.PhotoImage(Image.open("taskL.png"))
taskB = ImageTk.PhotoImage(Image.open("taskB.png"))
trashBI = ImageTk.PhotoImage(Image.open("trashB.png"))
editBI = ImageTk.PhotoImage(Image.open("editB.png"))
deadlineBI = ImageTk.PhotoImage(Image.open("deadlineB.png"))
taskBBlack = ImageTk.PhotoImage(Image.open("buttonCheckBlack.png"))
taskBGray = ImageTk.PhotoImage(Image.open("buttonCheckGray.png"))


# Level
size = 0.43
oneLevel = Image.open("lvl1.png").resize((round(90*size), round(237*size)), Image.ANTIALIAS)
oneLevel = ImageTk.PhotoImage(oneLevel)
threeLevel = Image.open("lvl3.png").resize((round(90*size), round(237*size)), Image.ANTIALIAS)
threeLevel = ImageTk.PhotoImage(threeLevel)
sixLevel = Image.open("lvl6.png").resize((round(90*size), round(237*size)), Image.ANTIALIAS)
sixLevel = ImageTk.PhotoImage(sixLevel)
nineLevel = Image.open("lvl9.png").resize((round(90*size), round(237*size)), Image.ANTIALIAS)
nineLevel = ImageTk.PhotoImage(nineLevel)

xp = 0
w = 1


def levelF():
	global w
	global xpToNext
	global level
	global levelLabel
	global xpLabel
	if xp < 20:
		level = 1
		xpToNext = 20
	elif 60 > xp >= 20:
		level = 2
		xpToNext = 60
	elif 100 > xp >= 60:
		level = 3
		xpToNext = 100
	elif 150 > xp >= 100:
		level = 4
		xpToNext = 150
	elif 210 > xp >= 150:
		level = 5
		xpToNext = 210
	elif 280 > xp >= 210:
		level = 6
		xpToNext = 280
	elif 360 > xp >= 280:
		level = 7
		xpToNext = 360
	elif 410 > xp >= 360:
		level = 8
		xpToNext = 410
	elif 500 > xp >= 410:
		level = 9
		xpToNext = 500
	elif xp >= 500:
		level = 10
		w = 2
		xpToNext = 999999999999999999

	# 1-2 levels character
	if level in [1, 2]:
		oneLvl = Label(root, image=oneLevel, borderwidth=0)
		oneLvl.place(x=50, y=6)
	# 3 - 5 levels character
	if level in [3, 4, 5]:
		threeLvl = Label(root, image=threeLevel, borderwidth=0)
		threeLvl.place(x=50, y=6)
	# 6 - 8 levels character
	if level in [6, 7, 8]:
		sixLvl = Label(root, image=sixLevel, borderwidth=0)
		sixLvl.place(x=50, y=6)
	# 9 - 10 levels character
	if level > 8:
		nineLvl = Label(root, image=nineLevel, borderwidth=0)
		nineLvl.place(x=50, y=6)

	# # # # # # # # # # # # # #
	levelLabel = Label(root, text=level, font=("Calibri Bold", 40//w), borderwidth=0, bg="#fff5e6", height=0, width=w)
	levelLabel.place(x=21, y=96, anchor=CENTER)
	xpLabel = Label(root, text=(xp, "/", xpToNext, "xp"), font=("Calibri Bold", 20), bg="#387cbc", borderwidth=0)
	xpLabel.place(x=139, y=49)


levelF()

# To Do
todoTasks = 1
todobuttonsq = 1
labels_ids = []
buttons_ids = []
trash_ids = []
edit_ids = []
time_ids = []


def todoAddNew():
	global todobuttonsq
	global todoTasks
	if todobuttonsq <= 4:

		def check():
			global todobuttonsq
			global xp
			global todoTasks
			todoB.config(state=DISABLED)
			trashB.config(state=DISABLED)
			editB.config(state=DISABLED)
			deadlineB.config(state=DISABLED)
			todoL.config(state=DISABLED)
			todoB.config(image=taskBGray)
			todoB.unbind("<Enter>")
			todoB.unbind("<Leave>")
			todoB.destroy()
			todoL.destroy()
			trashB.destroy()
			editB.destroy()
			deadlineB.destroy()
			todobuttonsq -= 1
			levelLabel.destroy()
			xpLabel.destroy()
			xp += 15
			levelF()
			xpEff = Text(root, bg="#387cbc", width=6, height=0)
			xpEff.insert(INSERT, "+15 xp")
			xpEff.place(x=240, y=90)
			root.after(1000, xpEff.destroy)

		def delete():
			global todobuttonsq
			global todoTasks
			todoB.destroy()
			todoL.destroy()
			trashB.destroy()
			editB.destroy()
			deadlineB.destroy()
			todobuttonsq -= 1
			'''labels_ids[1].destroy()
			buttons_ids[1].destroy()
			trash_ids[1].destroy()
			edit_ids[1].destroy()
			time_ids[1].destroy()'''

		def edit():
			todoB.config(state=DISABLED)
			trashB.config(state=DISABLED)
			editB.config(state=DISABLED)
			deadlineB.config(state=DISABLED)

			def saveEdit():
				todoB.config(state=ACTIVE)
				trashB.config(state=ACTIVE)
				editB.config(state=ACTIVE)
				deadlineB.config(state=ACTIVE)
				todoL.config(text=editE.get())
				saveEditB.destroy()
				editE.delete(0, END)
				editE.destroy()

			editE = Entry(root, borderwidth=1)
			editE.place(x=56, y=326, width=212, height=29)
			editE.insert(0, todoL.cget("text"))
			saveEditB = Button(root, text="zapisz", borderwidth=0, command=saveEdit)
			saveEditB.place(x=269, y=327, width=30, height=28)

		def deadline():
			return

		todoL = Label(todoCanvas, text=todo_new_E.get(), image=taskL, compound=CENTER, borderwidth=0)
		todoL.grid(row=todoTasks, column=0, padx=(6, 0), pady=(4, 0))
		# todoL.place(x=62, y=todoTasks)
		todoB = Button(todoCanvas, image=taskB, borderwidth=0, command=check)
		todoB.grid(row=todoTasks, column=1, pady=(4, 0))
		# todoB.place(x=238, y=todoTasks-1)
		trashB = Button(todoCanvas, image=trashBI, borderwidth=0, command=delete)
		trashB.grid(row=todoTasks, column=2, sticky=NE, pady=(4, 0))
		# trashB.place(x=272, y=todoTasks-1)
		editB = Button(todoCanvas, image=editBI, borderwidth=0, command=edit)
		editB.grid(row=todoTasks, column=2, sticky=E, pady=(4, 0))
		# editB.place(x=272, y=todoTasks-1+18)
		deadlineB = Button(todoCanvas, image=deadlineBI, borderwidth=0, command=deadline)
		deadlineB.grid(row=todoTasks, column=2, sticky=SE, pady=(4, 0))
		# deadlineB.place(x=272, y=todoTasks-1+17+18)
		todoTasks += 1
		todobuttonsq += 1
		# deleting button - required
		labels_ids.append(todoL)
		buttons_ids.append(todoB)
		trash_ids.append(trashB)
		edit_ids.append(editB)
		time_ids.append(deadlineB)

		def enterTodo(event):
			todoB.config(image=taskBBlack)

		def leaveTodo(event):
			todoB.config(image=taskB)

		todoB.bind("<Enter>", enterTodo)
		todoB.bind("<Leave>", leaveTodo)
		todo_new_E.delete(0, END)
	else:
		errorPage = Label(root, text="Program jest w wersji alpha - ilość Zadań jest jeszcze ograniczona :(",
		                  fg="#ffffff", bg="red")
		errorPage.place(x=640, y=690)
		root.after(3000, errorPage.destroy)


todo_new_E = Entry(root, borderwidth=1)
todo_new_E.insert(0, " Dodaj Nowe Zadanie")
todo_new_E.place(x=56, y=326, width=212, height=29)
todo_new_B = Button(root, text="+", bg="#ffffff", borderwidth=0, command=todoAddNew, state=DISABLED)
todo_new_B.place(x=269, y=327, width=30, height=28)


def restrictLen(event):
	txt = todo_new_E.get()
	if len(txt) >= 25:
		todo_new_E.delete(25)


def clickDel(event):
	global todo_new_B
	todo_new_E.delete(0, 'end')
	todo_new_B.config(state=ACTIVE)
	todo_new_B.place(x=269, y=327, width=30, height=28)


def clickIns(event):
	global todo_new_B
	todo_new_E.delete(0, 'end')
	todo_new_E.insert(0, " Dodaj Nowe Zadanie")
	todo_new_B.config(state=DISABLED)
	todo_new_B.place(x=269, y=327, width=30, height=28)


todo_new_E.bind("<Key>", restrictLen)
todo_new_E.bind("<FocusIn>", clickDel)
todo_new_E.bind("<FocusOut>", clickIns)


# Habit
habitTasks = 1
habitbuttonsq = 1


def habitAddNew():
	global habitTasks
	global habitbuttonsq
	if habitbuttonsq <= 4:

		def check():
			global xp
			global habitbuttonsq
			global habitTasks
			habitB.config(state=DISABLED)
			# trashB.config(state=DISABLED)
			editB.config(state=DISABLED)
			deadlineB.config(state=DISABLED)
			habitL.config(state=DISABLED)
			habitB.config(image=taskBGray)
			habitB.unbind("<Enter>")
			habitB.unbind("<Leave>")

			levelLabel.destroy()
			xpLabel.destroy()
			xp += 5
			levelF()
			xpEff = Text(root, bg="#387cbc", width=5, height=0)
			xpEff.insert(INSERT, "+5 xp")
			xpEff.place(x=240, y=90)
			root.after(1000, xpEff.destroy)

		def delete():
			global habitbuttonsq
			global habitTasks
			habitB.destroy()
			habitL.destroy()
			trashB.destroy()
			editB.destroy()
			deadlineB.destroy()
			habitbuttonsq -= 1

		def edit():
			habitB.config(state=DISABLED)
			trashB.config(state=DISABLED)
			editB.config(state=DISABLED)
			deadlineB.config(state=DISABLED)

			def saveEdit():
				habitB.config(state=ACTIVE)
				trashB.config(state=ACTIVE)
				editB.config(state=ACTIVE)
				deadlineB.config(state=ACTIVE)

				habitL.config(text=editE.get())
				saveEditB.destroy()
				editE.delete(0, END)
				editE.destroy()

			editE = Entry(root, borderwidth=1)
			editE.place(x=56 + 272, y=326, width=212, height=29)
			editE.insert(0, habitL.cget("text"))
			saveEditB = Button(root, text="zapisz", borderwidth=0, command=saveEdit)
			saveEditB.place(x=269 + 272, y=327, width=30, height=28)

		def deadline():
			return

		habitL = Label(habitCanvas, text=habit_new_E.get(), image=taskL, compound="center", borderwidth=0)
		habitL.grid(row=habitTasks, column=0, padx=(6, 0), pady=(4, 0))
		# habitL.place(x=62 + 272, y=habitTasks)
		habitB = Button(habitCanvas, image=taskB, borderwidth=0, command=check)
		habitB.grid(row=habitTasks, column=1, pady=(4, 0))
		# habitB.place(x=238 + 272, y=habitTasks-1)
		trashB = Button(habitCanvas, image=trashBI, borderwidth=0, command=delete)
		trashB.grid(row=habitTasks, column=2, sticky=NE, pady=(4, 0))
		# trashB.place(x=272 + 272, y=habitTasks-1)
		editB = Button(habitCanvas, image=editBI, borderwidth=0, command=edit)
		editB.grid(row=habitTasks, column=2, sticky=E, pady=(4, 0))
		# editB.place(x=272 + 272, y=habitTasks-1+18)
		deadlineB = Button(habitCanvas, image=deadlineBI, borderwidth=0, command=deadline)
		deadlineB.grid(row=habitTasks, column=2, sticky=SE, pady=(4, 0))
		# deadlineB.place(x=272 + 272, y=habitTasks-1+17+18)
		habitTasks += 1
		habitbuttonsq += 1

		def enterHabit(event):
			habitB.config(image=taskBBlack)

		def leaveHabit(event):
			habitB.config(image=taskB)

		habitB.bind("<Enter>", enterHabit)
		habitB.bind("<Leave>", leaveHabit)
		habit_new_E.delete(0, END)
	else:
		errorPage = Label(root, text="Program jest w wersji alpha - ilość Nawyków jest jeszcze ograniczona :(",
		                  fg="#ffffff", bg="red")
		errorPage.place(x=640, y=690)
		root.after(3000, errorPage.destroy)


habit_new_E = Entry(root, borderwidth=1)
habit_new_E.insert(0, " Dodaj Nowy Nawyk")
habit_new_E.place(x=56 + 272, y=326, width=212, height=29)
habit_new_B = Button(root, text="+", bg="#ffffff", borderwidth=0, command=habitAddNew, state=DISABLED)
habit_new_B.place(x=269 + 272, y=327, width=30, height=28)


def clickDel(event):
	global habit_new_B
	habit_new_E.delete(0, 'end')
	habit_new_B.config(state=ACTIVE)


def clickIns(event):
	global habit_new_B
	habit_new_E.delete(0, 'end')
	habit_new_E.insert(0, " Dodaj Nowy Nawyk")
	habit_new_B.config(state=DISABLED)


habit_new_E.bind("<FocusIn>", clickDel)
habit_new_E.bind("<FocusOut>", clickIns)


# Timer


def timerAddNew():

	def start():
		global count
		count = 0
		start_timer()

	def start_timer():
		global count
		timer()

	def stop():
		global count
		count = 1

	def timer():
		global count
		if count == 0:
			d = str(t.get())
			h, m, s = map(int, d.split(":"))

			h = int(h)
			m = int(m)
			s = int(s)
			if s < 59:
				s += 1
			elif s == 59:
				s = 0
				if m < 59:
					m += 1
				elif m == 59:
					h += 1
			if h < 10:
				h = str(0) + str(h)
			else:
				h = str(h)
			if m < 10:
				m = str(0) + str(m)
			else:
				m = str(m)
			if s < 10:
				s = str(0) + str(s)
			else:
				s = str(s)
			d = h + ":" + m + ":" + s

			t.set(d)
			if count == 0:
				root.after(930, start_timer)

	t = StringVar()
	t.set("00:00:00")

	timerNameL = Label(timerCanvas, text=timer_new_E.get(), image=timerName, compound=CENTER, borderwidth=0)
	timerNameL.grid(row=0, column=1, sticky=N, pady=(6, 0))
	timerTimeL = Label(timerCanvas, textvariable=t, image=timerTime, compound=CENTER, borderwidth=0)
	timerTimeL.grid(row=0, column=1, sticky=NW, pady=(31, 0), rowspan=3)
	timerStartB = Button(timerCanvas, image=timerStart, borderwidth=0, command=start)
	timerStartB.grid(row=0, column=0, padx=(5, 0), pady=(5, 0))
	timerStopB = Button(timerCanvas, image=timerStop, borderwidth=0, command=stop)
	timerStopB.grid(row=1, column=0, padx=(5, 0), sticky=NW)
	timerTB = Button(timerCanvas, image=timerT, borderwidth=0)
	timerTB.grid(row=0, column=2, sticky=N, pady=(5, 0), padx=1, rowspan=2)
	timerEB = Button(timerCanvas, image=timerE, borderwidth=0)
	timerEB.grid(row=0, column=2, sticky=E, pady=(6, 0), padx=1, rowspan=2)
	timerDB = Button(timerCanvas, image=timerD, borderwidth=0)
	timerDB.grid(row=0, column=2, sticky=E, pady=(51, 0), padx=1, rowspan=2)


timer_new_E = Entry(root, borderwidth=1)
timer_new_E.insert(0, " Dodaj Nowy Timer")
timer_new_E.place(x=56 + 544, y=326, width=212, height=29)
timer_new_B = Button(root, text="+", bg="#ffffff", borderwidth=0, command=timerAddNew, state=DISABLED)
timer_new_B.place(x=269 + 544, y=327, width=30, height=28)


def clickDel(event):
	global timer_new_B
	timer_new_E.delete(0, 'end')
	timer_new_B.config(state=ACTIVE)


def clickIns(event):
	global timer_new_B
	timer_new_E.delete(0, 'end')
	timer_new_E.insert(0, " Dodaj Nowy Timer")
	timer_new_B.config(state=DISABLED)


timer_new_E.bind("<FocusIn>", clickDel)
timer_new_E.bind("<FocusOut>", clickIns)

mainloop()
