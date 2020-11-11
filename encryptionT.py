from tkinter import *
import cryptifier
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

'''This program requires the matplotlib and numpy modules to be installed.'''

class encryptionGui:
    def __init__(self, master):
        # configuration
        master.configure(bg='peach puff')
        master.title('Cryptography Cave')
        master.option_add('*Font', 'Georgia 12')  # font for all widgets
        master.option_add('*Background', 'honeydew3')  # background of all
        master.option_add('*Label.Font', 'helvetica 14')  # font for all
        master.geometry('800x500+980+180')  # w,h,x,y (top left corner)
        #
        master.iconbitmap(r'padlock.ico')
        #
        # frame1 - header area
        #
        frame1 = Frame(master, bg='gray15')
        frame1.pack(fill='both', expand=True)  # fills window
        #
        # frame2 - user input area
        #
        frame2 = Frame(master)
        #
        frame2.pack(fill='both', expand=True)
        #
        # frame 2a (subframe for frame 2)
        #
        frame2a = Frame(frame2, relief=GROOVE, borderwidth=1, bg='honeydew3')
        frame2a.pack(side=LEFT, fill=Y)  # fill Y makes frames same height
        #
        label_2a_heading = Label(frame2a)
        label_2a_heading.config(borderwidth=0, text='Choose a Cipher:', bg='honeydew3')
        label_2a_heading.pack(padx=10, pady=10)
        #
        self.radio_2a_choice = StringVar(master)  # variable to store radio button choice
        self.radio_2a_choice.set('Caesar')  # sets to default value
        radio_2a_1 = Radiobutton(frame2a, text='Caesar', variable=self.radio_2a_choice, value='Caesar', bg='honeydew3')
        radio_2a_2 = Radiobutton(frame2a, text='Vernam', variable=self.radio_2a_choice, value='Vernam', bg='honeydew3')
        radio_2a_1.pack(anchor=W, padx=10, pady=10)
        radio_2a_2.pack(anchor=W, padx=10, pady=10)
        #
        # frame 2b 
        #
        frame2b = Frame(frame2, relief=GROOVE, borderwidth=1, bg='honeydew3')
        frame2b.pack(side=LEFT, fill=Y)
        #
        label_2b_heading = Label(frame2b)
        label_2b_heading.config(borderwidth=0, text='Shift Number:', bg='honeydew3')
        label_2b_heading.pack(padx=10, pady=10)
        #
        self.length_spin = Spinbox(frame2b, width=6, from_=-26, to=26, bg='gray95')
        self.length_spin.pack(anchor=W, padx=10, pady=10)

        #
        # frame 2c 
        #
        frame2c = Frame(frame2, relief=GROOVE, borderwidth=1, bg='honeydew3')
        frame2c.pack(side=LEFT, fill=Y)
        #
        label_2c_heading = Label(frame2c)
        label_2c_heading.config(borderwidth=0, text='Choose:', bg='honeydew3')
        label_2c_heading.pack(anchor=W, padx=10, pady=10, side=TOP)
        #
        self.radio_2c_choice = StringVar(master)  # variable to store radio button choice
        self.radio_2c_choice.set('Encrypt')  # sets to default value
        radio_2c_1 = Radiobutton(frame2c, text='Encrypt', variable=self.radio_2c_choice, value='Encrypt',
                                 bg='honeydew3')
        radio_2c_2 = Radiobutton(frame2c, text='Decrypt', variable=self.radio_2c_choice, value='Decrypt',
                                 bg='honeydew3')
        radio_2c_1.pack(anchor=W, padx=10, pady=10)
        radio_2c_2.pack(anchor=W, padx=10, pady=10)
        #
        btn_generate = Button(frame2)
        btn_generate.config(relief=RAISED, borderwidth=5, text='Cryptify!', command=self.criptify)
        btn_generate.pack(padx=10, pady=10, side=BOTTOM)
        #
        label_heading_input = Label(frame2)
        label_heading_input.config(text='Input:')
        label_heading_input.pack(side=LEFT, padx=10, pady=10, anchor=NW)
        #
        self.entry_input_var = StringVar(master)
        self.entry_input_var.set('')
        entry_input = Entry(frame2)
        entry_input.config(bd=1, relief=GROOVE, bg='gray93', textvariable=self.entry_input_var)
        entry_input.pack(side=LEFT, anchor=W, padx=10, pady=10)
        #
        icon = PhotoImage(file="cryptocave.gif")
        lbl_icon = Label(frame1)
        lbl_icon.config(image=icon)
        lbl_icon.image = icon
        lbl_icon.pack(side=LEFT, padx=10, pady=10)
        lbl_icon.config(bg='gray15')  # override default font
        lbl_icon.pack(side=LEFT, padx=10, pady=10)
        #
        btn_frequencyAnalysis = Button(frame1)
        btn_frequencyAnalysis.config(text='Frequency Analysis', font='helvetica 16 bold', activebackground='sea green',
                                     bg='gold2', command=self.freqAnalysis)
        btn_frequencyAnalysis.pack(side=RIGHT, padx=10, pady=10)
        #
        # frame3-output area
        #
        frame3 = Frame(master)
        frame3.pack(fill='both', expand=True)
        #
        label_3a = Label(frame3)
        label_3a.config(borderwidth=0, text='Here is your output: ', bg='honeydew3')
        label_3a.pack(side=LEFT)
        #
        self.output_var = StringVar(master)
        self.output_var.set('')  # default to empty string
        entry_output = Entry(frame3)
        entry_output.config(borderwidth=1, relief=GROOVE, bg='light gray', textvariable=self.output_var)
        entry_output.pack(side=LEFT)
        #
        btn_quit = Button(frame3)
        btn_quit.config(relief=RAISED, borderwidth=5, text='   Quit   ', command=master.destroy)
        btn_quit.pack(padx=10, pady=10, side=BOTTOM, anchor=SE)
        #
        label_symmetrical_heading = Button(frame3)
        label_symmetrical_heading.config(relief=RAISED, borderwidth=5, bg='honeydew3',
                                         text='The Two Sides of Encryption', command=self.typesOf_Encryption)
        label_symmetrical_heading.pack(padx=10, pady=10, side=BOTTOM, anchor=SE)

    def criptify(self):
        # get values from interface
        shiftNumber = self.length_spin.get()
        cipherChoice = self.radio_2a_choice.get()
        encrypt_or_decrypt = self.radio_2c_choice.get()
        inputEntry = self.entry_input_var.get()
        #
        cryptifier.cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry)
        output = cryptifier.cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry)
        self.output_var.set(output)

    def typesOf_Encryption(self):
        encryptionTypes = Toplevel()
        encryptionTypes.title('The Two Sides of Encryption')
        encryptionTypes.geometry('800x500+980+180')
        encryptionTypes.option_add('*Font', 'Georgia 12')
        encryptionTypes.option_add('*Background', 'gray15')
        encryptionTypes.option_add('*Label.Font', 'helvetica 14')
        encryptionTypes.config(bg='gray15')
        #
        # Frame1 - Header for Symmetrical + Definition + Examples
        #
        frame1 = Frame(encryptionTypes, bg='gray30')
        frame1.pack(fill=Y, expand=True, side=LEFT)
        #
        header_Symmetrical = Label(frame1)
        header_Symmetrical.config(borderwidth=0, text='Symmetrical', bg='gray30', fg='ghost white')
        header_Symmetrical.pack(anchor=N, side=TOP, padx=10, pady=10)
        #
        symmetricalDefinition = Label(frame1)
        symmetricalDefinition.config(borderwidth=0, wraplength=300, justify=LEFT,
                                     text='When we use a single key to encrypt/decrypt plaintext.', bg='gray30',
                                     fg='ghost white')
        symmetricalDefinition.pack(anchor=N, side=TOP, padx=10, pady=10)
        #
        symmetricalExamples = Label(frame1)
        symmetricalExamples.config(borderwidth=0, wraplength=160, justify=LEFT,
                                   text='Examples:                -Caesar Cipher;                -Vernam Cipher',
                                   bg='gray30', fg='ghost white')
        symmetricalExamples.pack(anchor=N, side=LEFT, padx=10, pady=10)
        #
        # Frame2 - Header for Asymmetrical + Definition + Examples
        #
        frame2 = Frame(encryptionTypes, bg='gray30')
        frame2.pack(fill=Y, expand=True, side=RIGHT)
        #
        header_Asymmetrical = Label(frame2)
        header_Asymmetrical.config(borderwidth=0, text='Asymmetrical', bg='gray30', fg='ghost white')
        header_Asymmetrical.pack(anchor=N, side=TOP, padx=10, pady=10)
        #
        asymmetricalDefinition = Label(frame2)
        asymmetricalDefinition.config(borderwidth=0, wraplength=300, justify=LEFT, fg='ghost white', bg='gray30',
                                      text="When keys come in pairs, a Public Key and a Private Key. Users can send secret messages by encrypting a message with the recipient's public key. Only the intended recipient can decrypt the message, since only that user should have access to the required key.")
        asymmetricalDefinition.pack(anchor=N, side=TOP, padx=10, pady=10)
        #
        asymmetricalExamples = Label(frame2)
        asymmetricalExamples.config(borderwidth=0, wraplength=160, justify=LEFT,
                                    text='Examples:                -RSA Encryption (This relies on the fact that it is very hard to factorise large composite numbers with few prime numbers)',
                                    bg='gray30', fg='ghost white')
        asymmetricalExamples.pack(anchor=N, side=LEFT, padx=10, pady=10)

        btn_close = Button(encryptionTypes, bg='honeydew3', relief=RAISED, borderwidth=5, text='   Close   ',
                           command=encryptionTypes.destroy)
        btn_close.pack(padx=10, pady=10, side=BOTTOM)

    def freqAnalysis(self):

        # fetches data from GUI
        shiftNumber = self.length_spin.get()
        cipherChoice = self.radio_2a_choice.get()
        encrypt_or_decrypt = self.radio_2c_choice.get()
        inputEntry = self.entry_input_var.get()

        # fetches output data from cryptifier
        cryptifier.cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry)
        data = cryptifier.cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry)

        # Creates the bar chart visually on the GUI
        characters = list(data)

        while data == '':  # If the user enters nothing, this will run. it is a validation check
            try:
                plt.clf()
                labels, values = zip(*Counter(characters).items())
                indexes = np.arange(len(labels))
                width = 0.5

                plt.bar(indexes, values, width)
                plt.xticks(indexes + width * 0, labels)
                plt.title('Most frequent characters outputted')
                plt.ylabel('Number of uses')
                plt.xlabel('Characters')
                plt.figure('Frequency Analysis')
                plt.show()
            except ValueError:
                from tkinter import messagebox
                messagebox.showerror('Error', 'Please enter an input')
                break
        else:  # create the graph if all else is good.
            plt.figure('Frequency Analysis')
            plt.clf()
            labels, values = zip(*Counter(characters).items())
            indexes = np.arange(len(labels))
            width = 0.5

            plt.bar(indexes, values, width)
            plt.xticks(indexes + width * 0, labels)
            plt.yticks()
            plt.title('Most frequent characters outputted')
            plt.ylabel('Number of uses')
            plt.xlabel('Characters')
            plt.show()


def main():
    root = Tk()  # creates a tkinter root window
    app = encryptionGui(root)  # puts GUI onto the root
    root.mainloop()  # runs the event handler


if __name__ == "__main__":
    main()
