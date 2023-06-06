import argparse

def my_command():
    print("This is my command.")

def another_command():
    print("This is another command.")

def main():
    parser = argparse.ArgumentParser(description='This is a simple CLI tool.')
    
    # The 'dest' argument is used to specify the attribute name to store the result.
    # The 'action' argument tells argparse what to do when this command is encountered.
    parser.add_argument('--my-command', dest='my_command', action='store_true',
                        help='Run my command.')
    parser.add_argument('--another-command', dest='another_command', action='store_true',
                        help='Run another command.')
    
    args = parser.parse_args()

    if args.my_command:
        my_command()
    elif args.another_command:
        another_command()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
