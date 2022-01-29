from itertools import count
from itertools import cycle

m_1 = count(3)
m_2 = cycle('1, 2, 3')

for _ in range (2):
    print('(m_1,m_2): ({}, {})'.format(next(m_1), next(m_2)))

