import pymysql, os 

# 读取数据源
from stardict import DictCsv
csvname = os.path.join(os.path.dirname(__file__), 'ecdict.csv')
dc = DictCsv(csvname)
rows = dc.get_all_words()
#插入mysql
db = pymysql.connect("localhost","root","root","edic" )
cursor = db.cursor()
sql = 'insert into stardict values (default, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
count = 0
errors = []
for i in rows:
    count += 1
    try:
        cc = cursor.execute(sql%(i[0].replace('"', '\\"'), i[15].replace('"', '\\"'), i[1].replace('"', '\\"'), i[2].replace('"', '\\"'), i[3].replace('"', '\\"'), i[4], "0" if i[5] == "" else i[5], "0" if i[6] == "" else i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
        print(count)
    except Exception as e:
        errors.append(i)
    if count >10000:
        count = 0
        db.commit()
db.commit()
db.close()

# 把错误的写到文件中
with open("err_sql.sql", "w", encoding="utf8") as f:
    for i in errors:
        f.write(sql%(i[0].replace('"', '\\"'), i[15].replace('"', '\\"'), i[1].replace('"', '\\"'), i[2].replace('"', '\\"'), i[3].replace('"', '\\"'), i[4], "0" if i[5] == "" else i[5], "0" if i[6] == "" else i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
        f.write("\n")

print("完成")