# Standards Crosswalk

| Scope Element | CSF 2.0 Outcome (exact text + page) | ZTA Tenet (exact text + page) | ISO 27001 Theme | Evidence Pointer (repo) |
|--------------|--------------------------------------|-------------------------------|------------------|--------------------------|
| One-step analysis script that reads a small sample dataset and prints a simple metric (for example, count of failed events). | **DE.AE-02 –** “Potentially adverse events are analyzed to better understand associated activities.” (NIST CSF 2.0, p.51) | **Tenet 7 –** “The enterprise collects as much information as possible about the current state of assets, network infrastructure and communications and uses it to improve its security posture.” (NIST SP 800-207, p.6) | Technological | `src/analyze_dataset.py`, `data/sample_data.csv` |
| Run logs folder that documents each script execution, including date, command, input file, and key results. | **RS.AN-07 –** “Incident data and metadata are collected, and their integrity and provenance are preserved.” (NIST CSF 2.0, p.59) | **Tenet 5 –** “The enterprise monitors and measures the integrity and security posture of all owned and associated assets.” (NIST SP 800-207, p.6) | Organizational | `docs/run_logs/run1.md`, `docs/run_logs/README.md` |
| Containerized analysis environment defined in a Dockerfile so the script always runs with the same dependencies and configuration. | **PR.PS-01 –** “Configuration management practices are established and applied.” (NIST CSF 2.0, p.43) | **Tenet 2 –** “All communication is secured regardless of network location.” (NIST SP 800-207, p.5) | Technological | `Dockerfile`, `docs/container_instructions.md` |

---

## Rationale (Row 1 – One-step analysis script)

The one-step analysis script aids me in transforming unprocessed data into repeatable and relevant results for this projct. Rather than manually examining a log or dataset to determine what is important, the script consistently processes the data and generates a straightforward metric that I can refer to or compare between runs. This supports the CSF DE.AE-02 Outcome since I'm conducting a systematic and consistent analysis of potentially significant occurrences, even if they are fictitious. Additionally, it is consistent with Zero Trust Tenet 7 since I am consciously gathering data about the "state" of my data, analyzing the findings, and applying them to improve my comprehension of my ability to spot patterns. Despite the tiny size of the project, the script establishes a strong basis for dependable, repeatable analysis.

## Rationale (Row 2 – Run logs folder)

The run logs are crucial because they provide a detailed account of every instance in which my analysis script was executed. I record information such as the input file utilized, the command I used, the timestamp, and the outcomes each time I execute the script. Because the logs preserve the integrity and history of each run and generate a record of incident-style metadata, this immediately fulfills CSF RS.AN-07. These records allow me to determine what happened and why if something suddenly changes in the future. Additionally, Zero Trust Tenet 5, which stresses tracking and evaluating asset integrity, is supported by the logs. The script, the dataset, and the environment in which I run them are my "assets" in this instance. The logs make my workflow more visible and reliable by assisting me in identifying problems, inconsistencies, or unexpected output.

## Rationale (Row 3 – Containerized environment)
My analytic environment may be clearly and consistently defined by using a Docker container. I can reproduce the same environment at any moment, and anyone else can do the same, because the Dockerfile contains all the dependencies, versions, and configuration information. This is directly consistent with CSF PR. PS-01 because I'm using configuration management techniques rather than relying on my machine's installed software. Because it represents the notion that we shouldn't rely on trusted networks or trusted devices, the container also aligns with Zero Trust Tenet 2. Rather, I'm conducting the analysis in a secure, controlled environment. This method lessens surprises, increases the project's repeatability, and strengthens my basis for upcoming security enhancements.

---

## Profile Snippet (Current → Target)

(SP 1301 term: Current/Target Profile)

**Current Profile:**
- **PR.PS-01:** Dependencies and tooling are installed manually on the host; configuration varies by user.  
- **DE.AE-02:** Event analysis is performed informally without a reusable script or consistent metric.  
- **RS.AN-07:** There is no structured process for documenting runs or preserving output provenance.

**Target Profile:**
- **PR.PS-01:** All analysis runs execute inside a container with pinned versions and reproducible configuration.  
- **DE.AE-02:** A single, reusable script provides consistent analysis and measurable output.  
- **RS.AN-07:** All runs produce a dated markdown log under `docs/run_logs/`, showing inputs, commands, and results.

