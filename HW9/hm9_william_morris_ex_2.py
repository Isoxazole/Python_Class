import imapclient
import threading
import pyzmail
import time
import datetime
import json

userEmail = 'wmorris1367@gmail.com'
password = 'MyPassword'


def checkMessages():
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(userEmail, password)

    # Read only false so email will be read when open
    imapObj.select_folder('INBOX', readonly=False)

    #searches only unread emails
    UIDs = imapObj.search(f'(SUBJECT Instructions FROM {userEmail} UNSEEN)')
    print(UIDs)

    for UID in UIDs:
        rawMessages = imapObj.fetch(UID, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
        # execute the subject instructions
        instructions = message.get_subject()

        instructions = instructions.replace("INSTRUCTIONS", "")
        print(instructions)
        loadMessage = json.loads(instructions)

        print(loadMessage)
        number = loadMessage["instruction"]

        if number == 1:
            firstName = loadMessage["arguments"]["firstName"]
            lastName = loadMessage["arguments"]["lastName"]
            print(f"Hi, my name is {firstName} {lastName}")
        elif number == 2:
            print(f"Hello, today's date is {datetime.date.today()}")
        elif number == 3:
            person = loadMessage["arguments"]["person"]
            feeling = loadMessage["arguments"]["feeling"]
            print(f"Hello there! {person} is feeling {feeling} today!")


def checkTime():
    while True:
        checkMessages()
        time.sleep(60*15)


threadObj = threading.Thread(target=checkTime)
threadObj.start()


