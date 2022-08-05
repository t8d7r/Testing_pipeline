from suzieq.sqobjects import get_sqobject

vlans = get_sqobject('vlan')().get(state="active", vlan = 11).vlanName
assert not vlans.empty
