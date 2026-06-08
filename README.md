# 🛡️ CyberSecOnto - Un'Ontologia per la Cybersecurity

**CyberSecOnto** è un'ontologia OWL nel dominio della cybersecurity sviluppata per superare i limiti dei tradizionali database relazionali. Modella le relazioni implicite tra sistemi informatici, vulnerabilità, attacchi e mitigazioni, trasformando un inventario statico in un sistema di analisi automatica del rischio aziendale.

Progetto realizzato per il corso di **Web Reasoning** (Prof.ssa Marianna Nicolosi Asmundo), Università degli Studi di Catania.

---

## 📋 Indice
1. [Panoramica delle Tecnologie](#panoramica-delle-tecnologie)
2. [Struttura delle Directory](#struttura-delle-directory)
3. [File dell'Ontologia](#file-dellontologia)
4. [Script Python e Automazione](#script-python-e-automazione)
5. [Come Usare il Progetto](#come-usare-il-progetto)

---

## Panoramica delle Tecnologie
Il progetto utilizza un ecosistema integrato:
* **OWL:** per la definizione strutturata delle classi, proprietà e restrizioni (T-Box).
* **SWRL:** per le regole di inferenza (es. calcoli matematici sui punteggi).
* **SPARQL:** per interrogare la base di conoscenza e generare report.
* **Python + owlready2:** per il popolamento procedurale e il testing automatizzato.

---

## Struttura delle Directory

```text
semantic_web/
├── Untitled.rdf                    # Scheletro vuoto iniziale
├── cyberseconto_populated.owl      # Dati generati (A-Box)
├── cyberseconto_inferred.owl       # Ontologia finale con inferenze
├── popolamento.py                  # Script di generazione dati
├── apply_swrl_rules.py             # Motore inferenziale SWRL
├── test_sparql.py                  # Suite di query
├── debug_onto.py                   # Utility di ispezione
├── debug_properties.py             # Utility di ispezione
└── README.md                       # Questa documentazione



# 🛡️ CyberSecOnto: Un'Ontologia per la Cybersecurity
**CyberSecOnto** è un progetto accademico basato sulle tecnologie del Web Semantico, sviluppato per superare i limiti dei tradizionali database relazionali nella gestione della sicurezza informatica.Trasforma un inventario statico di asset in un **sistema di analisi proattiva del rischio**, capace di dedurre automaticamente le minacce sfruttando regole logiche e inferenziali.

Progetto realizzato per il corso di **Web Reasoning** (Prof.ssa Marianna Nicolosi Asmundo), Università degli Studi di Catania.

---

## ✨ Caratteristiche Principali

* **Modellazione Semantica (OWL):** Tassonomia strutturata per `System`, `Vulnerability`, `Attack` e `Mitigation`.
* **Analisi dell'Impatto a Catena:** Utilizzo della proprietà transitiva `dependsOn` per calcolare come la compromissione di un nodo impatti l'intera infrastruttura.
* **Motore Inferenziale Ibrido:** Integrazione di Python (`owlready2`) e regole SWRL per superare le limitazioni computazionali dei reasoner grafici nei calcoli matematici (es. valutazione dinamica dei punteggi CVSS).
* **Classificazione Automatica (Reasoning):** Identificazione automatica di `CriticalVulnerability` (CVSS > 8.0) e propagazione del rischio per inferire i `HighRiskSystem`.
* **Validazione Logica:** Impiego di restrizioni universali (`only`), esistenziali (`some`) e di cardinalità (`exactly 1`) per garantire la consistenza formale dei dati.

---

## 📂 Struttura del Progetto

Il progetto è suddiviso in tre fasi, rappresentate dall'evoluzione dei file ontologici e governate dagli script Python:

### 1. I File Ontologici
* `Untitled.rdf`: Lo scheletro iniziale (T-Box) contenente classi e proprietà, privo di individui.
* `cyberseconto_populated.owl`: L'ontologia popolata proceduralmente (A-Box) con l'infrastruttura di test.
* `cyberseconto_inferred.owl`: L'artefatto finale, indipendente e interrogabile, contenente i dati e tutte le inferenze logiche materializzate.

### 2. Gli Script di Automazione (Python)
* `popolamento.py`: Simula uno scenario Enterprise reale. Genera dinamicamente 20 server e 10 vulnerabilità CVE con punteggi CVSS randomizzati (4.0 - 10.0), assegnandoli ai sistemi.
* `apply_swrl_rules.py`: Il motore ibrido. Applica le regole SWRL per classificare le vulnerabilità critiche e i sistemi ad alto rischio, salvando l'output finale.
* `test_sparql.py`: Suite di interrogazioni per validare la conoscenza dedotta dal sistema.
* `debug_onto.py` / `debug_properties.py`: Utility per l'ispezione della struttura.

---


## 🚀 Come Iniziare

### Prerequisiti
Assicurati di avere Python 3 installato. Per installare la libreria necessaria all'interazione con l'ontologia, esegui:
```bash
pip install owlready2# Semantic-Web
