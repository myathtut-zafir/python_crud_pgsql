import psycopg2 # type: ignore

conn = psycopg2.connect(host="localhost",
                        dbname="Python1",
                        user="myathtut",
                        password="",
                        port=5432)

cur=conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
    );
    """)

cur.execute(""" INSERT INTO person(id,name,age,gender) VALUES
            (1,'Mike',30,'m'),
            (2,'Mike',30,'m'),
            (3,'Mike',30,'m'),
            (4,'Mike',30,'m'),
            (5,'Mike',30,'m'),
            (6,'Mike',30,'m'),
            (7,'MikeLast',30,'m');

            """)

cur.execute("""SELECT * FROM person; """)
# print(cur.fetchall())

for row in cur.fetchall():
    print(row)

sql= cur.mogrify("""SELECT * FROM person where name='MikeLast'; """)
print(sql)
conn.commit()
cur.close()
conn.close