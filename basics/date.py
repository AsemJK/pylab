import datetime


ns = '2025-09-06'
print(repr(ns))

dt = datetime.datetime.fromisoformat(ns)
print(dt)
print(repr(dt))
