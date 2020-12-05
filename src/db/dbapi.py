from .mysql import m
from .redis import r

print('dhibhibhib')

__all__: ['m', 'r']




# 用法
# insert
# qurey = dbm.insert('user', [('name', 'user2'), ('coin', 300)])
# r = dbm.execute(qurey)

# update
# qurey = dbm.update('user', [('name', 'user3'), ('coin', 200)]) + dbm.where([('id', '=', 1)])
# r = dbm.execute(qurey)

# selete
# query = dbm.select('user') + dbm.where([('id', '>', 1)]) + db.orderDesc('id') + dbm.limit(10,1)
# r = dbm.fetch(query)
# print(query)
# print(r)