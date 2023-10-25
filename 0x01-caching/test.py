from collections import OrderedDict


mydict = {}
mydict = OrderedDict()

mydict['first'] = 'firstvalue'
mydict['second'] = 'secondvalue'
mydict['third'] = 'thirdvalue'

mydict.move_to_end('first', last=True)
print(mydict.popitem(False))

