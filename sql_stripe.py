import sqlite3
# import stripe


def init_db():
    confirm = raw_input('THIS WILL DELETE YOUR DB IF IT EXISTS. Are you sure you want to continue? [Y/n] ')
    if confirm == 'y' or confirm == 'Y':
        print 'creating db...'
        with sqlite3.connect("stripeserverkeys.db") as connection:
            c = connection.cursor()
            c.execute("DROP TABLE IF EXISTS keys")
            c.execute("CREATE TABLE keys(public TEXT UNIQUE, secret TEXT UNIQUE, email TEXT)")
    else:
        print 'Exiting without making changes...'


def addkeys(newpost):
    with sqlite3.connect("stripeserverkeys.db") as connection:
        c = connection.cursor()
        c.execute('INSERT INTO keys VALUES(?, ?, ?)', (newpost))


def charge(seckey, token, amount, description):
    return {"message": "This service is no longer available."}
