from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

'''
def main():
    i=0
   
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['UNREAD']).execute()
    messages = results.get('messages', [])
    
    print(len(messages))
    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            # payload=msg['payload']
            # print("from : "+payload['headers'][16]['value'])
            print(msg['snippet'])
            print(len(msg))
            print("\n")
            i+=1
            if i > 1 :
                break

        # for message in messages: #모든 메일가져옴
        #     msg = service.users().messages().get(userId='me', id=message['id']).execute()
        #     print(msg['snippet'])
'''

def getUnreadMail():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['UNREAD']).execute()
    messages = results.get('messages', [])

    return len(messages)

if __name__ == '__main__':
    main()