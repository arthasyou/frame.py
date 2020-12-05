# 字典分解成2个数组
# {'key1':'val1', 'key2':'val2'...} => (['key1', 'key2'...],['val1','val2'...]) 
def dictSplit(d):
    keys = []
    vals = []
    for k, v in d.items():
        keys.append(k)
        vals.append(v)
    return (keys, vals)

# 2元元组数组解压
# [(a1, b1), (a2, b2)...] => ([a1, a2...], [b1,b2...])
def unzip(list):
    list1 = []
    list2 = []
    for a,b in list:
        list1.append(a)
        list2.append(b)
    return (list1, list2)

# 3元元组数组解压
# [(a1, b1, c1), (a2, b2, c2)...] => ([a1, a2...], [b1,b2...], [c1, c2...])
def unzip3(list):
    list1 = []
    list2 = []
    list3 = []
    for a,b,c in list:
        list1.append(a)
        list2.append(b)
        list3.append(c)
    return (list1, list2, list3)