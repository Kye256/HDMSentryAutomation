# HDM-Sentry Automation

Automated sensitivity analysis of the HDM-4 highway management model using Python GUI automation and statistical methods (ANOVA, Sobol indices).

## What This Does

[HDM-4](https://www.piarc.org/en/activities/Road-Pavements-Earthworks/HDM-4-Software) is the standard tool for economic appraisal of road projects worldwide, but running hundreds of analyses manually through its GUI is impractical. **HDM-Sentry** is a simplified front-end to HDM-4, and this project automates it.

The core script (`hdmsentry_automation.py`) drives HDM-Sentry's Windows GUI using `pywinauto` to run full factorial experiments across four input parameters: traffic volume, traffic growth, initial road condition, and geometry. A second script (`results_extractor.py`) connects to the Access databases HDM-4 produces and extracts NPV, IRR, and IRI results for analysis.

The extracted results were then analysed using ANOVA (to identify which inputs matter most) and Sobol sensitivity analysis (to quantify global sensitivity indices), covering both gravel and bituminous road maintenance alternatives.

## Repository Structure

```
├── scripts/                    # Python automation and analysis code
│   ├── hdmsentry_automation.py # Main: drives HDM-Sentry GUI via pywinauto
│   ├── results_extractor.py    # Extracts NPV/IRR/IRI from Access databases
│   ├── factorial_design.py     # Generates factorial experiment combinations
│   ├── sobol_analysis.py       # Sobol sensitivity analysis (SALib)
│   ├── delta_analysis.py       # Delta moment-independent sensitivity
│   ├── create_input.py         # Input file generation
│   ├── graph.py                # Result visualisation
│   ├── old_versions/           # Script revision history
│   └── data/                   # Script inputs and raw outputs
├── results/
│   ├── anova/                  # ANOVA results with plots per trial
│   ├── factorial/              # Factorial experiment outputs (trials 1-7)
│   └── sobol/                  # Sobol sensitivity indices
├── data/                       # Reference data (road list, abbreviations)
├── docs/
│   ├── thesis.pdf              # Full MSc dissertation
│   ├── presentation.ppt        # Oral defence presentation
│   └── poster.pptx             # Research poster
└── LICENSE
```

## Key Scripts

| Script | Purpose |
|--------|---------|
| `hdmsentry_automation.py` | Automates HDM-Sentry via `pywinauto` — reads input parameters, navigates the GUI, runs analyses |
| `results_extractor.py` | Connects to HDM-4's Access `.mdb` databases via `pyodbc`, extracts economic outputs |
| `factorial_design.py` | Generates full factorial combinations of input levels |
| `sobol_analysis.py` | Runs Sobol sensitivity analysis using SALib |
| `delta_analysis.py` | Computes delta moment-independent sensitivity measures |

## Dependencies

- Python 2.7 (original development environment)
- [pywinauto](https://pywinauto.readthedocs.io/) — Windows GUI automation
- [pyodbc](https://github.com/mkleehammer/pyodbc) — Access database connectivity
- [SALib](https://salib.readthedocs.io/) — Sensitivity analysis library
- [numpy](https://numpy.org/)
- HDM-Sentry (Windows application, requires HDM-4 licence)

## Context

This work was completed as an MSc dissertation at the University of Birmingham, School of Engineering (2016). The full thesis, oral presentation, and poster are in the `docs/` folder.

The research found that **traffic growth and initial road condition** are the most influential inputs to HDM-Sentry's economic outputs, while geometry had relatively little effect — suggesting that simplified data collection focused on these key parameters could make HDM-4 adoption more practical in resource-constrained settings.

## Citation

If you found this useful, please cite:

```bibtex
@mastersthesis{kazibwe2016hdmsentry,
  author  = {Kazibwe, Philip Kyeyune},
  title   = {Assessing High Level Data Representation for HDM-4},
  school  = {University of Birmingham},
  year    = {2016},
  type    = {MSc Dissertation},
  note    = {School of Engineering, Road Management and Engineering}
}
```

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
