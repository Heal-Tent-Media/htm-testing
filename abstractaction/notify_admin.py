from celery import shared_task
import boto3

# notify_phone_list = ["+918508663203", "+917010397367", "+919698913355"]
notify_phone_list = ["+918508663203", "+917010397367"]

notify_mail_list = ["simuchand.balachandran@gmail.com", "ceo@healtentmedia.com", "cdo@healtentmedia.com"]


@shared_task
def notify_new_client(program, client):
    # create sns client
    sns = boto3.client('sns', region_name='us-east-1')

    # create ses client
    ses = boto3.client('ses', region_name='us-east-1')

    #  send msg
    notify_msg_list = ["Unknown request called.",
                       "New Client Request for" + client[2] + "through form. Reach out to your client"]
    for phone in notify_phone_list:
        msg = notify_msg_list[0]
        if str(program):
            msg = notify_msg_list[1]
        try:
            print(phone)
            print(msg)
            sns.publish(
                PhoneNumber=str(phone),
                Message=str(msg)
            )
            print("Msg sent to admin")
        except ConnectionError:
            continue

    #  send mail
    subject = "AAN - New Client"
    title = "New Client Request"
    for mail in notify_mail_list:
        try:
            ses.send_templated_email(
                Source='healtentmedia@gmail.com',
                Destination={
                    'ToAddresses': [
                        mail,
                    ]
                },
                ReplyToAddresses=[
                    'ceo@healtentmedia.com'
                ],
                Template='AdminNotifyNewClient',
                TemplateData='{\"subject\":\"' + subject +
                             '\",\"title\":\"' + title +
                             '\",\"name\":\"' + client[0] +
                             '\",\"mail\":\"' + client[1] +
                             '\",\"request\":\"' + client[2] +
                             '\",\"req_time\":\"' + client[3] + '\"}',
            )
            print("Mail sent to admin")
        except ConnectionError:
            continue
