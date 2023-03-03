import imaplib, email
from constants import gmail_user,gmail_RECEIVING_appPass,SMS_number





def thisWholdThingIsAFunction():
    user = gmail_user
    password = gmail_RECEIVING_appPass
    imap_url = 'imap.gmail.com'
    
    # Function to get email content part i.e its body part
    def get_body(msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)
    
    # Function to search for a key value pair
    def search(key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data
    
    # Function to get the list of emails under this label
    def get_emails(result_bytes):
        msgs = [] # all the email data are pushed inside an array
        for num in result_bytes[0].split():
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)
    
        return msgs
    
    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url)
    
    # logging the user in
    con.login(user, password)
    
    # calling function to check for email under this label
    con.select('Inbox')
    
    # fetching emails from this user "tu**h*****1@gmail.com"
    msgs = get_emails(search('FROM', SMS_number, con))

    mailCount = len(msgs)

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

                        cut1 = htmlData.split("<td>")
                        cut2 = cut1[1].split("</td>")
                        phrase = cut2[0]
                        phrase = phrase.strip()

                        
                        counter += 1
                        
        
                    except UnicodeEncodeError as e:
                        pass


    msgs = get_emails(search('FROM', SMS_number, con))
    mailCount = len(msgs)

    whyMakeMeDoThis = str(mailCount) + "/|/" + str(phrase)

    
    return str(whyMakeMeDoThis)


