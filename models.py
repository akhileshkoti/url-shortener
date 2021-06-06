import sqlite3
from hashlib import md5
def create_hash(link):
    con=sqlite3.connect('DDS')
    cur=con.cursor()
    check = cur.execute("select tiny from urltab where url=?",(link,)).fetchone()
    if(check != None):
        return(check[0])
    tiny=md5(link.encode())
    tiny=tiny.hexdigest()
    params=(link,tiny)
    cur.execute("insert into urltab(url,tiny) values(?,?)",params)
    con.commit()
    con.close()
    return(tiny)
def revoke(id):
    con=sqlite3.connect('DDS')
    cur=con.cursor()
    check = cur.execute("select url from urltab where tiny=?",(id,)).fetchone()
    print("check=",check)
    if(check != None):
        return(check[0])
    con.commit()
    con.close()
    return("create new")