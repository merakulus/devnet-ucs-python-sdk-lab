from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "admin", "password")

from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

vlans = handle.query_classid("FabricVlan")

for vlan_mo in vlans:
    print(vlan_mo)
    if vlan_mo.id != "1":
        handle.remove_mo(vlan_mo)

## Remove All VLAN Except for VLAN 1


handle.commit()


