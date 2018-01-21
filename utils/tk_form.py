from tkinter import *


def make_form():

    master = Tk()

    master.title('SolidWorks Extension')

    Label(master, text="Last Name").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Label(master, text="First Name").grid(row=0)
    Button(master, text='Quit', command=master.quit) \
        .grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show',
           command=lambda: print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))) \
        .grid(row=3, column=1, sticky=W, pady=4)


if __name__ == '__main__':
    make_form()
    mainloop()
