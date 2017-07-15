#!/usr/bin/python

import Image
import numpy as np

im = Image.open('maxresdefault.jpg')

r, g, b = np.array(im).T
for i in range(1,11):
	
	print i
	r = r * i
	g*=i
	b*=i

	im = Image.fromarray(np.dstack([item.T for item in (r,g,b)]))

	im.save(str(i)+'.png')
