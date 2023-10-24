from collections import OrderedDict


mydict = {}
mydict = OrderedDict()

mydict['first'] = 'firstvalue'
mydict['second'] = 'secondvalue'
mydict['third'] = 'thirdvalue'

mydict.popitem(True)
print(mydict)
