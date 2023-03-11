import transform as i
from process.load import Load
#import sqlalchemy as db
#import pymysql
#from process.util import utils as u
#pymysql.install_as_MySQLdb()

load = Load()

df_enunciado1 = i.df_enunciado1
df_enunciado2 = i.df_enunciado2
df_enunciado3 = i.df_enunciado3
df_enunciado4 = i.df_enunciado4

load.load_to_adls(df_enunciado1,"datalake", "americo/gold/df_enunciado1")
load.load_to_adls(df_enunciado2,"datalake", "americo/gold/df_enunciado2")
load.load_to_adls(df_enunciado3,"datalake", "americo/gold/df_enunciado3")
load.load_to_adls(df_enunciado4,"datalake", "americo/gold/df_enunciado4")

#u.create_mysql_tbl_schema(df_enunciado1, u.mysql_conn(u.mysql_engine()), 'retail', "enunciado1")
#u.create_mysql_tbl_schema(df_enunciado2, u.mysql_conn(u.mysql_engine()), 'retail', "enunciado2")
#u.create_mysql_tbl_schema(df_enunciado3, u.mysql_conn(u.mysql_engine()), 'retail', "enunciado3")
#u.create_mysql_tbl_schema(df_enunciado4, u.mysql_conn(u.mysql_engine()), 'retail', "enunciado4")

#load.load_mysql(df_enunciado1, "enunciado1")
#load.load_mysql(df_enunciado2, "enunciado2")
#load.load_mysql(df_enunciado3, "enunciado3")
#load.load_mysql(df_enunciado4, "enunciado4")