def is_already_logged_in(f):
    
    def do_login():
        print ("Before login...")
        f()
        print ("After login...")

    return do_login


'''
def login():
    new_fun = is_already_logged_in()
    new_fun()
    print "Successfully logged in"
'''

@is_already_logged_in
def login(f):
    print "Successfully logged in"
    

def main():
    login()

if __name__ == '__main__':
    main()


