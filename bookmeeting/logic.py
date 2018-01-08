import MySQLdb
import os
import logging
from django.contrib.auth.models import User

logger = logging.getLogger('rms')

OA_DB_HOST = os.environ.get('OA_DB_HOST', '106.14.180.170')
OA_DB_USER = os.environ.get('OA_DB_USER', 'rms')
OA_DB_PORT = os.environ.get('OA_DB_PORT', 3306)
OA_DB_PASSWORD = os.environ.get('OA_DB_PASSWORD', 'rms@dragonest.com')
OA_DB_NAME = os.environ.get('OA_DB_NAME', 'oa')


def db_conn():
    db = MySQLdb.connect(host=OA_DB_HOST, user=OA_DB_USER, passwd=OA_DB_PASSWORD, db=OA_DB_NAME, charset="utf8")
    print(db.character_set_name())
    return db.cursor()


def sync_user():
    sql = """
    SELECT a.username, a.realname 
    FROM lywl_user a, lywl_user_profile b 
    WHERE a.uid = b.uid AND (b.quit_time > unix_timestamp(now()) OR b.quit_time=0);
    """

    conn = db_conn()
    conn.execute(sql)
    rows = conn.fetchall()
    for row in rows:
        if isinstance(row, tuple) and len(row) == 2:
            try:
                User.objects.get(username=row[0])
            except User.DoesNotExist:
                u = User(
                    username=row[0],
                    first_name=row[1],
                    email='{}@dragonest.com'.format(row[0])
                )
                u.save()