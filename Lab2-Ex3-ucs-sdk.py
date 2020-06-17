from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "admin", "password")

from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

lan_cloud = handle.query_classid("FabricLanCloud")

# vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan100", id="100")
# handle.add_mo(vlan_mo, True)

vlans = ["200", "201", "202"]

for vlan in vlans:
    vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan"+vlan, id=vlan)
    handle.add_mo(vlan_mo, True)

handle.commit()


