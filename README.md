# 🛡️ CyberSecOnto: Un'Ontologia per la Cybersecurity

[cite_start]**CyberSecOnto** è un progetto accademico basato sulle tecnologie del Web Semantico, sviluppato per superare i limiti dei tradizionali database relazionali nella gestione della sicurezza informatica[cite: 200, 201, 214]. [cite_start]Trasforma un inventario statico di asset in un **sistema di analisi proattiva del rischio**, capace di dedurre automaticamente le minacce sfruttando regole logiche e inferenziali[cite: 218, 355].

[cite_start]Progetto realizzato per il corso di **Web Reasoning** (Prof.ssa Marianna Nicolosi Asmundo), Università degli Studi di Catania[cite: 205, 206, 207, 208].

---

## ✨ Caratteristiche Principali

* [cite_start]**Modellazione Semantica (OWL):** Tassonomia strutturata per `System`, `Vulnerability`, `Attack` e `Mitigation`[cite: 231, 232, 233, 234].
* [cite_start]**Analisi dell'Impatto a Catena:** Utilizzo della proprietà transitiva `dependsOn` per calcolare come la compromissione di un nodo impatti l'intera infrastruttura[cite: 246, 247, 248].
* [cite_start]**Motore Inferenziale Ibrido:** Integrazione di Python (`owlready2`) e regole SWRL per superare le limitazioni computazionali dei reasoner grafici nei calcoli matematici (es. valutazione dinamica dei punteggi CVSS)[cite: 305, 316].
* [cite_start]**Classificazione Automatica (Reasoning):** Identificazione automatica di `CriticalVulnerability` (CVSS > 8.0) e propagazione del rischio per inferire i `HighRiskSystem`[cite: 279, 283, 284].
* [cite_start]**Validazione Logica:** Impiego di restrizioni universali (`only`), esistenziali (`some`) e di cardinalità (`exactly 1`) per garantire la consistenza formale dei dati[cite: 254, 255, 261, 266].

---

## 📂 Struttura del Progetto

[cite_start]Il progetto è suddiviso in tre fasi, rappresentate dall'evoluzione dei file ontologici e governate dagli script Python[cite: 50]:

### 1. I File Ontologici
* [cite_start]`Untitled.rdf`: Lo scheletro iniziale (T-Box) contenente classi e proprietà, privo di individui[cite: 51, 309].
* [cite_start]`cyberseconto_populated.owl`: L'ontologia popolata proceduralmente (A-Box) con l'infrastruttura di test[cite: 53, 314].
* [cite_start]`cyberseconto_inferred.owl`: L'artefatto finale, indipendente e interrogabile, contenente i dati e tutte le inferenze logiche materializzate[cite: 55, 318, 319].

### 2. Gli Script di Automazione (Python)
* `popolamento.py`: Simula uno scenario Enterprise reale. [cite_start]Genera dinamicamente 20 server e 10 vulnerabilità CVE con punteggi CVSS randomizzati (4.0 - 10.0), assegnandoli ai sistemi[cite: 63, 66, 68, 69].
* `apply_swrl_rules.py`: Il motore ibrido. [cite_start]Applica le regole SWRL per classificare le vulnerabilità critiche e i sistemi ad alto rischio, salvando l'output finale[cite: 54, 317].
* [cite_start]`test_sparql.py`: Suite di interrogazioni per validare la conoscenza dedotta dal sistema[cite: 302, 323].
* [cite_start]`debug_onto.py` / `debug_properties.py`: Utility per l'ispezione della struttura[cite: 302].

---

## 🚀 Come Iniziare

### Prerequisiti
Assicurati di avere Python 3 installato. Per installare la libreria necessaria all'interazione con l'ontologia, esegui:
```bash
pip install owlready2# Semantic-Web
