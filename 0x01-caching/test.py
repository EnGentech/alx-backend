from collections import OrderedDict


mydict = {}
mydict = OrderedDict()

mydict['first'] = 'firstvalue'
mydict['second'] = 'secondvalue'
mydict['third'] = 'thirdvalue'

lastValue = list(mydict.keys())[-1]
print(mydict.keys())
