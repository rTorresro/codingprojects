from tkinter import*


class Calculator:

        def __init__(calc,root):
                
            calc.root = root
            calc.root .title("Calculator")
            calc.root.geometry("615x680+400+100")
            calc.root.configure(bg = 'purple')

            calc.MainFrame = Frame(calc.root , bd = 23, width = 600, height=670, relief=RIDGE, bg = 'blue')
            calc.MainFrame.grid()
            calc.WidgetFrame = Frame(calc.MainFrame , bd = 23, width = 590, height=660, relief=RIDGE, bg = 'purple')
            calc.WidgetFrame.grid()

            calc.lblDisplay = Label(calc.WidgetFrame, width = 30, height=2, bg='white', font = ('arial',20,'bold'), anchor='e')
            calc.lblDisplay.grid (row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

            calc.input_button = ""
            
            calc.create_button ("<-", 1, 0)
            calc.create_button ("AC" , 1, 1)
            calc.create_button ("C" , 1, 2)
            calc.create_button ("+/-", 1, 3)

            calc.create_button ("7", 2, 0)
            calc.create_button ("8" , 2, 1)
            calc.create_button ("9" , 2, 2)
            calc.create_button ("+", 2, 3)

            calc.create_button ("4", 3, 0)
            calc.create_button ("5" , 3, 1)
            calc.create_button ("6" , 3, 2)
            calc.create_button ("-", 3, 3)

            calc.create_button ("1", 4, 0)
            calc.create_button ("2" , 4, 1)
            calc.create_button ("3" , 4, 2)
            calc.create_button ("*", 4, 3)

            calc.create_button ("0", 5, 0)
            calc.create_button ("." , 5, 1)
            calc.create_button ("=" , 5, 2)
            calc.create_button ("/", 5, 3)
        
        def create_button(calc, text, row, column):
            btnWidget = Button(calc.WidgetFrame, text=text, width = 5, height=2, bd=4,  bg='purple', font = ('arial',20,'bold'), command =lambda: calc.button_click(text))
            btnWidget.grid(row = row, column = column, padx=5, pady = 5)
        
        def button_click(calc, text):
             
            if text == '<-':
                 calc.input_button = calc.input_button[:-1]
            elif text == 'AC':
                 calc.input_button = ""
            elif text == 'C':
                 calc.input_button = ""

            elif text == "=":
                try:
                      calc.input_button = str(eval(calc.input_button))
                except: 
                     calc.input_button = 'Error'
            elif text == "+/-":
                 calc.input_button = str(float(calc.input_button))
            else:
                 calc.input_button += text
            calc.lblDisplay.config(text = calc.input_button)

                
                  
root = Tk()
App = Calculator(root)
root.mainloop()
