import pymysql
db = pymysql.connect("localhost", "root", "root", "edic")
cursor = db.cursor()

sql = "SELECT word from stardict where frq >1000 and word not in (SELECT word from user_words where user_id = 1) and word not in (SELECT word from no_words where user_id = 1) ORDER BY frq LIMIT 2000"
insql = "insert into user_words values (default, '%s', 1, now())"
insql1 = "insert into no_words values (default, '%s', 1, now())"
cursor.execute(sql)
ws = cursor.fetchall()

for i in ws:
    inp = input("--> %10s :"%i)
    if inp == "exit":
        db.commit()
        db.close()
        break
    if inp == "":
        cursor.execute(insql%i)
        db.commit()
    else:
        cursor.execute(insql1%i)
        db.commit()