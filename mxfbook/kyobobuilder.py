import instrument as inst
import uuid

class KyoboBuilder:
    def __init__(self):
        pass


# krcode 에 있는거 우선
def build_instrument(args):

    if args['inst_type'] == 'vanilla_swap':
        return _build_instrument_vanilla_swap(args)
    elif args['inst_type'] == 'fixed_bond':
        return _build_instrument_fixed_bond(args)
    elif args['inst_type'] == 'stock':
        return _build_instrument_stock(args)
    elif args['inst_type'] == 'bond':
        return _build_instrument_stock(args)
    elif args['inst_type'] == 'option':
        return _build_instrument_stock(args)
    elif args['inst_type'] == 'fututes':
        return _build_instrument_stock(args)
    elif args['inst_type'] == 'deposit':
        return _build_instrument_stock(args)
    elif args['inst_type'] == 'realestate':
        return _build_instrument_realestate(args)
    elif args['inst_type'] == '':
        return _build_instrument_realestate(args)
    elif args['inst_type'] == '':
        return _build_instrument_realestate(args)
    else:
        return None


def _build_instrument_vanilla_swap(args):
    _inst = inst.Swap()
    _inst.name = str(uuid.uuid4())
    _inst['inst_type'] = 'vanilla_swap'
    _inst['notional'] = args['notional']
    _inst['currency'] = 'krw'
    _inst['effective_date'] = 'krw'
    _inst['maturity_date'] = 'krw'
    _inst['side'] = 'long'

    payleg_args = dict()
    payleg_args['leg_type'] = 'fixed'
    _inst['pay_leg'] = _build_leg(payleg_args)

    recleg_args = dict()
    payleg_args['leg_type'] = 'vanilla_floating'
    _inst['rec_leg'] = _build_leg(recleg_args)

    return _inst


def _build_leg(args):
    return inst.FixedRateLeg()


def _build_fixed_leg(args):
    cpn = inst.FixedRateLeg()
    return cpn


def _build_fixedrate_coupon(args):
    cpn = inst.FixedRateCoupon()

    return cpn


def _build_vanilla_floating_leg(**args):
    return inst.FixedRateLeg()


def _build_instrument_fixed_bond(**args):
    _inst = inst.Swap()
    _inst.name = str(uuid.uuid4())
    _inst['inst_type'] = 'vanilla_swap'
    _inst['notional'] = args['notional']
    _inst['currency'] = 'krw'
    _inst['effective_date'] = 'krw'
    _inst['maturity_date'] = 'krw'
    _inst['side'] = 'long'
    _inst['leg'] = 'krw'

    return inst.Swap()