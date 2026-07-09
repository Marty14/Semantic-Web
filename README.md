# 🛡️ CyberSecOnto - Documentazione del Progetto

**CyberSecOnto** è un'ontologia OWL nel dominio della cybersecurity che modella le relazioni tra sistemi informatici, vulnerabilità, attacchi e mitigazioni. Progetto realizzato per il corso di **Web Reasoning** (Prof.ssa Marianna Nicolosi Asmundo), Università degli Studi di Catania.

---

## 📋 Indice
1. [Panoramica](#panoramica)
2. [File dell'Ontologia](#file-dellontologia)
3. [Script Python](#script-python)
4. [Come Usare il Progetto](#come-usare-il-progetto)
5. [Struttura delle Directory](#struttura-delle-directory)

---

## Panoramica

Il progetto utilizza un ecosistema di tecnologie integrate:
- **OWL** per la definizione di un dominio espanso a 58 classi e proprietà logiche avanzate (transitive, simmetriche, asimmetriche e inverse)
- **SWRL** per le regole di inferenza
- **SPARQL** per interrogare la base di conoscenza
- **Python + owlready2** per il popolamento e testing automatizzato

---

## File dell'Ontologia

### `Untitled_2.rdf`
**Tipo:** Ontologia OWL originale (formato RDF/XML)  
**Descrizione:** Questo è il file principale dell'ontologia creato inizialmente con Protégé, sostituito poi con il file `cyberseconto_inferred.owl` sul quale sono state applicate tutte le modifiche necessarie al fine di usarlo come file finale. 

### `cyberseconto_populated_2.owl`
**Tipo:** Ontologia popolata con dati di test  
**Descrizione:** Versione dell'ontologia dopo l'esecuzione di `popolamento.py`. 

### `cyberseconto_inferred.owl`
**Tipo:** Ontologia con inferenze applicate  
**Generato da:** `apply_swrl_rules.py`

---

## Script Python

### `popolamento.py`
**Scopo:** Popolare l'ontologia con dati di test  

**Cosa fa:**
1. Carica `Untitled_2.rdf`
2. Crea 10 vulnerabilità CVE con punteggi CVSS casuali (4.0 - 10.0)
3. Crea 4 attacchi che sfruttano vulnerabilità casuali
4. Crea 20 server di produzione con vulnerabilità assegnate
5. Aggiunge dipendenze tra alcuni server (per testare la transitività)
6. Salva tutto in `cyberseconto_populated_2.owl`

### `apply_swrl_rules.py`
**Scopo:** Applicare manualmente le regole SWRL

**Cosa fa:**
**1.** Carica `cyberseconto_populated_2.owl`
**2.** Applica Regola 1 (CriticalVulnerability): Classifica vulnerabilità con CVSS > 8.0
**3.** Applica Regola 2 (HighRiskSystem): Identifica sistemi con vulnerabilità critiche
**4.** Salva risultati in `cyberseconto_inferred.owl`
**5.** Stampa report dettagliato

**Come usarlo:**
```bash
python3 apply_swrl_rules.py
