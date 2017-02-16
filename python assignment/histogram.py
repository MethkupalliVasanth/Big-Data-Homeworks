from __future__ import division, print_function
import numpy as np
import pandas as pd
import pygal as pg
data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')
ages = [int(x) for x in data['Cited Person Age'] if x < 100]
age = list()
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)
for x in range(min_age, max_age):
	w = 0
	for y in ages:
		if x == y:
			w = w + 1
	t = w, x, x + 1
	age.append(t)
lc = pg.Histogram()
lc.title = 'Age histogram'
lc.add('age', age)
lc.render_in_browser()
