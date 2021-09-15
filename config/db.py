from sqlalchemy import create_engine, MetaData

#create_engine('postgres://user:%s@host/database' % urlquote('badpass'))
#daviddem249
#conn = pymysql.connect(db='db_fastapi', user='root', passwd='daviddem249', host='localhost', port=3306)
engine = create_engine("mysql+pymysql://root:daviddem249@localhost:3306/db_fastapi") 
meta = MetaData()

conn = engine.connect()