path = 'scripts/select_query.sql'
 

def read_file():
    with open(path, 'r') as r1:
        return r1.read()

print(read_file())