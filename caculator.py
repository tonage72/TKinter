from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")

# Global variables
f_num = 0

# Function for number buttons
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

# Function for clear button
def button_clear():
	global f_num
	f_num = 0
	e.delete(0, END)

# Function for add button
def button_add():
	global f_num
	entered_number = e.get()
	e.delete(0, END)
	f_num = f_num + int(entered_number)

# Function for equal button
def button_equal():
	global f_num
	entered_number = e.get()
	e.delete(0, END)
	e.insert(0, f_num + int(entered_number))
	f_num = 0

# Function for divide button
def button_divide():
	return

# Function for multiply button
def button_multiply():
	return

# Function for subtract button
def button_subtract():
	return

# Create and place entry widget on the screen
e = Entry(root,
	width=20,
	relief="flat",
	highlightbackground="black",
	highlightthickness=1,)
e.grid(row=0,
	column=0,
	columnspan=5,
	padx=10,
	pady=10)

# Create button - All buttons have this style
def create_button(text, command):
	return Button(
		root,
		text=text,
		width=9,
		height=4,
		fg="white",
		relief="solid",
		bg="darkgray",
		bd=1,
		command=command
		)

# Define number buttons
button = {}
for i in range(10):
	button[i] = create_button(str(i), lambda x=i: button_click(x))

# Put number buttons on the screen
button_positions = {
	0:(4,0),1:(3,0),2:(3,1),3:(3,2),4:(2,0),5:(2,1),6:(2,2),7:(1,0),8:(1,1),9:(1,2)
}
for num, pos in button_positions.items():
	button[num].grid(row=pos[0], column=pos[1])

# Define operation buttons and place them on the screen
button_divide = create_button("/", button_divide)
button_divide.grid(row=1, column=3)
button_multiply = create_button("*", button_multiply)
button_multiply.grid(row=2, column=3)
button_subtract = create_button("-", button_subtract)
button_subtract.grid(row=3, column=3)
button_add = create_button("+", button_add)
button_add.grid(row=4, column=3)
button_equal = create_button("=", button_equal)
button_equal.grid(row=4, column=2)
button_clear = create_button("C", button_clear)
button_clear.grid(row=4, column=1)


root.mainloop()