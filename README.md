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
- **OWL** per la definizione delle classi e proprietà
- **SWRL** per le regole di inferenza
- **SPARQL** per interrogare la base di conoscenza
- **Python + owlready2** per il popolamento e testing automatizzato

---

## File dell'Ontologia

### `Untitled.rdf`
**Tipo:** Ontologia OWL originale (formato RDF/XML)  
**Descrizione:** Questo è il file principale dell'ontologia creato inizialmente con Protégé, sostituito poi con il file `cyberseconto_inferred.owl` sul quale sono state applicate tutte le modifiche necessarie al fine di usarlo come file finale. 

### `cyberseconto_populated.owl`
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
1. Carica `Untitled.rdf`
2. Crea 10 vulnerabilità CVE con punteggi CVSS casuali (4.0 - 10.0)
3. Crea 4 attacchi che sfruttano vulnerabilità casuali
4. Crea 20 server di produzione con vulnerabilità assegnate
5. Aggiunge dipendenze tra alcuni server (per testare la transitività)
6. Salva tutto in `cyberseconto_populated.owl`


apply_swrl_rules.py
Scopo: Applicare manualmente le regole SWRL

**Cosa fa:**

**1.** Carica cyberseconto_populated.owl

**2.** Applica Regola 1 (CriticalVulnerability): Classifica vulnerabilità con CVSS > 8.0

**3.** Applica Regola 2 (HighRiskSystem): Identifica sistemi con vulnerabilità critiche

**4.** Salva risultati in cyberseconto_inferred.owl

**5.** Stampa report dettagliato

**Come usarlo:**
### `python3 apply_swrl_rules.py`
### `test_sparql.py`

**Scopo**: Testare l'ontologia con query SPARQL

Cosa fa: Esegue 7 query SPARQL complete:

**Query 1** - Trova sistemi ad alto rischio (HighRiskSystem)

**Query 2** - Trova vulnerabilità critiche (CVSS > 8.0)

**Query 3** - Lista tutti i sistemi con le loro vulnerabilità

**Query 4** - Mostra attacchi e vulnerabilità sfruttate

**Query 5** - Identifica sistemi potenzialmente attaccabili

**Query 6** - Statistiche distribuzione vulnerabilità per severità

**Query 7** - Mostra dipendenze tra sistemi

Come usarlo:

### Bash
### python3 test_sparql.py
### debug_onto.py e debug_properties.py
Scopo: Script di debug per ispezionare ontologia

Uso: Temporaneo, per sviluppo

Cosa fanno:

**debug_onto.py** - Elenca tutte le classi e individui nell'ontologia

**debug_properties.py** - Elenca tutte le proprietà (object e data)

Come usarli:

Bash
### python3 debug_onto.py
### python3 debug_properties.py

**Come Usare il Progetto**
Setup Iniziale
Installa dipendenze:

Bash
pip3 install owlready2
Verifica Java (per tentativi con reasoner, opzionale):


Bash
java -version
Workflow Completo
**Passo 1: Popolare l'Ontologia**

Bash
python3 popolamento.py
Output: cyberseconto_populated.owl

**Passo 2: Applicare Regole SWRL**

Bash
python3 apply_swrl_rules.py
Output: cyberseconto_inferred.owl

**Passo 3: Testare con Query SPARQL**

Bash
python3 test_sparql.py

**Passo 4: Visualizzare in Protégé**
Apri cyberseconto_inferred.owl in Protégé per la visualizzazione grafica delle inferenze.

Struttura delle Directory
Plaintext
semantic_web/
├── Untitled.rdf                    
├── cyberseconto_populated.owl      
├── cyberseconto_inferred.owl       
├── popolamento.py                  
├── apply_swrl_rules.py            
├── test_sparql.py                
├── debug_onto.py                  
├── debug_properties.py            
└── README.md

