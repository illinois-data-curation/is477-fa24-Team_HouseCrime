import os
import pandas as pd
import logging
import time
from dotenv import load_dotenv
from sodapy import Socrata
from requests.exceptions import ReadTimeout

load_dotenv()
app_token = os.getenv("APP_TOKEN")

client = Socrata("data.cityofchicago.org", app_token, timeout=30)  

limit = 50000
offset = 0
all_data = []

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


max_retries = 5
retry_count = 0  

while True:
    try:
        results = client.get("ijzp-q8t2", limit=limit, offset=offset)
        if not results:
            break

        all_data.extend(results)
        offset += limit

        logging.info(f"Fetched {len(results)} records. Total records fetched: {len(all_data)}.")

        retry_count = 0

    except ReadTimeout:
        retry_count += 1
        logging.warning(f"Timeout occurred. Retrying {retry_count}/{max_retries}...")

        if retry_count >= max_retries:
            logging.error("Max retries reached. Exiting...")
            break

        time.sleep(1)

df = pd.DataFrame.from_records(all_data)

df.to_json("Crimes_2001_to_Present.json", orient="records")
df.to_csv("Crimes_2001_to_Present.csv", index=False)

logging.info("Data collection completed and saved to files.")

