# version = 0.1
# developer: Felhazi Lorand
# app for auto key pressing, support for a max of 5 keys
import tkinter
import pyautogui
#initialize 
app = tkinter.Tk()
# user interface
app.title('KP')
app.minsize(width=520, height=250)
app.maxsize(width=520, height=250)

default_delay = 1000  # 1 sec

#Functions
def onClickStart():
    if btnStart['state'] == tkinter.NORMAL:
        btnStop['state'] = tkinter.NORMAL
        btnStart['state'] = tkinter.DISABLED       
def onClickStop():
    if btnStop['state'] == tkinter.NORMAL:
        btnStart['state'] = tkinter.NORMAL
        btnStop['state'] = tkinter.DISABLED
        
def createFrame(nr=1, param = tkinter.NORMAL):
    Frame = tkinter.Frame(app)
    Frame.pack(side='right',  fill='both',  padx=5,  pady=5)

    funcHeader = tkinter.Label(Frame,
                        text=nr,
                        width=3,
                        bd=3,
                        font=('Arial', 18),
                        state = param)
    funcKey = tkinter.Entry(Frame,
                            width=3,
                            bd=3,
                            font=('Arial', 18),
                            state = param)
    funcDelay = tkinter.Entry(Frame,                
                              width=3,
                              bd=3,
                              font=('Arial', 18),
                              state = param)
    funcHeader.pack(padx=10,  pady=5)
    funcKey.pack(padx=10,  pady=5)
    funcDelay.pack(padx=10,  pady=5)
    
    ##########funcKey.config(text = entry.get())

# Main app GUI
#mainFrame components
mainFrame = tkinter.Frame(app)
mainFrame.pack(side='left',  fill='both',  padx=10,  pady=5) 

emptySpace = tkinter.Label(mainFrame,
                    text='',
                    font=('Arial', 18))
key = tkinter.Label(mainFrame,
                    text='Key',
                    font=('Arial', 18))
delay = tkinter.Label(mainFrame,
                    text='Delay(s)',
                    font=('Arial', 18))
btnStart = tkinter.Button(mainFrame,
                    text='Start',
                    font=('Arial', 18),
                    state=tkinter.NORMAL,
                    command=onClickStart)
btnStop = tkinter.Button(mainFrame,
                    text='Stop',
                    font=('Arial', 18),
                    state=tkinter.DISABLED,
                    command=onClickStop)
emptySpace.pack(padx=5,  pady=5)
key.pack(padx=5,  pady=5)
delay.pack(padx=5,  pady=5)
btnStart.pack(padx=5,  pady=5)
btnStop.pack(padx=5,  pady=5)

#Frame components
i = 0
while i < 5:
    createFrame(5-i,tkinter.NORMAL)
    i+=1

app.mainloop()
