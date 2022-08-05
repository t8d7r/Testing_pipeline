from suzieq.sqobjects import get_sqobject

devices = get_sqobject('device')().get(status="dead").hostname
for hostname in devices:
        print (hostname)
assert devices.empty
