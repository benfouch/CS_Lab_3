"""
- NOTE: REPLACE 'N' Below with your section, year, and lab number
- CS2911 - 0NN
- Fall 202N
- Lab N
- Names:
  - 
  - 

"The Machine" implementation of parsing and executing a program.

The application reads a file name from the user and executes the contents of the file or sends an error if the file format is not valid.

The file format is describe in "The Machine" exercise and the lab description.


Introduction: (Describe the lab in your own words)




Summary: (Summarize your experience with the lab, what you learned, what you liked, what you disliked, and any suggestions you have for improvement)




"""

import readfile


def main():
    """
    - Input and execute a file formatted for "The Machine"
    """
    # Get chosen file from the user.
    program_file = input('Enter the name of the program to execute: ')
    # Execute the chosen file.
    execute(program_file)


def execute(program_file):
    """
    - Execute a program file formatted for "The Machine"
    :param str program_file: name of the file to execute
    """

    num_of_0ps = -1
    readfile.set_file(program_file)
    if checkMagicNumber(readfile.read_byte() + readfile.read_byte()):
        num_of_ops = readNumOfOps(readfile.read_byte())
        # readOps()

    readfile.set_file(program_file)

def checkMagicNumber(header):
    return header == b'\x31\x41\xFA\xCE'


def readNumOfOps(next_byte):
    return int.from_bytes(next_byte, "big")

  
def read_operand():
    b1 = readfile.read_byte()
    b2 = readfile.read_byte()
    opd = b1 + b2
    opd = int.from_bytes(opd, 'big')

    if opd == 1:
        add()
    elif opd == 2:
        subtract()
    elif opd == 3:
        multiply()
    elif opd == 4:
        divide()
    elif opd == 5:
        string()
    else:
        error()


def add():
    pass


def subtract():
    pass


def multiply():
    pass


def divide():
    pass


def string():
    pass


def error():
    pass


# Invoke the main method to run the program.
main()
