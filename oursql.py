

def setsql(param):


    conn=sqlite3.connect("accounts.db")
   # print param
    c=conn.cursor()
    sql_insert="insert into {tablename}(id, private, public, address, wif) values {ourvalue}".format(tablename="account",ourvalue=param)
    try:
        c.execute(sql_insert)
    except:
        'sql_insert is not correct!!'
    #print sql_insert

    conn.commit()
    conn.close()