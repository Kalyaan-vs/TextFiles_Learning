# import json
#
# json_data_source = "temperature_anomaly.json"
#
# with open(json_data_source, encoding="utf-8" ) as data:
#     anomalies = json.load(data)
# # print(anomalies["description"])
# # print(anomalies["data"].items())
#
#
# for year, value in anomalies["data"].items():
#     # print(type(year), type(value))
#     year, value = int(year), float(value)
#     # print(type(year), type(value))
#     print(f"{year}....{value:6.2f}")

import json
import urllib.request

json_data_source = ("https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg"
                    "/land_ocean/1/12/1850-2024/data.json")

# with open(json_data_source, encoding="utf-8") as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalies = json.loads(data)
print(anomalies)
print(anomalies["description"])
print(anomalies["data"].items())


for year, value in anomalies["data"].items():
    # print(type(year), type(value))
    year = int(year)
    values = float(value["anomaly"])
    # print(type(year), type(value))
    print(f"{year}....{values:6.2f}")
