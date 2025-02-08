import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


# 最高気温と最低気温を取得する
def get_weather_date(path, dates, highs, lows):
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)
    index_low = header_row.index("TMIN")
    index_high = header_row.index("TMAX")
    index_date = header_row.index("DATE")

    for row in reader:
        current_date = datetime.strptime(row[index_date], "%Y-%m-%d")
        high = int(row[index_high])
        low = int(row[index_low])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# 地点の名前を取得する
def get_name(path):
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    for index, column_name in enumerate(header_row):
        if column_name == "NAME":
            index_name = index

    name = next(reader)[index_name]
    return name


dates, highs, lows = [], [], []
path = Path("weather_data/sitka_weather_2021_simple.csv")
name = get_name(path)
get_weather_date(path, dates, highs, lows)
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title(f"Daily High and Low Temperatures, 2021\n{name}", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
