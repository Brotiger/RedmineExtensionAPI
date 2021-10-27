import pymysql
import conf

class DB():
  @staticmethod
  def getConnection():
    db = pymysql.connect(
      host=conf.dbHost,
      user=conf.dbUser,
      password=conf.dbPassword,
      port= int(conf.dbPort),
      db=conf.dbName,
    )
    
    return db