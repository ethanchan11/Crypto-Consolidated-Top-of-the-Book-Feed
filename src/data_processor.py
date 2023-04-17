import sys
import time
import pandas as pd

def consolidate(ob, exchanges):
    if len(ob) == 0:
        return

    bids = {}
    asks = {}
    bid_volumes = {}
    ask_volumes = {}

    for exchange in exchanges:
        try:
            ob[exchange]
            bid_volumes[exchange] = ob[exchange][2]
            bids[exchange] = ob[exchange][3]
            asks[exchange] = ob[exchange][4]
            ask_volumes[exchange] = ob[exchange][5]
        except:
            bid_volumes[exchange] = 0
            bids[exchange] = 0
            asks[exchange] = sys.maxsize
            ask_volumes[exchange] = 0

    new_bid = max(bids.values())
    new_ask = min(asks.values())

    best_bid_exchanges = [exchange for exchange, bid in bids.items() if bid == new_bid]
    best_ask_exchanges = [exchange for exchange, ask in asks.items() if ask == new_ask]

    best_bid_size = sum([bid_volumes[exchange] for exchange in best_bid_exchanges])
    best_ask_size = sum([ask_volumes[exchange] for exchange in best_ask_exchanges])

    output = pd.DataFrame([{
        'time': time.time_ns(),
        'symbol': 'ETHUSD',
        'bid_exchange': ', '.join(best_bid_exchanges),
        'bestbid': new_bid,
        'bestbidsize': best_bid_size,
        'ask_exchange': ', '.join(best_ask_exchanges),
        'bestask': new_ask,
        'bestasksize': best_ask_size
    }])

    print(output)

    return output
