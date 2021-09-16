import hashlib
import random
import string
from datetime import datetime
import secrets


def random_char_generator():
    password_characters = string.digits + secrets.token_urlsafe(20)
    password_characters = ''.join(random.choice(password_characters) for i in range(3))
    return str(password_characters)


def mail_verify_hash(subscriber_id, subscriber_mail):
    hash_string = str(datetime.now) + 'htm-sm-verify-mail-hash' + subscriber_id + subscriber_mail
    hash_string = hashlib.md5(hash_string.encode()).hexdigest()
    hash_string = random_char_generator() + hash_string[3:8] + random_char_generator() + hash_string[
                                                                                         12:16] + random_char_generator() + hash_string[
                                                                                                                            20:]
    return str(hash_string)


def unsubscribe_hash(subscriber_id, subscriber_mail):
    hash_string = str(datetime.now()) + 'htm-sm-unsubscribe-hash' + subscriber_id + subscriber_mail
    hash_string = hashlib.md5(hash_string.encode()).hexdigest()
    hash_string = random_char_generator() + hash_string[3:8] + random_char_generator() + hash_string[
                                                                                         12:16] + random_char_generator() + hash_string[
                                                                                                                            20:]
    return str(hash_string)


def preference_hash(subscriber_id, subscriber_mail):
    hash_string = str(datetime.now()) + 'htm-sm-change-preference-hash' + subscriber_id + subscriber_mail
    hash_string = hashlib.md5(hash_string.encode()).hexdigest()
    hash_string = random_char_generator() + hash_string[3:8] + random_char_generator() + hash_string[
                                                                                         12:16] + random_char_generator() + hash_string[
                                                                                                                            20:]
    return str(hash_string)
