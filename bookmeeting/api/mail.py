# coding=utf-8
import json
import logging

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
import os
import jinja2
from django.conf import settings
import tempfile

logger = logging.getLogger('book-meeting')


class BaseMail(object):
    def __init__(self, subject, sender, receiver, **kwargs):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.message = kwargs.pop('message', 'empty message!')
        self.tpl = tempfile.TemporaryFile()

    def send_plaintext_mail(self):
        try:
            return send_mail(self.subject, self.message, self.sender, self.receiver)
        except Exception as e:
            logger.error('send mail error: {}'.format(str(e)))
            return str(e)

    def send_html(self):
        # content = self.page_content.decode()
        msg = EmailMultiAlternatives(subject=self.subject, body=self.message, from_email=self.sender, to=self.receiver)
        msg.attach_alternative(self.message, 'text/html')
        try:
            return msg.send()
        except Exception as e:
            logger.error('send mail error: {}'.format(str(e)))
            return "Exception: {}".format(str(e))


def send_invitation(receiver, book_user, subject, start_time, end_time, members, location):
    current_dir = os.path.join(settings.BASE_DIR, 'templates')
    tpl_loader = jinja2.FileSystemLoader(searchpath=current_dir)
    tpl_env = jinja2.Environment(loader=tpl_loader)
    tpl = tpl_env.get_template('invitation.j2')

    # 处理显示的用户名称
    logger.debug('args:{}'.format(receiver, book_user, subject, start_time, end_time, members, location))
    you_real_name = User.objects.get(username=receiver).first_name
    book_user_real_name = User.objects.get(username=book_user).first_name
    yy = '{}[{}]'.format(you_real_name, receiver)
    bb = '{}[{}]'.format(book_user_real_name, book_user)
    mm = [book_user]
    logger.debug(members)
    for m in members.split(';'):
        if len(m) == 0: continue
        logger.debug('search user: [{}] on auth db'.format(m))
        u = User.objects.get(username=m)
        mm.append(u.first_name)

    html = tpl.render(you=yy,
                      book_user=bb,
                      subject=subject,
                      start_time=start_time,
                      end_time=end_time,
                      members=mm,
                      location=location)

    user_mail = '{}@dragonest.com'.format(receiver)
    logger.debug(json.dumps({'receiver': user_mail, 'sender': settings.EMAIL_SENDER}))
    mail = BaseMail(subject, settings.EMAIL_SENDER, [user_mail], **{'message': html})
    send_result = mail.send_html()
    if send_result == 1:
        logger.debug('send invitation to {} success'.format(receiver))
    else:
        logger.debug('send invitation to {} failure'.format(receiver))
        raise Exception('send invitation to {} failure')
