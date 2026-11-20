
import ifcopenshell

# ==========================================
# 1. LOAD IFC FILE
# ==========================================

ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")

print("IFC file loaded:", ifc_file.schema)


# ==========================================
# 2. FIND ALL STAIRS
# ==========================================

stairs = ifc_file.by_type("IfcStair")

print("\nNumber of stairs:", len(stairs))

for stair in stairs:
    print(stair.GlobalId, stair.Name)


# ==========================================
# 3. FIND ALL SLABS
# ==========================================

slabs = ifc_file.by_type("IfcSlab")

print("\nNumber of slabs:", len(slabs))

for slab in slabs:
    print(slab.GlobalId, slab.Name)


# ==========================================
# 4. RENAME ALL SLABS
# ==========================================

for i, slab in enumerate(slabs, start=1):
    old_name = slab.Name
    slab.Name = f"Renamed_Slab_{i}"

    print(f"Updated slab: {old_name} -> {slab.Name}")


# ==========================================
# 5. PRINT BUILDING STOREYS
# ==========================================

storeys = ifc_file.by_type("IfcBuildingStorey")

print("\nBuilding Storeys:")

for storey in storeys:
    print("Storey:", storey.Name)
    print("Elevation:", storey.Elevation)


# ==========================================
# 6. LIST ALL UNIQUE OBJECT TYPES
# ==========================================

print("\nObject types in file:")

object_types = set()

for element in ifc_file:
    object_types.add(element.is_a())

for object_type in sorted(object_types):
    print(object_type)


# ==========================================
# 7. GET PROJECT NAME
# ==========================================

projects = ifc_file.by_type("IfcProject")

for project in projects:
    print("\nProject Name:", project.Name)


# ==========================================
# 8. SAVE UPDATED IFC FILE
# ==========================================

ifc_file.write("AC20-FZK-Haus_renamed.ifc")

print("\nUpdated IFC file successfully saved!")
