import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd2023",
    database="escola_turmac"
)
print(banco)

meucursor = banco.cursor()

pesquisa = "select * from alunos;"

meucursor.execute(pesquisa)

resultado = meucursor.fetchall() #recebe tudo da pesquisa e retorna atraves de uma tupla

for x in resultado:
    print(x)

nome1 = "menino Ney"
telefone1 = "11111111111"
turma = "C"
media = 7
cursor = banco.cursor()
sql = "INSERT INTO alunos (nome,telefone,turma,media) VALUES (%s,%s,%s,%s)"
data = (nome1,telefone1,turma,media)
cursor.execute(sql,data)
banco.commit()
userid = cursor.lastrowid
print(userid)
for x in resultado:
    print(x)
cursor.close()
banco.close()
