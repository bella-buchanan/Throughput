from Throughput_public import *
def TP(filename):
    t = Throughput(filename)
    print(filename + ': %.3f bits/s' % t.calThroughput())
    # calculate throughput for each of the following JSON files:
    TP('Ammara iPad .json')
    TP('Khadijah_ipad.json')
    TP('Mou_ipad.json')
    TP('Niat_ipad.json')
    TP('Ricardo_ipad.json')
    TP('Tess iPad.json')
    TP('Vanessa_ipad.json')
    TP('Yidan_ipad.json')