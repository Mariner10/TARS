import imaplib, email
from constants import gmail_user,gmail_RECEIVING_appPass,SMS_number,debug_mode






def thisWholdThingIsAFunction():
    user = gmail_user
    password = gmail_RECEIVING_appPass
    imap_url = 'imap.gmail.com'
    
    def get_body(msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)
    
    def search(key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data
    
    # Function to get the list of emails under this label
    def get_emails(result_bytes):
        msgs = [] # all the email data are pushed inside an array
        simp_counter = 0    # This counter -was going to be- the sole workaround to mkaing sure the mail count never reaches zero, because then
                            #   the program complains when it tries to parse the text, and ends up coming up with nothing. Luckily I did some close
                            #   reading a discovered I could shuffle a few lines around and get a better result :).
        for num in result_bytes[0].split():
            con.store(num,'+FLAGS','\\Deleted')
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)
    
        return msgs
    
    if debug_mode == True: print("Initializing email fucntions...\n")

    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url)
    
    # logging the user in
    if debug_mode == True: print("     |Logging into gmail...")
    con.login(user, password)
    
    # calling function to check for email under this label
    if debug_mode == True: print("     |Checking Inbox...")
    con.select('Inbox')
    
    if debug_mode == True: print("     |Searching for " + SMS_number + "...")
    msgs = get_emails(search('FROM', SMS_number, con))

    mailCount = len(msgs)
    if debug_mode == True: print("     |Counted " + str(mailCount) + " message(s)...")
    
    if debug_mode == True: print("     |Checking for new mail...")
    counter = 0
    for msg in msgs[::-1]:
        for sent in msg:
            if counter > 0:
                    pass
            else:
                if type(sent) is tuple:
                    
                    # encoding set as utf-8
                    content = str(sent[1], 'utf-8')
                    data = str(content)
        
                    # Handling errors related to unicodenecode
                    try:
                        indexstart = data.find("ltr")
                        data2 = data[indexstart + 5: len(data)]
                        indexend = data2.find("</div>")
        
                        # printing the required content which we need
                        # to extract from our email i.e our body
                        
                        htmlData = data2[0: indexend]
                        if mailCount > 0:
                            if debug_mode == True: print("     |Found new mail, processing...")
                            cut1 = htmlData.split("<td>")
                            cut2 = cut1[1].split("</td>")
                            phrase = cut2[0]
                            phrase = phrase.strip()
                            whyMakeMeDoThis = str(mailCount) + "/|/" + str(phrase)
                    
                            counter += 1

                            if debug_mode == True: print("     |Returning data...")

                            return str(whyMakeMeDoThis)
                        else:
                            pass
                        
                        
        
                    except UnicodeEncodeError as e:
                        pass
        
        break
    con.expunge()
    


