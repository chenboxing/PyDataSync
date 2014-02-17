import pyodbc
import os
import shutil
import ConfigParser
import logging
import logging.config

logging.config.fileConfig("settings.conf")
#create logger
logger = logging.getLogger("example")


#read the configuration information
conf = ConfigParser.ConfigParser()
conf.read('settings.conf')


#conf.get('DB', 'server'), conf.get('DB', 'database'), conf.get('DB', 'username'), conf.get('DB', 'password')

logger.info("Begin to process")
conn_str = 'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (conf.get('DB','server'), conf.get('DB','database'), conf.get('DB','username'), conf.get('DB','password'))
logger.info(conn_str)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()


server_ip = conf.get('Settings',"server_ip")
data_folder = conf.get('Settings',"data_folder")
removed_folder = conf.get('Settings',"removed_folder")

# get all host for the specify server
cursor.execute("""select distinct H.HostName from Main_HostList H, Main_Goods G, Main_Server S
              where H.GoodsNO = G.GoodsNO
            and G.ServerID = S.ServerID and S.IP=?""", server_ip)

hosts = []
for row in cursor:
    hosts.append(row.HostName)

# remove folder that has not in the db
for subdir in os.listdir(data_folder):
    if not subdir in hosts:
        logger.info("folder %s  doesn't exists on db" % subdir)
        source = data_folder + subdir
        dest = removed_folder + subdir
        shutil.move(source, dest)

logger.info("Finished")

