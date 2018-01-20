# 部署说明

## 环境变量
    # 数据库环境变量
    DATABASE_NAME = "db_bootmeeting"
    DATABASE_USER = "DATABASE_USER"
    DATABASE_HOST = "127.0.0.1"
    DATABASE_PORT = 13306
    DATABASE_PASSWORD = "root"
    
    # 邮件相关环境变量
    EMAIL_SENDER = 'chenlin_youdao@126.com'
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtp.126.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'chenlin_youdao@126.com'
    EMAIL_HOST_PASSWORD = 'xxxx'
    
    # 其他，这个是用于从OA进行用户同步
    OA_DB_HOST = '106.14.180.170'
    OA_DB_USER = 'rms'
    OA_DB_PORT = 3306
    OA_DB_PASSWORD = 'rms@dragonest.com'
    OA_DB_NAME = 'oa'
    
    
# 运行
    python manage.py runserver 8080
    python manage.py crontab add