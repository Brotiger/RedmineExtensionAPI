from components.DB import DB

class Project():
  @staticmethod
  def setStatus(identifite, status):
    db = DB.getConnection()
    cur = db.cursor()

    sql = "UPDATE projects SET status = %s WHERE identifier = %s"
    result = cur.execute(sql, (str(status), str(identifite)))
    db.commit()

    cur.close()

    if result:
      return True

    return False
