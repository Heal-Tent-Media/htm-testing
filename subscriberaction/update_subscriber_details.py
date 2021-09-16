from django.http import HttpResponse
from datetime import date
import json
from index.models import MailSubscriber
from subscriberanalytics.models import UnsubscriptionAnalytic, PreferenceAnalytic
from abstractaction import hashgenerator


def unsubscribe_update(s_id, reason, comment):
    # updating subscriber table
    subscriber = MailSubscriber.objects.get(ms_id=s_id)
    subscriber.ms_sub_status = False
    un_sub_hash = hashgenerator.unsubscribe_hash(s_id, subscriber.ms_mail)
    subscriber.ms_unsubscribe_hash = un_sub_hash
    subscriber.ms_unsub_date = date.today()
    subscriber.save()

    # updating preference analytics
    unsub_instance = UnsubscriptionAnalytic()
    unsub_instance.sub_id = s_id
    unsub_instance.uns_reason = 'unsr-'+reason
    unsub_instance.uns_comment = comment
    unsub_instance.uns_date = date.today()
    unsub_instance.save()
    response = {
        "redirect_url": 'action-status/unsubscribe/?id=' +
                        str(s_id[-7:]) +
                        '&actionurl=' + str(un_sub_hash) +
                        '&status=success&update=unsubscribed',
    }
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


def preference_update(s_details, current_state, updated_state, changed_state):
    if current_state != updated_state:
        # updating subscriber table
        subscriber = MailSubscriber.objects.get(ms_id=s_details[0])
        subscriber.ms_promotional_mail_status = changed_state[0]
        subscriber.ms_info_mail_status = changed_state[1]
        pref_hash = hashgenerator.preference_hash(s_details[0], subscriber.ms_mail)
        subscriber.ms_preference_hash = pref_hash
        subscriber.save()

        # updating preference analytics
        pref_instance = PreferenceAnalytic()
        pref_instance.pref_id = get_last_pref_id()
        pref_instance.sub_id = s_details[0]
        pref_instance.pref_state = str(current_state + updated_state)
        pref_instance.pref_date = date.today()
        pref_instance.save()
        response = {
            "redirect_url": 'action-status/preference-update/?id=' +
                            str(s_details[0][-7:]) +
                            '&actionurl=' + str(pref_hash) +
                            '&status=success&update=changed',
        }
        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )
    else:
        response = {
            "redirect_url": 'action-status/preference-update/?id=' +
                            str(s_details[0][-7:]) +
                            '&actionurl=' + str(s_details[1]) +
                            '&status=success&update=held',
        }
        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )


def get_last_pref_id():
    count = PreferenceAnalytic.objects.count()
    if count is None:
        return '1'
    else:
        return str(count + 1)
