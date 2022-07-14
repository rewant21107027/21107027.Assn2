#Q1

from tkinter import *

def gst_formula(original_cost, net_price):
    return ((net_price - original_cost) * 100 / original_cost)


win = Tk()                                                                                              #Creating a GUI window
win.title("GST Tax Finder Calculator")                                                                  #Setting the title
win.geometry("1x1")
win.minsize(height = "400", width = "400")
win.maxsize(height = "1080", width = "1080")
win.configure(bg="Beige")                                                                               #Setting background colour

#Heading
heading = Label(win, text = "GST Tax Finder Calculator", borderwidth = 0, background = "red", font = ("Montserrat ExtraBold",35))
heading.pack(pady = 10,fill = X, ipady = 10)

#Original Cost entry
enter_original_cost = Label(win, text = "Enter the original cost (in ₹)", background = "brown", font = ('lato',13))
enter_original_cost.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.24)                 #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized


original_cost = DoubleVar(win, value = 0)
original_cost_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = original_cost, background = "light blue",fg="black")
original_cost_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.24)

#Net Price entry
enter_net_price = Label(win, text = "Enter the net price (in ₹)", font = ('lato',13), background = "brown")
enter_net_price.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.36)                     #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized

net_price = DoubleVar(win, value = 0)
net_price_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = net_price, background = "light blue",fg="black")
net_price_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.36)

#Calculate GST
def calculate_gst():
    global output
    value_gst = "%0.2f" % (gst_formula(original_cost.get(), net_price.get()))
    output = Label(win, text = value_gst+'%', font = ('lato',13))
    output.pack()
    clear_everything.configure(state = NORMAL)

gst_calculate = Button(win, text = "Calculate GST", font = ('lato',13), highlightbackground= "Beige", command = calculate_gst)
gst_calculate.place(relwidth = 100/400, relheight = 27/400, relx = 0.53, rely = 0.60)

#Clear all
def clear_all():
    original_cost_entry.delete(0,END)
    net_price_entry.delete(0,END)
    output.destroy()
    clear_everything.configure(state = DISABLED)

clear_everything = Button(win, text = "Clear", font = ('lato',13), highlightbackground= "Beige", state = DISABLED, command = clear_all)
clear_everything.place(relwidth = 64/400, relheight = 27/400, relx = 0.3, rely = 0.60)


win.mainloop()

#Q2

from tkinter import *
# importing calendar module
import calendar


# Function for showing the calendar of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set the background colour of GUI window
    new_gui.configure(background="white")

    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")

    # Set the configuration of GUI window
    new_gui.geometry("500x500")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row=5, column=1, padx=20)

    # start the GUI
    new_gui.mainloop()


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="light blue")

    # set the name of tkinter GUI window
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("500x500")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text="CALENDAR", bg="dark red", font=("times", 40, 'bold'), padx=5, pady=5)

    # Create a Enter Year : label
    year = Label(gui, text="ENTER YEAR", bg="light green", font=("times", 28, 'bold'), padx=5, pady=5)

    # Create a text entry box for filling or typing the information.
    year_field = Entry(gui)

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text="Show Calendar", fg="Black", bg="Red", command=showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row=1, column=1, padx=140, pady=10)

    year.grid(row=2, column=1, padx=140, pady=0)

    year_field.grid(row=3, column=1, pady=5)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    # start the GUI
    gui.mainloop()

#Q3

from tkinter import *
root = Tk()
root.title("Calculator")
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50,fg = "black", bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(root, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()

#Q4

lst_in = eval(input("Enter the list: "))

#Using quick sort algorithm
def quick_sort(list):
    if len(list) <= 1:                                                                                  #Base case
        return list
    else:
        left_arr = [x for x in list if x < list[0]]
        pivot = [x for x in list if x == list[0]]
        right_arr = [x for x in list if x > list[0]]
        return quick_sort(left_arr) + pivot + quick_sort(right_arr)                                     #Recursive call by taking pivot as the first element of the unsorted list
def merge_sort(list):
    pass

lst_out = quick_sort(lst_in)
print("The sorted list(using quick sort algorithm) is: ", lst_out)
lst_out2 = merge_sort(lst_in)
print("The sorted list(using merge sort algorithm) is: ", lst_out)

#Q5

print("ANSWER 5")
n = int(input())
li = list(map(int, input().strip().split()))
# Part 1
li.sort()
print("Sorted array is:", li)

# Part 2
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input())
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# Part 3
if(ind == -1):
    print("No element\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)

#Q6

# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [4, 5, 2, 4, 5, 6, 4, 5, 5, 6]
print(Remove(duplicate))
