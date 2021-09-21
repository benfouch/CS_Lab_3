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

    try:
        readfile.set_file(program_file)
        if check_magic_number(readfile.read_byte() + readfile.read_byte() + readfile.read_byte() + readfile.read_byte()):
            read_operand(read_num_of_ops(readfile.read_byte() + readfile.read_byte()))
    except:
        print("Invalid File")
    finally:
        readfile.set_file(program_file)


def check_magic_number(header):
    return header == b'1A\xfa\xce'


def read_num_of_ops(next_byte):
    return int.from_bytes(next_byte, "big")


def read_operand(num_of_ops):
    while num_of_ops != 0:
        b1 = readfile.read_byte()
        opd = b1
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
            raise Exception("Operand Not Supported")

        num_of_ops -= 1


def add():
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") + int.from_bytes(byte_2, "big"))


def subtract():
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") - int.from_bytes(byte_2, "big"))


def multiply():
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") * int.from_bytes(byte_2, "big"))


def divide():
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") / int.from_bytes(byte_2, "big"))


def string():
    next_byte = readfile.read_byte()
    end_string = ""
    while next_byte != b'\x0A':
        end_string += next_byte.decode("ASCII")
        next_byte = readfile.read_byte()
    end_string += next_byte.decode("ASCII")
    print(end_string)


# Invoke the main method to run the program.
main()
