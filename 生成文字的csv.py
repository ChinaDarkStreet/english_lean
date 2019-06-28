s = '''Electric vehicles currently make up a small percentage of overall car sales worldwide. But 2018 saw a big jump in international sales. And the market is expected to grow quickly in coming years.
JATO Dynamics researches cars and other vehicles. The company reported electric car sales rose by 74 percent in 2018. More than a million and a quarter electric cars were sold. Put another way, the company said electric car sales represented about 1.5 percent of total vehicle sales around the world.
Each of these electric vehicles will require a battery to power it – sometimes more than one. Electric car batteries become less effective over time and need to be replaced. Currently, most major auto manufacturers guarantee good battery performance for only about eight years.
So, one American company has found an unusual way to reuse the batteries that electric vehicles are no longer using. The company, called Eaton, is a large supplier of truck parts and industrial products to businesses all over the world.
Eaton is also an energy storage company. It takes aging batteries – which it calls "second-life batteries" - from Nissan's electric Leaf vehicles. The company then reuses them with its xStorage product, which stores power in buildings.
An official with Eaton recently told Reuters news agency the company is now in talks with several European football teams. They are discussing using electric batteries to help power their stadiums.
Eaton has already equipped a major stadium in the Netherlands with such a system. The project was completed at Johan Cruyff Arena in Amsterdam. The stadium holds about 54,000 people and is home to the country's Ajax football team, one of Europe's best known. It also holds large concerts and other major events.
The company also recently completed an energy storage system at Norway's Bislett stadium in Oslo. This stadium is partly powered by solar energy.
"The football stadium community is interested," Eaton vice president Craig McDonnell told Reuters. "From significant ones, (we are talking) with five to six stadiums in Europe," he said.
Eaton said its xStorage solution costs 20 percent less than a new battery. The storage system at Johan Cruyff Arena can produce a total of 3 megawatts. The company says that is enough to power several thousand homes. The system stores power gathered from 4,200 solar collectors on top of the stadium, Eaton says.
The system is designed to provide back-up power to reduce the need for diesel generators, which produce pollution. It also boosts the energy system during times of high energy usage, such as during concerts. Eaton says the storage system results in a more sustainable energy method, while also creating "a circular economy for electric vehicle batteries."
Eaton is one of several major companies attempting to develop large markets for old electric vehicle batteries. Another is German automaker BMW. It has supplied used batteries from its i3 electric vehicles to store electricity produced by wind farms.
Eaton says it expects the used battery market to grow up to 20 times by 2022. In Europe, the Middle East and Africa, it estimates the possible market value could reach $2.3 billion by 2025.
I'm Bryan Lynn.'''


ws = s.replace("\n", " ")\
    .replace(".", "")\
    .replace(",", "")\
    .replace("(", "")\
    .replace(")", "")\
    .replace('"', '')\
    .split(" ")


wss = set()
for i in ws:
    wss.add(i)


import pymysql
db = pymysql.connect("localhost","root","root","edic" )
cursor = db.cursor()
words = []
sql = "SELECT * from stardict where word = \"%s\""
def query_word(w):
    cursor.execute(sql%w)
    res = cursor.fetchall()
    if len(res) >= 1:
        return res[0]
    else:
        print("没有翻译 -- ", i)
        return ""


for i in wss:
    words.append((i, query_word(i)))


with open("tmp.csv", "w", encoding="gbk") as f:
    for i in words:
        tmp = i[1]
        if not tmp == "":
        #       单词， 中文翻译， 英文翻译， 柯林斯等级， 牛津三千， 历史词频， 当代语料库词频顺序
            f.write("%s#%s#%s#%s#%s#%s#%s\n"%(i[0],tmp[5].replace("\n"," "),tmp[4].replace("\n"," "),tmp[7],tmp[8],tmp[10],tmp[11]))
