#! python3
import webbrowser, sys, pyperclip

sys.argv
if len(sys.argv) > 1:
    address=' '.join(sys.argv[1:])
else:
    print('Please enter the address')

webbrowser.open('https://www.google.com/maps/search/' + address)
