import threading
import pandas as pd
import sys
import ssl
import json
from data_processor import consolidate
from webhook_handler import run_websocket
from multiprocessing import Queue

def read_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

if __name__ == '__main__':
    config = read_config('config.json')
    BUF_SIZE = 10000
    csv_file_path = config['output_file_path']
    q = Queue(BUF_SIZE)

    EXCHANGES = config['exchanges']
    ENDPOINTS = config['endpoints']
    SUBSCRIBE_MESSAGES = config['subscribe_messages']
    SSLOPTIONS = {k: getattr(ssl, v) for k, v in config['ssl_options'].items()}
    COLUMN_NAMES = [
    'time', 
    'symbol',
    'bid_exchange',
    'bestbid', 
    'bestbidsize',
    'ask_exchange', 
    'bestask', 
    'bestasksize'
    ]

    t1 = threading.Thread(target=run_websocket, args=['bitstamp', q, ENDPOINTS, SUBSCRIBE_MESSAGES, SSLOPTIONS], daemon=True)
    t2 = threading.Thread(target=run_websocket, args=['kraken', q, ENDPOINTS, SUBSCRIBE_MESSAGES, SSLOPTIONS], daemon=True)
    t3 = threading.Thread(target=run_websocket, args=['binance', q, ENDPOINTS, SUBSCRIBE_MESSAGES, SSLOPTIONS], daemon=True)

    t1.start()
    t2.start()
    t3.start()

    df = pd.DataFrame(columns=COLUMN_NAMES)
    df.to_csv(csv_file_path, index=False)

    ob = {}
    try:
        while True:
            if not q.empty():
                item = q.get()

                ex = item[1]
                item.pop(1)
                ob[ex] = item

                data = consolidate(ob, EXCHANGES)
                data.to_csv(csv_file_path, mode='a', index=False, header=False)
    except KeyboardInterrupt:
        print("\nTerminating script...")
        sys.exit(0)
