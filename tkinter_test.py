import tkinter as tk # Python 3 import
# import Tkinter as tk # Python 2 import


root = tk.Tk()

def my_function():
    current_id = my_entry.get()
    url_member = "https://api.example.com/member?member_id="+str(current_id)
    print(url_member)
    #do stuff with url_member

my_label = tk.Label(root, text = "Meber ID# ")
my_label.grid(row = 0, column = 0)
my_entry = tk.Entry(root)
#my_entry.grid(row = 0, column = 1)

for i in range(9):
	for j in range(9):
		my_entry.grid(row = i, column = j)

my_button = tk.Button(root, text = "Submit", command = my_function)
my_button.grid(row = 1, column = 1)

root.mainloop()