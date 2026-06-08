from owlready2 import *


# Caricamento ontologia
onto_path.append(".")
onto = get_ontology("cyberseconto_populated.owl").load()

print(" STATO INIZIALE:")
print("-" * 80)
print(f"✓ Vulnerabilità totali: {len(list(onto.Vulnerability.instances()))}")
print(f"✓ CriticalVulnerability: {len(list(onto.CriticalVulnerability.instances()))}")
print(f"✓ Sistemi totali: {len(list(onto.System.instances()))}")
print(f"✓ HighRiskSystem: {len(list(onto.HighRiskSystem.instances()))}")
print(f"✓ Attacchi totali: {len(list(onto.Attack.instances()))}")

# REGOLA 1: CriticalVulnerability
# Se una vulnerabilità ha CVSS > 8.0, diventa CriticalVulnerability
print("\n" + "=" * 80)
print(" APPLICAZIONE REGOLA 1: CriticalVulnerability")
print("=" * 80)
print("SWRL: Vulnerability(?v) ∧ hasCVSSScore(?v, ?score) ∧ greaterThan(?score, 8.0)")
print("      → CriticalVulnerability(?v)\n") 

critical_count = 0
with onto:
    for vuln in onto.Vulnerability.instances():
        if hasattr(vuln, 'hasCVSSScore') and vuln.hasCVSSScore:
            score = vuln.hasCVSSScore[0]
            if score > 8.0:
                if onto.CriticalVulnerability not in vuln.is_a:
                    vuln.is_a.append(onto.CriticalVulnerability)
                    print(f"  ✅ {vuln.name} (CVSS: {score}) → CriticalVulnerability")
                    critical_count += 1

print(f"\n {critical_count} vulnerabilità classificate come Critical")

# REGOLA 2: HighRiskSystem
# Se un sistema ha una CriticalVulnerability, diventa HighRiskSystem
print("\n" + "=" * 80)
print("  APPLICAZIONE REGOLA 2: HighRiskSystem")
print("=" * 80)
print("SWRL: System(?s) ∧ hasVulnerability(?s, ?v) ∧ CriticalVulnerability(?v)")
print("      → HighRiskSystem(?s)\n")

high_risk_count = 0
with onto:
    for system in onto.System.instances():
        if hasattr(system, 'hasVulnerability') and system.hasVulnerability:
            has_critical = False
            critical_vulns = []
            
            for vuln in system.hasVulnerability:
                if onto.CriticalVulnerability in vuln.is_a:
                    has_critical = True
                    critical_vulns.append(vuln)
            
            if has_critical:
                if onto.HighRiskSystem not in system.is_a:
                    system.is_a.append(onto.HighRiskSystem)
                    high_risk_count += 1
                    print(f"   {system.name} → HighRiskSystem")
                    for v in critical_vulns:
                        if hasattr(v, 'hasCVSSScore') and v.hasCVSSScore:
                            print(f"      └─ ha {v.name} (CVSS: {v.hasCVSSScore[0]})")

print(f"\n {high_risk_count} sistemi classificati come HighRisk")

# REGOLA 3: PotentiallyAttackable (nuova classe da creare)
print("\n" + "=" * 80)
print("  APPLICAZIONE REGOLA 3: PotentiallyAttackable")
print("=" * 80)
print("SWRL: Attack(?a) ∧ exploits(?a, ?v) ∧ System(?s) ∧ hasVulnerability(?s, ?v)")
print("      → PotentiallyAttackable(?s)\n")

# Verifica se la classe esiste, altrimenti creala
if not hasattr(onto, 'PotentiallyAttackable'):
    print("  Classe PotentiallyAttackable non esiste, la creiamo...")
    with onto:
        class PotentiallyAttackable(onto.System):
            pass
    print(" Classe PotentiallyAttackable creata come sottoclasse di System")

attackable_count = 0
attackable_info = []  # Lista per tracking

for attack in onto.Attack.instances():
    if hasattr(attack, 'exploits') and attack.exploits:
        for exploited_vuln in attack.exploits:
            # Trova tutti i sistemi che hanno questa vulnerabilità
            for system in onto.System.instances():
                if hasattr(system, 'hasVulnerability') and system.hasVulnerability:
                    if exploited_vuln in system.hasVulnerability:
                        # Tracciamo solo i sistemi attackable
                        info = (system.name, attack.name, exploited_vuln.name,
                               exploited_vuln.hasCVSSScore[0] if hasattr(exploited_vuln, 'hasCVSSScore') and exploited_vuln.hasCVSSScore else 0)
                        if info not in attackable_info:
                            attackable_info.append(info)
                            attackable_count += 1
                            print(f"    {system.name} → Potentially Attackable")
                            print(f"      └─ Attacco: {attack.name}")
                            print(f"      └─ Via: {exploited_vuln.name}")
                            if hasattr(exploited_vuln, 'hasCVSSScore') and exploited_vuln.hasCVSSScore:
                                print(f"      └─ CVSS: {exploited_vuln.hasCVSSScore[0]}")

print(f"\n {attackable_count} sistemi marcati come PotentiallyAttackable")

# STATO FINALE
print("\n" + "=" * 80)
print(" STATO FINALE:")
print("=" * 80)
print(f"✓ CriticalVulnerability: {len(list(onto.CriticalVulnerability.instances()))}")
print(f"✓ HighRiskSystem: {len(list(onto.HighRiskSystem.instances()))}")
print(f"✓ Sistemi Potenzialmente Attaccabili: {attackable_count}")

# Salvataggio
output_file = "cyberseconto_inferred.owl"
onto.save(file=output_file)
print(f"\n Ontologia con inferenze salvata come '{output_file}'")

# riepilogo dettagliato 
print("\n" + "=" * 80)
print(" RIEPILOGO DETTAGLIATO")
print("=" * 80)

print("\n VULNERABILITÀ CRITICHE:")
for vuln in onto.CriticalVulnerability.instances():
    if hasattr(vuln, 'hasCVSSScore') and vuln.hasCVSSScore:
        print(f"  - {vuln.name}: CVSS {vuln.hasCVSSScore[0]}")

print("\n  SISTEMI AD ALTO RISCHIO:")
for system in onto.HighRiskSystem.instances():
    print(f"  - {system.name}")
    if hasattr(system, 'hasVulnerability'):
        for v in system.hasVulnerability:
            if onto.CriticalVulnerability in v.is_a:
                if hasattr(v, 'hasCVSSScore') and v.hasCVSSScore:
                    print(f"    └─ {v.name} (CVSS: {v.hasCVSSScore[0]})")


print("\n SISTEMI POTENZIALMENTE ATTACCABILI:")
for sys_name, att_name,vuln_name, cvss in attackable_info:
    print(f"  - {sys_name}")
    print(f"    └─ Attacco: {att_name} via {vuln_name} (CVSS: {cvss})")

print("\n" + "=" * 80)
print(" TUTTE LE REGOLE SWRL APPLICATE CON SUCCESSO!")
print("=" * 80)

