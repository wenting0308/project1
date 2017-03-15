
from linkServer.rds_config import *
import sys
import logging
import pymysql


rds_db = rds_config()
rds_db.db_config_setup()

rds_host = rds_db.db_endpoint
name = rds_db.db_username
password = rds_db.db_password
db_name = rds_db.db_name
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=20)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()
    
else:
    print("finished link")