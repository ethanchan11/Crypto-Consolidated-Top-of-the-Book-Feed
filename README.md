# Crypto-Consolidated-Top-of-the-Book-Feed

Welcome to my market analysis tool for retail crypto traders! This program consolidates real-time best bid and offer quotes from Bitstamp, Kraken, and Binance, giving you a comprehensive market overview that can help inform your trading decisions. It is currently optimized for ETHUSD (since that is the only cryptocurrency I hold), but it should be pretty easy to add more currencies as well, and is something I am looking to do in the future.

The program features a real-time data visualization tool that displays bid and ask prices, as well as volumes from each exchange. This enables you to rapidly identify market trends and potential price discrepancies between exchanges. 

This software can be a valuable tool for retail crypto traders looking to stay on top of the market and make informed trading decisions. Thank you for checking out my script! Message me at e234chan@uwaterloo.ca if you have any suggestions or questions. Always happy to chat. Enjoy!

Setup:
1. Clone the repo to your local machine by running `git clone <repo URL>`.
2. Create a new virtual environment by running `python3 -m venv crypto_feed_venv` in the root. I am using python 3.11.1 here.
3. Activate the virtual environment by running `source crypto_feed_venv/bin/activate`. 
4. Install the required dependencies by running `pip install -r requirements.txt` in the root.
5. Open up config.json and change line 10 (output_file_path) to your desired file path. The program will create a csv here and read in bid/ask data to it.
6. Run the program from the src directory with `python main.py`. Once it is running, it will be reading real-time top-of-the-book data into the csv. You can run `python view.py` to watch the data in real-time.
7. Deactivate the venv with `deactivate`.

A side note about arbitrage opportunities:
When the blue bid line is above the orange ask line, a theoretical arbitrage opportunity may be present. It is important to note that Kraken often exhibits lower bid and ask values, resulting in numerous theoretical arbitrage opportunities. However, these opportunities might not be viable in practice due to two reasons: first, commission fees are not taken into account, and second, the webhooks used in this program are slower and less reliable compared to methods employed by professional algorithmic traders.
