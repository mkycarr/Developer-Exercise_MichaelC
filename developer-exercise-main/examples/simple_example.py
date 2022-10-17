
# Please create a simple example use of the pynn library for your end user. Assume that the end
# user knows a lot about their subject matter but has only a basic understanding of Python.

# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.

#function that writes to pointfile.txt
from asyncore import write
from cgi import print_arguments
import sys


def show_menu():
    valid_input= False
    print("***********POINTS MENU**************\n")
    while not valid_input:
        answer= input("Would you like to see the points created?(Yes/No)")
        answer= answer.lower()

        if answer== ("yes"):
            print_file()
            valid_input= True
            continue
        if answer== ('no'):
            print("Thanks for using the program.Goodbye.")
            valid_input= True
            continue
        else:
            print("Please make a valid selection")

def write_file(content):
    f = open("examples/pointfile.csv", "a")
    f.write(str(content)+'\n')
    f.close()

def print_file():
    print("****QueryPoint and Nearest Neighbor*********")
    f = open("examples/pointfile.csv", "r")
    for x in f:
        print(x)

    f.close()






