import json


class Instrument(dict):
    def __init__(self):
        dict.__init__(self)

    def get_json(self):
        return ''


class Leg(dict):
    def __init__(self):
        pass

    def get_coupons(self):
        return self.coupons


class FixedRateLeg(Leg):
    def __init__(self):
        Leg.__init__(self)


class Coupon(dict):
    def __init__(self):
        dict.__init__(self)


class FixedRateCoupon(Coupon):
    def __init__(self):
        Coupon.__init__(self)


class Swap(Instrument):
    def __init__(self):
        Instrument.__init__(self)

