import plotly.express as px  # type: ignore

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]


max_result = die_1.num_sizes + die_2.num_sizes
poss_results = range(2, max_result + 1)

frequencies = [results.count(value) for value in poss_results]

title = "2個の6面サイコロを1,000回転がした結果"
labels = {"x": "結果", "y": "発生した回数"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
