import tkinter as tk
import tkinter.filedialog
from test import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.input_file_name = None

    def create_widgets(self):
        # create a Frame for the Text and Scrollbar
        txt_frm = tk.Frame(self, width=800, height=600)
        txt_frm.pack(side='bottom', fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        # create a Frame for buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side='top')

        # create buttons
        browse_file_button = tk.Button(buttons_frame, text='Browse...',
        command=self.getFileName)
        browse_file_button.pack(side='left')

        run_button = tk.Button(buttons_frame, text='Run', command=self.executeTest)
        run_button.pack(side='left')

        quit_button = tk.Button(buttons_frame, text="QUIT", fg="red",
        command=root.destroy)
        quit_button.pack(side='left')


        self.output_text_widget = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        self.output_text_widget.config(undo=True, wrap='word')
        self.output_text_widget.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = tk.Scrollbar(txt_frm, command=self.output_text_widget.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.output_text_widget['yscrollcommand'] = scrollb.set

        self.printTextToTextWidger("Please select a file and press Run button to begin experiment.\n")

    def getFileName(self):
        self.input_file_name = tk.filedialog.askopenfilename(
        initialdir="/home/Documents/pattern-recognition/",
        filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
        title = "Choose a file.",
        )
        self.printTextToTextWidger("Input file: " + self.input_file_name + '\n')

    def destroyWidgets(self, widget_list):
        print('Destroying widgets...')
        for widget in widget_list:
            widget.destroy()

    def executeTest(self):
        p = Perceptron([1,1,1,1])
        # print ("Testing perceptron with weight vector: "+str(p.getWeightVector()))
        # print ("Result for input vector (255,100,30,1): "+str(p.fire([255,100,30,1])))
        # print ("Result for input vector (200,110,50,1): "+str(p.fire([200,110,50,1])))
        # print ("Result for input vector (30,100,200,1): "+str(p.fire([30,100,200,1])))
        # print ("Result for input vector (120,235,12,1): "+str(p.fire([120,235,12,1])))
        # print ("Result for input vector (40,100,30,1): "+str(p.fire([40,100,30,1])))
        # print ("Result for input vector (155,55,100,1): "+str(p.fire([155,55,100,1])))
        # print ("Result for input vector (255,200,55,1): "+str(p.fire([255,200,55,1])))

        if(self.input_file_name != None):
            data = readFile(self.input_file_name)

            # for debugging
            # print data
            t = Trainers(data,0.7)
            #raw_input("Continue?")

            self.printTextToTextWidger('Begining Perceptron training...\n')

            t.gradientDescent(p)

            self.printTextToTextWidger(
            "Perceptron's weight vector after training:\n" + \
            str(p.getWeightVector()) + '\n'
            )

            self.printTextToTextWidger("New file for testing is required!\n")
            self.getFileName()

            data = readFile(self.input_file_name)

            self.input_file_name = None

            self.printTextToTextWidger(tester(p,data))
        else:
            self.printTextToTextWidger("Error: No input file is given!!\n")

    def printTextToTextWidger(self, text_to_be_printed):
        self.output_text_widget['state'] = tk.NORMAL
        self.output_text_widget.insert(tk.END, text_to_be_printed)
        self.output_text_widget['state'] = tk.DISABLED
        self.output_text_widget.update()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
