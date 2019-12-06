# argparse is part of the STL
# https://docs.python.org/3/howto/argparse.html
import argparse

def printArgs(parser):
    # To show the results of the given option to screen.
    for _, value in parser.parse_args()._get_kwargs():
        if value is not None:
            print(value)

def main():
    parser = argparse.ArgumentParser()

    # create a simple argument. by default its mandatory that this is passed
    parser.add_argument("mandatoryArg")

    # accept an int. otherwise argument is treated as a string
    parser.add_argument("-int", help="get an int only", type=int)

    # store a text in the action=XYZ field if just "-v" is passed with no other arguments
    parser.add_argument("-v", help="print debug information", action="store_true")
    

    # if you give it a posix argument like "-s" it becomes optional
    parser.add_argument("-s", "--single", help="takes any single value")
    
    # accept a list of arguments. 
    # '+' == 1 or more.
    # '*' == 0 or more.
    # '?' == 0 or 1.
    parser.add_argument("-l", "--list", nargs="+", help="takes a list of values")

    args = parser.parse_args()

    if args.v:
        print("verbose")

if __name__ == "__main__":
    main()