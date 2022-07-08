import requests
import json
import pandas as pd

project = "reddit"

resp = requests.get(f"https://legacy-api.arpa.li/{project}/stats.json")

resp_json = resp.json()

# dict_keys(['total_items', 'counts', 'downloaders', 'domain_bytes', 'downloader_bytes', 'downloader_count', 'total_items_done', 'total_items_todo', 'total_items_out'])

data_bytes = [{"name": user, "bytes": resp_json["downloader_bytes"][user]} for user in resp_json["downloader_bytes"]]
data_count = [{"name": user, "count": resp_json["downloader_count"][user]} for user in resp_json["downloader_count"]]


df_bytes = pd.DataFrame(data_bytes)
df_count = pd.DataFrame(data_count)

df_downloaders = df_bytes.merge(df_count, on="name")

df_downloaders.sort_values("bytes", ascending=False)