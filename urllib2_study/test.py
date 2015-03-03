__author__ = 'xianbing'
from string import maketrans   # Required to call maketrans function.

intab = '<>:"/\|?*'
outtab = "666666666"
trantab = maketrans(intab, outtab)

str = '<>:"/\|?* string example....wow!!!\t';
print str.translate(trantab);
def tran(str):
    intab = '<>:"/\|?*'
    outtab = "666666666"
    trantab = maketrans(intab, outtab)
    return str.translate(trantab)


strs='as<>:"/\|?*'
print tran(strs)