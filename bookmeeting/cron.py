from .logic import sync_user


def sync_oa_user():
    sync_user()


def test():
    print('test cron')
    return 123
