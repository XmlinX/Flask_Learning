HOSTNAME = '192.168.31.47'
PORT = '3306'
DATABASE = 'demo_test'
USERNAME = 'root'
PASSWORD = 'root'

#dialect+driver://username:password@host:port/database
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE)