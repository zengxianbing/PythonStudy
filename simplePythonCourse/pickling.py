__author__ = 'xianbing'

shoplistfile='shoplist.data'

shoplist=['apple','mango','carrot']

f=file(shoplist,'w')
p.dump(shoplist,f)
f.close()



del shoplist

f=file(shoplist)
storedlist=p.load(f)
print(storedlist)
