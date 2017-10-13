import sqlite3


def get_connection():
    conn = sqlite3.connect('test.db')
    return conn

def execute(command):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(command)
        values = cursor.fetchall()
        cursor.close()
        return values
    except sqlite3.Error as e:
        print e
    finally:
        conn.commit()
        conn.close()

def add(name, urgency=0, importancy=0):
    command = "insert into todo (name, urgency, importancy)\
    values (\'%s\', \'%s\', \'%s\')" % (name, urgency, importancy)
    print command
    execute(command)

def get(urgency=-1, importancy=-1):
    cmd = ["select * from todo where done = 0"]
    if urgency > -1:
        cmd.append(" and urgency = %s" % (urgency))
    if importancy > -1:
        cmd.append(" and importancy = %s" % (importancy))
    command = "".join(cmd)
    print command
    print execute(command)

def do(name):
    command = "update todo set done = 1 where name = %s" % (name)
    print command
    execute(command)

def delete(name):
    command = "delete from todo where name = '%s'" % (name)
    print command
    execute(command)