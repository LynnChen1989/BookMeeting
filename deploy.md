# 部署说明

## 环境变量
    # 表明生产环境
    PROD = 1
    # 数据库环境变量
    DATABASE_NAME = "db_bootmeeting"
    DATABASE_USER = "DATABASE_USER"
    DATABASE_HOST = "127.0.0.1"
    DATABASE_PORT = 13306
    DATABASE_PASSWORD = "root"
    
    # 邮件相关环境变量
    EMAIL_SENDER = 'xxxx@126.com'
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtp.126.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'xxxx@126.com'
    EMAIL_HOST_PASSWORD = 'xxxx'
    
    # 其他，这个是用于从OA进行用户同步, 同步的数据写入到User表
    OA_DB_HOST = ''
    OA_DB_USER = ''
    OA_DB_PORT = 3306
    OA_DB_PASSWORD = ''
    OA_DB_NAME = 'oa'
    
    
# 运行
    python manage.py runserver 8080
    python manage.py crontab add
    
    
# 说明
    由于这是针对本公司的会议室预定系统开源版本，