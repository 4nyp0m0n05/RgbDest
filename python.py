#!/usr/bin/python

import Image
import numpy as np
from random import randint
im = Image.open('maxresdefault.jpg')

r, g, b = np.array(im).T
for i in range(1,11):
	t=randint(1,10)
	print t
	r = (b + g) * t
	g*=t
	b*=t

	im = Image.fromarray(np.dstack([item.T for item in (r,g,b)]))

	im.save(str(i)+'.png')
