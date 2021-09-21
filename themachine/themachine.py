"""
- CS2911 - 011
- Fall 2021
- Lab 3
- Names:
  - Ben Fouch
  - Nathan Cernik
  - Aiden Regan

"The Machine" implementation of parsing and executing a program.

The application reads a file name from the user and executes the contents of the file or sends an error if the file format is not valid.

The file format is describe in "The Machine" exercise and the lab description.


Introduction: (Describe the lab in your own words)
    This lab is designed to have us automate(with python), the process of decoding that we have been practicing by hand.
    It helps teach us the pitfalls of dealing with bytes coming from files, and hows us how python can interpret these bytes for us.

Summary: (Summarize your experience with the lab, what you learned, what you liked, what you disliked, and any suggestions you have for improvement)
    Over all, the lab experience was very good. We were able to work as a team well to get the code done very quickly.
    We learned how to deal with bytes objects, conversion between bytes objects, and a bit of python syntax/how python works
    We have no suggestions for the lab, its great
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
    :author Ben Fouch
    """

    try:
        readfile.set_file(program_file)
        if check_magic_number(readfile.read_byte() + readfile.read_byte() + readfile.read_byte() + readfile.read_byte()):
            perform_ops(read_num_of_ops(readfile.read_byte() + readfile.read_byte()))
        else:
            print("Invalid Header")
    except:
        print("Invalid File")
    finally:
        readfile.set_file(program_file)


def check_magic_number(header):
    """
    - Checks the first bytes of the file to verify that it meets the requirements of the file format
    :param header the first 4 bytes of the file that should match the required format
    :author Ben Fouch
    :author Aiden Regan
    """
    return header == b'1A\xfa\xce'


def read_num_of_ops(next_bytes):
    """
    - Finds the number of operations to be performed in the file
    :param next_bytes the next 2 bytes from the file
    :author Ben Fouch
    :author Aiden Regan
    """
    return int.from_bytes(next_bytes, "big")


def perform_ops(num_of_ops):
    """
    - finds the value of the next operand and sends a helper method to perform it
    :param num_of_ops the number of operation in the file as given from the read_num_of_ops method
    :author Nathan Cernik
    """
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
    """
    - performs the add operation
    :author Nathan Cernik
    :author Ben Fouch
    :author Aiden Regan
    """
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") + int.from_bytes(byte_2, "big"))


def subtract():
    """
    - performs the subtract operation
    :author Nathan Cernik
    :author Ben Fouch
    :author Aiden Regan
    """
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") - int.from_bytes(byte_2, "big"))


def multiply():
    """
    - performs the multiply operation
    :author Nathan Cernik
    :author Ben Fouch
    :author Aiden Regan
    """
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") * int.from_bytes(byte_2, "big"))


def divide():
    """
    - performs the divide operation
    :author Nathan Cernik
    :author Ben Fouch
    :author Aiden Regan
    """
    byte_1 = readfile.read_byte() + readfile.read_byte()
    byte_2 = readfile.read_byte() + readfile.read_byte()
    print(int.from_bytes(byte_1, "big") / int.from_bytes(byte_2, "big"))


def string():
    """
     - Prints out the ascii value of the next bytes until the hex char '0x0A' is found
    :author Nathan Cernik
    :author Ben Fouch
    :author Aiden Regan
    """
    next_byte = readfile.read_byte()
    end_string = ""
    while next_byte != b'\x0A':
        end_string += next_byte.decode("ASCII")
        next_byte = readfile.read_byte()
    end_string += next_byte.decode("ASCII")
    print(end_string)


# Invoke the main method to run the program.
main()
