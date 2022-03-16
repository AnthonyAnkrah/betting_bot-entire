import engine as en
from pprint import pprint as pp

leagues = ['SP1', 'D1', 'E0', 'I1']
data = en.get_historical(leagues)
pp(data)