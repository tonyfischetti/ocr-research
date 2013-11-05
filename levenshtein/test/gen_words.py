#!/usr/bin/env python -tt

import levenshteintest as lt

a_list = lt.mutate_string("cat", 300, .7)

a_list = [item for item in a_list if len(item) == 3]

x_ax = []
y_ax = []
z_ax = []


for item in a_list:
    x_ax.append(ord(item[0]))

for item in a_list:
    y_ax.append(ord(item[1]))

for item in a_list:
    z_ax.append(ord(item[2]))

print x_ax
print 
print y_ax
print
print z_ax

