#   Useful to see text output in terminal for non-background usage or nohup output logging.
debug_mode = True

#   You are going to need to sign into OpenAI and generate an organisation with a private key for API access.
openAI_ORG = ""
openAI_privKey = ""

#   Your phone number & carrier you are going to talk to it with.
# Carrier choices - "att", "tmobile", "verizon", "sprint".
SMS_number = ''
mobile_carrier = ''

#   Your gmail account will need to have IMAP enabled to allow python to correctly converse with it via code.
gmail_user = ""

#       You will need to enable 2FA and generate 2 app-specific passwords for these two variables,
#   you might only need one and then you change around the variables a little but two works just fine for me
gmail_SENDING_appPass = ""
gmail_RECEIVING_appPass = ''
