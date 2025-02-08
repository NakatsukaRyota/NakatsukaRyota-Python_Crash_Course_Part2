import plotly.express as px  # type: ignore

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sizes * die_2.num_sizes
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "2個の6面サイコロを1,000回転がした結果"
labels = {"x": "結果", "y": "発生した回数"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
