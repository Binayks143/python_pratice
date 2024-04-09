car={'make':'Honda','model':'city','year':2012}
from exceptions import *

try:
    print(car['color'])
except Exception as e1:
    print('color is not defined',e1)
finally:
    print('done')