from owlready2 import *
from owlready2.sparql import *

print("=" * 80)
print("CYBERSECONTO - SPARQL QUERIES TEST")
print("=" * 80)

# caricamento ontologia 
onto_path.append(".")
try:
    onto = get_ontology("cyberseconto_inferred.owl").load()
    print(" Caricata ontologia con inferenze\n")
except:
    onto = get_ontology("cyberseconto_populated.owl").load()
    print(" Caricata ontologia popolata (senza inferenze)\n")


default_world.sparql_query("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    SELECT ?s WHERE { ?s rdf:type owl:Thing } LIMIT 1
""")

# QUERY 1: sistemi ad alto rischio
print("=" * 80)
print("QUERY 1: SISTEMI AD ALTO RISCHIO (HighRiskSystem)")
print("=" * 80)

query1 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?system ?vuln ?cvss
    WHERE {
        ?system rdf:type cyber:HighRiskSystem .
        ?system cyber:hasVulnerability ?vuln .
        ?vuln cyber:hasCVSSScore ?cvss .
    }
    ORDER BY DESC(?cvss)
"""

try:
    results = list(default_world.sparql(query1))
    if results:
        print(f"\nTrovati {len(results)} risultati:")
        for system, vuln, cvss in results:
            system_name = system.name if hasattr(system, 'name') else str(system)
            vuln_name = vuln.name if hasattr(vuln, 'name') else str(vuln)
            print(f"  - Sistema: {system_name}")
            print(f"    Vulnerabilità: {vuln_name} (CVSS: {cvss})")
    else:
        print("\n  Nessun HighRiskSystem trovato (esegui prima il reasoner)")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 2: vulnerabilità critiche (CVSS > 8)
print("\n" + "=" * 80)
print("QUERY 2: VULNERABILITÀ CRITICHE (CVSS > 8.0)")
print("=" * 80)

query2 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    
    SELECT ?vuln ?cvss
    WHERE {
        ?vuln cyber:hasCVSSScore ?cvss .
        FILTER (?cvss > 8.0)
    }
    ORDER BY DESC(?cvss)
"""

try:
    results = list(default_world.sparql(query2))
    print(f"\nTrovate {len(results)} vulnerabilità critiche:")
    for vuln, cvss in results:
        vuln_name = vuln.name if hasattr(vuln, 'name') else str(vuln)
        print(f"  - {vuln_name}: CVSS {cvss}")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 3: sistemi con vulnerabilità e relativi CVSS
print("\n" + "=" * 80)
print("QUERY 3: SISTEMI CON VULNERABILITÀ")
print("=" * 80)

query3 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?system ?vuln ?cvss
    WHERE {
        ?system rdf:type cyber:System .
        ?system cyber:hasVulnerability ?vuln .
        ?vuln cyber:hasCVSSScore ?cvss .
    }
    ORDER BY DESC(?cvss)
"""

try:
    results = list(default_world.sparql(query3))
    print(f"\nTrovati {len(results)} sistemi con vulnerabilità:")
    current_system = None
    for system, vuln, cvss in results[:10]:  
        system_name = system.name if hasattr(system, 'name') else str(system)
        vuln_name = vuln.name if hasattr(vuln, 'name') else str(vuln)
        if system_name != current_system:
            print(f"\n   {system_name}:")
            current_system = system_name
        print(f"    └─ {vuln_name} (CVSS: {cvss})")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 4: attacchi e vulnerabilità sfruttate
print("\n" + "=" * 80)
print("QUERY 4: ATTACCHI E VULNERABILITÀ SFRUTTATE")
print("=" * 80)

query4 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    
    SELECT ?attack ?vuln ?cvss
    WHERE {
        ?attack cyber:exploits ?vuln .
        ?vuln cyber:hasCVSSScore ?cvss .
    }
    ORDER BY DESC(?cvss)
"""

try:
    results = list(default_world.sparql(query4))
    print(f"\nTrovati {len(results)} attacchi:")
    for attack, vuln, cvss in results:
        attack_name = attack.name if hasattr(attack, 'name') else str(attack)
        vuln_name = vuln.name if hasattr(vuln, 'name') else str(vuln)
        print(f"  - Attacco: {attack_name}")
        print(f"    → Sfrutta: {vuln_name} (CVSS: {cvss})")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 5: sistemi potenzialmente attaccabili 
print("\n" + "=" * 80)
print("QUERY 5: SISTEMI POTENZIALMENTE ATTACCABILI")
print("=" * 80)

query5 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT DISTINCT ?system ?attack ?vuln ?cvss
    WHERE {
        ?attack cyber:exploits ?vuln .
        ?system rdf:type cyber:System .
        ?system cyber:hasVulnerability ?vuln .
        ?vuln cyber:hasCVSSScore ?cvss .
    }
    ORDER BY DESC(?cvss)
"""

try:
    results = list(default_world.sparql(query5))
    print(f"\nTrovati {len(results)} sistemi potenzialmente attaccabili:")
    for system, attack, vuln, cvss in results:
        system_name = system.name if hasattr(system, 'name') else str(system)
        attack_name = attack.name if hasattr(attack, 'name') else str(attack)
        vuln_name = vuln.name if hasattr(vuln, 'name') else str(vuln)
        print(f"\n    {system_name}")
        print(f"    Attacco: {attack_name}")
        print(f"    Via: {vuln_name} (CVSS: {cvss})")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 6: statistiche vulnerabilità per Range CVSS
print("\n" + "=" * 80)
print("QUERY 6: STATISTICHE VULNERABILITÀ PER SEVERITÀ")
print("=" * 80)

query6_critical = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    SELECT (COUNT(?v) as ?count)
    WHERE {
        ?v cyber:hasCVSSScore ?cvss .
        FILTER (?cvss >= 9.0)
    }
"""

query6_high = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    SELECT (COUNT(?v) as ?count)
    WHERE {
        ?v cyber:hasCVSSScore ?cvss .
        FILTER (?cvss >= 7.0 && ?cvss < 9.0)
    }
"""

query6_medium = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    SELECT (COUNT(?v) as ?count)
    WHERE {
        ?v cyber:hasCVSSScore ?cvss .
        FILTER (?cvss >= 4.0 && ?cvss < 7.0)
    }
"""

query6_low = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    SELECT (COUNT(?v) as ?count)
    WHERE {
        ?v cyber:hasCVSSScore ?cvss .
        FILTER (?cvss < 4.0)
    }
"""

try:
    critical = list(default_world.sparql(query6_critical))[0][0]
    high = list(default_world.sparql(query6_high))[0][0]
    medium = list(default_world.sparql(query6_medium))[0][0]
    low = list(default_world.sparql(query6_low))[0][0]
    
    total = critical + high + medium + low
    
    print(f"\n Distribuzione Vulnerabilità per Severità (CVSS):")
    print(f"   Critical (9.0-10.0): {critical} ({100*critical//total if total > 0 else 0}%)")
    print(f"   High (7.0-8.9):     {high} ({100*high//total if total > 0 else 0}%)")
    print(f"   Medium (4.0-6.9):   {medium} ({100*medium//total if total > 0 else 0}%)")
    print(f"   Low (0.0-3.9):      {low} ({100*low//total if total > 0 else 0}%)")
    print(f"   TOTALE:             {total}")
except Exception as e:
    print(f" Errore: {e}")

# QUERY 7: dipendenze tra sistemi (Transitività)
print("\n" + "=" * 80)
print("QUERY 7: DIPENDENZE TRA SISTEMI")
print("=" * 80)

query7 = """
    PREFIX cyber: <http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#>
    
    SELECT ?system ?depends
    WHERE {
        ?system cyber:dependsOn ?depends .
    }
"""

try:
    results = list(default_world.sparql(query7))
    if results:
        print(f"\nTrovate {len(results)} dipendenze:")
        for system, depends in results:
            system_name = system.name if hasattr(system, 'name') else str(system)
            depends_name = depends.name if hasattr(depends, 'name') else str(depends)
            print(f"  - {system_name} → dipende da → {depends_name}")
    else:
        print("\n  Nessuna dipendenza trovata")
except Exception as e:
    print(f" Errore: {e}")

print("\n" + "=" * 80)
print(" TUTTE LE QUERY COMPLETATE")
print("=" * 80)
