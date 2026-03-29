from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort 

--------------add complexity ------------------------
algo_complexity = {
    "Bubble Sort": "Time: O(n²) | Space: O(1)",
    "Merge Sort": "Time: O(n log n) | Space: O(n)",
    "Quick Sort": "Time: O(n log n) | Space: O(log n)"
}
complexity_label = Label(
    root,
    text="Time Complexity: ",
    font=("arial", 12, "bold"),
    bg="#082A46",
    fg="white"
)
complexity_label.place(x=300, y=100)
def update_complexity(event=None):
    selected = algo_menu.get()
    complexity_label.config(text=algo_complexity.get(selected, ""))

algo_menu.bind("<<ComboboxSelected>>", update_complexity)
update_complexity()

------------------------end add complexity------------------------------------

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='#082A46')
data = []

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rest = 10
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rest
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray [i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "italic bold"),
                           fill="orange")

    root.update_idletasks()

def StartAlgorithm():
    global data
    if not data :
        return
    
    if (algo_menu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data) - 1 , drawData, speedscale.get())
        
    elif algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData,speedscale.get())
        
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData,speedscale.get())
    drawData(data, ['green' for x in range(len(data))])
    

def Generate():
    global data
    print('Selected Algorithm:' + selected_algorithm.get())
    minivalue = int(Minvalue.get())
    maxivalue = int(Maxvalue.get())
    sizevalue = int(Sizevalue.get())

    data = []
    for _ in range(sizevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))

    drawData(data,['red' for x in range(len(data))])

selected_algorithm = StringVar()
mainlabel = Label(root, text="Algorithm:", font=("new roman", 16, "italic bold"), bg="#05897A",
                   width=10, fg="black", relief=GROOVE, bd=5)
mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 19, "italic bold"), textvariable=selected_algorithm,
                         values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0)

random_generate = Button(root, text="Generate", bg="#2DAE9A", font=("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground='#05945B', activeforeground="white", bd=5, width=10, command=Generate)
random_generate.place(x=750, y=60)

Sizevaluelabel = Label(root, text="Size:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                   width=10, fg="black", height=2, relief=GROOVE, bd=5)
Sizevaluelabel.place(x=0, y=60)

Sizevalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
Sizevalue.place(x=120, y=60)

Minvaluelabel = Label(root, text="Min Value:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                   width=10, fg="black", height=2, relief=GROOVE, bd=5)
Minvaluelabel.place(x=250, y=60)

Minvalue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
Minvalue.place(x=370, y=60)

Maxvaluelabel = Label(root, text="Max Value:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                   width=10, fg="black", height=2, relief=GROOVE, bd=5)
Maxvaluelabel.place(x=500, y=60)

Maxvalue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
Maxvalue.place(x=620, y=60)

start = Button(root, text="Start", bg="#C45809", font=("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground='#05945B', activeforeground="white", bd=5, width=10, command=StartAlgorithm)
start.place(x=750, y=0)

speedlabel = Label(root, text="Speed:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                   width=10, fg="black", relief=GROOVE, bd=5)
speedlabel.place(x=400, y=0)

speedscale = Scale(root, from_=0.2, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
speedscale.place(x=520, y=0)

canvas = Canvas(root, width=870, height=450, bg='black')
canvas.place(x=10, y=130)

root.mainloop()
