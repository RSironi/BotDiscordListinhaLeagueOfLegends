import connection as connection

#ADD - Command Bot = !!addListinha @User @Champ
def add(userID: int, champName: str):
    sql = "INSERT INTO listinha (id_usuario,fk_champs_nome_champ) values (%s,%s);"
    val = (userID, champName)
    connection.cursor.execute(sql,val)
    connection.con.commit()

#DELETE - Command Bot = !!delListinha @User @Champ
def delete(userID: int, champName: str):
    sql = "DELETE FROM listinha where id_usuario = %s and fk_champs_nome_champ = %s;"
    val = (userID,champName)
    connection.cursor.execute(sql,val)
    connection.con.commit()

#SELECT - Command Bot = !!Listinha @User
def select(userID: int, userName:str):
    result= f":\n:man_mage:SELADOS DE {userName}:man_mage:\n"
    sql = f"SELECT fk_champs_nome_champ from listinha where id_usuario = {userID};"
    connection.cursor.execute(sql)
    fetchresult = connection.cursor.fetchall()
    for x in fetchresult:
        result = result + ":no_entry_sign:" + x[0] + "\n"
    return result