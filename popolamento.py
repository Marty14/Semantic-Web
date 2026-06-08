from owlready2 import *
import random

input_file = "Untitled.rdf"
output_file = "cyberseconto_populated.owl"
base_iri = "http://www.semanticweb.org/salvleanza/ontologies/cybersOnto#"

onto_path.append(".")
try:
    onto = get_ontology(input_file).load()
    print(" Ontologia caricata!")
except:
    print(f" Errore: Non trovo '{input_file}'.")
    exit()

with onto:
    print("  Generazione dati in corso...")

    # creo vunlnerabilità 
    vulns = []
    for i in range(1, 11): 
        v_name = f"CVE_2025_{1000+i}"
        new_v = onto.Vulnerability(v_name)
        
        # assegnazione cve random ( > 8 per testare vulnerabilità) 
        score = round(random.uniform(4.0, 10.0), 1)
        new_v.hasCVSSScore.append(score)
        
        vulns.append(new_v)
        print(f"  -> Vuln: {v_name} (Score: {score})")

    # creazione attacchi 
    attacks = []
    attack_names = ["WannaCry", "Log4Shell_Exploit", "Phishing_Campaign", "DDoS_Botnet"]
    
    for i, name in enumerate(attack_names):
        # Istanziamo la classe Attack
        new_attack = onto.Attack(f"{name}_{i}")
        
        # L'attacco sfrutta una vulnerabilità a caso
        target_vuln = random.choice(vulns)
        new_attack.exploits.append(target_vuln)
        
        attacks.append(new_attack)
        print(f"  -> Attack: {new_attack.name} exploits {target_vuln.name}")

    # creazione sistemi
    for i in range(1, 21): # 20 Sistemi
        s_name = f"Server_Production_{i}"
        new_sys = onto.Server(s_name)
        
        # assegnazione vulnerabilità 
        my_vuln = random.choice(vulns)
        new_sys.hasVulnerability.append(my_vuln)
        
        # Transitività (opzionale, per fare scena)
        if i > 1 and i < 5:
             prev_sys = onto.search_one(iri = f"*{base_iri}Server_Production_{i-1}")
             if prev_sys:
                 new_sys.dependsOn.append(prev_sys)

    print(" Popolamento completato.")
    onto.save(file=output_file)
    print(f" File salvato come '{output_file}'.")