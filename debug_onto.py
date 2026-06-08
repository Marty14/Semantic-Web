from owlready2 import *

# Carica l'ontologia
onto_path.append(".")
onto = get_ontology("Untitled.rdf").load()

print("=" * 60)
print("CLASSI NELL'ONTOLOGIA:")
print("=" * 60)

# Lista tutte le classi
for cls in onto.classes():
    print(f"✓ {cls.name}")
    print(f"  IRI: {cls.iri}")
    print()

print("=" * 60)
print("VERIFICA ACCESSO AttackType:")
print("=" * 60)

print(f"onto.AttackType = {onto.AttackType}")
print(f"type(onto.AttackType) = {type(onto.AttackType)}")

attack_class = onto.search_one(iri="*AttackType")
print(f"search_one AttackType = {attack_class}")

# Lista  individui
print("\n" + "=" * 60)
print("INDIVIDUI ESISTENTI:")
print("=" * 60)
for ind in onto.individuals():
    print(f"  - {ind.name} (tipo: {ind.is_a})")
