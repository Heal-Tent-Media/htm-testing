from celery import shared_task
import boto3
from abstractaction.notify_admin import notify_new_client


@shared_task
def send_mail_for_client(client):
    # sending mail
    ses = boto3.client('ses', region_name='us-east-1')
    try:
        ses.send_templated_email(
            Source='healtentmedia@gmail.com',
            Destination={
                'ToAddresses': [
                    client[1],
                ]
            },
            ReplyToAddresses=[
                'contact@healtentmedia.com'
            ],
            Template='WelcomeTemplate',
            TemplateData='{ \"name\":\"' + client[0] + '\" }'
        )
        print('notify admin')
        notify_new_client.delay(client[2], client)
        return True
    except ConnectionError:
        return False
    finally:
        return False
