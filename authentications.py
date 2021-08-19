import yaml2 as yaml

def creds(index):
    with open('db_credentials.yaml', 'r') as cred:
        credentials = yaml.load(cred, Loader=yaml.FullLoader)
        credentials1 = tuple(credentials)
        return credentials1[index]

database = creds(0).get('database')
user = creds(1).get('user')
password = creds(2).get('password')
host = creds(3).get('host')
port = creds(4).get('port')

connection_string = ('dbname='+ database + ' user=' + user + ' password=' + password + ' host=' + host + ' port=' + str(port))
