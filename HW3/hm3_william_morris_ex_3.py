#! python3
"""
Homework 3, Exercise 3
William Morris
2/12/19
This program is a simple password manager where the account name can be
entered as argument and password for that account will be copied to the
clip board
"""
import sys
import pyperclip

PASSWORDS = {'facebook': "asflkjdsljwoieuqoxcnv,mzxnc",
             'twitter': "asldkjflsjfojiwjozmcvnxdfkj",
             'instagram': "owuroiuwekjdsfknmvxczzn"}
MASTER = "Password"

account = sys.argv[1]
master = sys.argv[2]
# check if user input of password and account is valid
if master == MASTER and account in PASSWORDS:
    # copy account password from hash table
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

# if user input not valid, let user know
else:
    print('Account: ' + account + " or master password is invalid")
