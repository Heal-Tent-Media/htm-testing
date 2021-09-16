def get_preference_state(promo, info):
    info_status = '20'
    promo_status = '10'
    if info:
        info_status = '21'
    if promo:
        promo_status = '11'

    return str(promo_status + info_status)
