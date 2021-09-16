from celery import shared_task
import boto3


@shared_task
def send_mail_for_subscriber(mail_id, name, url):
    # sending mail
    ses = boto3.client('ses', region_name='us-east-1')
    response = ses.send_templated_email(
        Source='healtentmedia@gmail.com',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        ReplyToAddresses=[
            'contact@healtentmedia.com'
        ],
        Template='SubscriberWelcomeTemplate',
        # TemplateData='{ \"name\":\"' + name + '\" }',
        TemplateData='{ \"name\":\"' + name + '\", \"hashurl\": \"' + url + '\" }'
    )
    return True
