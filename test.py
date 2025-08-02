import tkinter
import sv_ttk
#
def change_run():
    button.config(text='run', command= change_stop)

def change_stop():
    button.config(text='stop', command= change_run)



#

main = tkinter.Tk()
main.geometry("400x400")
main.title('Voice to keyboard')
sv_ttk.set_theme("dark")

empty1= tkinter.Label(main, text='')
empty1.pack()
text = tkinter.ttk.Label(main, text='Not currently listening')
text.pack()
empty2= tkinter.Label(main, text='')
empty2.pack()

empty3= tkinter.Label(main, text='')
empty3.pack()
message = tkinter.ttk.Label(main, text='[message recorded]')
message.pack()
empty4= tkinter.Label(main, text='')
empty4.pack()
#
button = tkinter.ttk.Button(main, text='run', command= change_stop) 
button.pack() 
#
button1 = tkinter.ttk.Button(main, text='Stop', width=25, command=main.destroy)
button1.pack()

t = tkinter.Text(main, height=10, width=40)
t.pack()

main.mainloop()




