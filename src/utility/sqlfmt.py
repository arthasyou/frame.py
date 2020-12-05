from .listfmt import unzip

# "item" => "`item`"
def sqlItem(i):
    return "`" + i + "`"

# ["ites1", "item2"...] => "`item1`, `item2`"
def sqlItems(list):
    return ", ".join([sqlItem(x) for x in list])

def select(items, table):
    if items != "*":
        items = sqlItems(items)
    return "SELECT " + items + " FROM " + sqlItem(table)

def valFormat(v):
    if isinstance(v, str):
        return "'" + v + "'"
    return str(v)

def cItems(items):
    (keys, vals) = unzip(items)
    keyStr = ", ".join([sqlItem(x) for x in keys])
    valStr = ", ".join(valFormat(x) for x in vals)
    return " (" + keyStr + ") VALUES (" + valStr + ")"

def whereItem(i):
    key, op, val = i
    return sqlItem(key) + " " + op + " " + valFormat(val)

def updateItem(i):
    key, val = i
    return sqlItem(key) + " = " + valFormat(val)

def where(list):
    return " WHERE " + " AND ".join([whereItem(x) for x in list])

def whereOr(list):
    return " WHERE " + " OR ".join([whereItem(x) for x in list])

def subAnd(list):
    return " AND " + " AND ".join([whereItem(x) for x in list])

def subOr(list):
    return " OR " + " OR ".join([whereItem(x) for x in list])

def insert(table, items):
    iStr = cItems(items)
    return "INSERT INTO " + sqlItem(table) + iStr

def replace(table, items):
    iStr = cItems(items)
    return "REPLACE INTO " + sqlItem(table) + iStr

def update(table, items):
    return "UPDATE " + sqlItem(table) + " SET " + ", ".join([updateItem(x) for x in items])

def deltet(table):
    "DELETE FROM " + sqlItem(table)

def order(key):
    return " ORDER BY " + sqlItem(key)

def orderDesc(key):
    return " ORDER BY " + sqlItem(key) + " DESC"

def limit(page, column):
    return " LIMIT {}, {}".format(valFormat((page-1) * column), column)
