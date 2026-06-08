from owlready2 import *

# Carica l'ontologia
onto_path.append(".")
onto = get_ontology("Untitled.rdf").load()

print("=" * 60)
print("PROPRIETÀ OBJECT NELL'ONTOLOGIA:")
print("=" * 60)

for prop in onto.object_properties():
    print(f"✓ {prop.name}")
    print(f"  IRI: {prop.iri}")
    if prop.domain:
        print(f"  Domain: {[d.name for d in prop.domain]}")
    if prop.range:
        print(f"  Range: {[r.name for r in prop.range]}")
    print()

print("=" * 60)
print("PROPRIETÀ DATA NELL'ONTOLOGIA:")
print("=" * 60)

for prop in onto.data_properties():
    print(f"✓ {prop.name}")
    print(f"  IRI: {prop.iri}")
    if prop.domain:
        print(f"  Domain: {[d.name for d in prop.domain]}")
    if prop.range:
        print(f"  Range: {prop.range}")
    print()
