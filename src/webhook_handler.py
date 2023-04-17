import json
import websocket
import time

def on_open_factory(exchange, subscribe_messages):
    def on_open(wsapp):
        try:
            wsapp.send(json.dumps(subscribe_messages[exchange]))
        except Exception as e:
            print(e)
    return on_open

def on_message_factory(exchange, q):
    def on_message(wsapp, message):
        data = json.loads(message)
        rec_timestamps = time.time_ns()
        symbol = 'ETHUSD'

        if exchange == 'bitstamp':
            bid_price = float(data["data"]["bids"][0][0])
            bid_volume = float(data["data"]["bids"][0][1])
            ask_price = float(data["data"]["asks"][0][0])
            ask_volume = float(data["data"]["asks"][0][1])
        elif exchange == 'binance':
            bid_volume = float(data['B'])
            bid_price = float(data['b'])
            ask_price = float(data['a'])
            ask_volume = float(data['A'])
        elif exchange == 'kraken':
            bid_price = float(data[1][0])
            bid_volume = float(data[1][3])
            ask_price = float(data[1][1])
            ask_volume = float(data[1][4])

        q.put([
            rec_timestamps, 
            exchange, 
            symbol, 
            bid_volume, 
            bid_price, 
            ask_price, 
            ask_volume])

    return on_message

def on_close(wsapp):
    print("closed connection")

def run_websocket(exchange, q, endpoints, subscribe_messages, ssloptions):
    on_open = on_open_factory(exchange, subscribe_messages)
    on_message = on_message_factory(exchange, q)
    endpoint = endpoints[exchange]
    ws = websocket.WebSocketApp(endpoint,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)
    ws.run_forever(sslopt=ssloptions)
