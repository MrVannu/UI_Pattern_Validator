# UI_Patter_Validator
This GitHub repository serves as the archive for the thesis project of Luca Vannuccini. The thesis builds upon the paper "Visualization Impedance Mismatch" by Vannuccini and Janes, which was presented at SERA 2025 in Las Vegas (USA) and is scheduled for publication at SFSCON 2025 in Bolzano this coming November. The success of the paper has been notable, and the thesis aims to expand and advance this work.

The repository is made public to share these resources with the research community, providing an open platform for collaboration. Researchers and developers interested in contributing or building upon this work are welcome to do so.


# What is it?

A comprehensive tool for detecting common GUI interaction patterns and usability issues (for more detailed information please read the paper mentioned before), designed to help developers and designers improve user experience through data-driven insights.

---

## Overview

The **UI Pattern Validator** analyses raw interaction data from user interfaces to identify common usability patterns, repeated actions, and opportunities for personalization. By leveraging statistical analysis and pattern detection, the tool provides actionable insights to enhance interface responsiveness, reduce friction, and increase user satisfaction.

The tool currently supports detection of three key patterns (the other ones are easy to implement as metrics are similar):

1. **Immediate Visual Feedback** – Ensures users receive timely confirmation of their interactions.
2. **Autocomplete** – Identifies input fields where predictive text could improve efficiency.
3. **Customisation** – Highlights redundant configuration actions and potential global defaults.

---

## Architecture & Workflow

The tool follows a structured workflow:

1. **Client-side logging:** Captures user clicks, inputs, and configuration changes via a dedicated plugin.  
2. **Cloud storage:** Logs are sent to a web server and persisted in a database.  
3. **Data export:** Logs are exported as CSV (or TSV) files for analysis.  
4. **Pattern detection:** The tool parses input files, computes metrics, and identifies interaction patterns.  
5. **Output:** Results are displayed to developers or designers to inform UI improvements.

**Workflow Diagram:**  
User Interaction -> Client Plugin -> Web Server -> Cloud Database -> CSV Export -> UI Pattern Validator -> Developer Feedback

<div style="background-color: white; display: flex; justify-content: center; padding: 10px;">
  <img src="img/Tool_Function_ConceptMap.png" alt="Workflow Diagram">
</div>

---

## Pattern Detectors

### 1. Immediate Visual Feedback Detector
Detects delayed or missing feedback in the interface:

- **Metrics:** Time between consecutive actions per user.  
- **Thresholds:**  
  - Impatience: < 500 ms  
  - Missing pattern: < 1,000 ms  
- **Output:**  
  - `Pattern implemented` – no issues detected  
  - `Missing pattern: no visual feedback detected (<1s)` – feedback delayed  
  - `Missing pattern: impatience detected (<500ms)` – user impatience detected


---

### 2. Autocomplete Pattern Detector
Identifies fields where autocomplete could improve user efficiency:

- **Metrics:** Shannon entropy and coverage of most frequent inputs.  
- **Thresholds:**  
  - Coverage ≥ 70%  
  - Normalized entropy < 0.3  
- **Output:**  
  - `Pattern implemented` – diverse inputs  
  - `Candidate for AUTOCOMPLETE` – repetitive inputs detected  
  - `Low variety → Missing pattern` – low diversity in inputs

---

### 3. Customisation Pattern Detector
Evaluates whether customization options are meaningful or redundant:

- **Metrics:**  
  - Per-user repeated configuration (≥80%)  
  - Global preset candidate (>51% of users)  
- **Output:**  
  - `Pattern implemented` – customization is effective  
  - `Repeated config (≥80%)` – persistent default recommended  
  - `Preset global candidate (≥51% users)` – suggest global default  
  - `Diverse customization` – no simplification needed



#### NOTE:
All metrics mentioned below are either drawn from the literature (see the paper) or are arbitrarily defined, as the desired sensibility may vary depending on the specific context or use case.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/MrVannu/UI_Pattern_Validator.git
cd UI_Pattern_Validator
```

2. Prepare your CSV file
Make sure it contains all necessary column headers.
Refer to the test datasets in the `res/` folder for examples.

3. Run the main script on your CSV file (Replace 'yourFile.csv' with your CSV file)

```bash
python3 main.py yourFile.csv
```
Alternatively (if not CSV file is provided), run the script with default test datasets
```bash
python3 main.py
```

6. Optional: Adjust thresholds
As said, thresholds for impatience, coverage, entropy, and repeated configurations
can be modified inside the scripts to better suit your dataset or desired sensitivity.


## Contributing

Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests. Future enhancements could include:

Support for additional patterns

Real-time analysis and dashboard visualization

Integration with analytics platforms

## License

This project is released under the MIT License. See LICENSE for details.