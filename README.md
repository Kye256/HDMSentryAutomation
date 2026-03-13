# Assessing High Level Data Representation for HDM-4

**MSc Dissertation** — University of Birmingham, School of Engineering  
**Degree:** Master of Science in Road Management and Engineering  
**Author:** Philip Kyeyune Kazibwe  
**Date:** August 2016

## Abstract

Economic decision making is at the kernel of highway management. The Highway Development and Management Model (HDM-4) is a popular appraisal tool for road projects, but adoption is hindered by its large data requirements. This project assessed high level data representations for the HDM-4 Model as implemented in HDM-Sentry, a simplified HDM-4 data-preparation and analysis tool.

Four main inputs to HDM-Sentry were considered: Traffic Volume, Traffic Growth, Initial Road Condition, and Geometry. A full factorial experiment design was used to run analyses across all levels of the four inputs for both gravel and bituminous surfaced roads. The NPV and average IRI outputs were analysed using ANOVA sensitivity analysis, supplemented by Sobol sensitivity analysis for global sensitivity indices.

## Repository Structure

```
├── Thesis_Rev02_AsSubmitted.docx   # Final thesis (Word)
├── Thesis_Rev02_AsSubmitted.pdf    # Final thesis (PDF)
├── PKK535_PresentationRev01_AsPresented.ppt  # Oral presentation
├── Poster.pptx                     # Research poster
├── Poster.pdf                      # Research poster (PDF)
├── abbreviations.csv               # Abbreviations used in the thesis
├── ListOfRoads.xls                 # Road network data
├── LowLevelDataRepresentation.xlsx # Data representation reference
└── Analysis/
    ├── Scripts/                    # Python automation scripts
    │   ├── HDMSENTRYAutoRev4.py    # HDM-Sentry automation (final version)
    │   ├── ResultsExtractorRev3.py # Results extraction from HDM-4 databases
    │   ├── factorial.py            # Factorial experiment design
    │   ├── graph.py                # Graph generation
    │   └── OldVersions/            # Earlier script revisions
    ├── Results/                    # Factorial analysis outputs
    │   ├── AnovaResults/           # ANOVA analysis with graphs per trial
    │   ├── Trial2-7/              # Per-trial results (CSVs, graphs)
    │   └── *.csv, *.png, *.xlsx   # Summary data and visualisations
    └── SobolAnalysis/
        └── Trial2/                 # Sobol sensitivity analysis scripts and results
```

## Methodology

1. **Automation** — Python scripts automated HDM-Sentry to run hundreds of analyses across factorial combinations of input parameters
2. **Factorial Design** — Full factorial experiments across Traffic Volume, Traffic Growth, Initial Road Condition, and Geometry for multiple maintenance alternatives
3. **ANOVA** — Analysis of Variance to identify which input parameters most significantly affect NPV and IRI outputs
4. **Sobol Analysis** — Global sensitivity analysis to quantify the contribution of each input parameter

## Tools Used

- **HDM-4 / HDM-Sentry** — Highway Development and Management Model
- **Python** — Automation of HDM-Sentry and data extraction
- **MATLAB** — ANOVA statistical analysis
- **SALib** — Sobol sensitivity analysis library
