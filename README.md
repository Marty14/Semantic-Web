# 🛡️ CyberSecOnto - Un'Ontologia per la Cybersecurity

**CyberSecOnto** è un'ontologia OWL nel dominio della cybersecurity sviluppata per superare i limiti dei tradizionali database relazionali. Modella le relazioni implicite tra sistemi informatici, vulnerabilità, attacchi e mitigazioni, trasformando un inventario statico in un sistema di analisi automatica del rischio aziendale.

Progetto realizzato per il corso di **Web Reasoning** (Prof.ssa Marianna Nicolosi Asmundo), Università degli Studi di Catania.

---

## 📋 Indice
1. [Caratteristiche e Tecnologie](#caratteristiche-e-tecnologie)
2. [Struttura e File del Progetto](#struttura-e-file-del-progetto)
3. [Come Iniziare](#come-iniziare)

---

## ✨ Caratteristiche e Tecnologie
Il progetto utilizza un ecosistema integrato per l'analisi proattiva del rischio:
* **Modellazione Semantica (OWL):** Tassonomia strutturata per `System`, `Vulnerability`, `Attack` e `Mitigation`. Impiego di restrizioni logiche (`only`, `some`, `exactly 1`) per garantire la consistenza dei dati.
* **Analisi dell'Impatto a Catena:** Utilizzo della proprietà transitiva `dependsOn` per calcolare come la compromissione di un nodo impatti l'intera infrastruttura.
* **Motore Inferenziale Ibrido (SWRL + Python):** Integrazione di Python (`owlready2`) e regole SWRL per superare le limitazioni computazionali nei calcoli matematici (es. valutazione dinamica dei punteggi CVSS).
* **Classificazione Automatica:** Identificazione automatica di `CriticalVulnerability` (CVSS > 8.0) e propagazione del rischio per inferire i `HighRiskSystem`.
* **Interrogazione (SPARQL):** Estrazione di nuova conoscenza e generazione di report automatizzati.

---

## 📂 Struttura e File del Progetto
L'architettura del progetto riflette l'evoluzione dei dati, da scheletro vuoto a ontologia intelligente, gestita tramite script Python.

```text
semantic_web/
├── Untitled.rdf                    # Scheletro OWL iniziale (T-Box, senza individui)
├── cyberseconto_populated.owl      # Dati procedurali generati dallo script (A-Box)
├── cyberseconto_inferred.owl       # Ontologia finale con deduzioni logiche
├── popolamento.py                  # Genera 20 server e 10 CVE (CVSS random 4.0-10.0)
├── apply_swrl_rules.py             # Applica le regole SWRL (Motore ibrido)
├── test_sparql.py                  # Esegue 7 query di test sull'ontologia finale
├── debug_onto.py                   # Utility temporanea di ispezione
├── debug_properties.py             # Utility temporanea di ispezione
└── README.md                       # Questa documentazione
