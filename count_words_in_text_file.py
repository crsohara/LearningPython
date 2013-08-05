'''
Created on Aug 5, 2013

@author: seriousbuns
'''
import Tkinter, tkFileDialog

def count_words(string):                    #returns word count
    word_array = string.split(" ")
    return len(word_array)

def get_file_address():                     #show file chooser & return file location
    root = Tkinter.Tk()
    root.withdraw()
    return tkFileDialog.askopenfilename()

def read_words_from_file():                 #read words from file & print count
    text_file = open(get_file_address(), 'r')
    words = text_file.read()
    
    word_count = count_words(words)
    print "Wordcount = ", word_count
    
read_words_from_file()