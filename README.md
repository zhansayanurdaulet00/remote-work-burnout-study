# The Impact of Remote Work Formats on Employee Emotional Burnout

**Authors:** Nurdaulet Zhansaya, Kabygali Nazerke

**Repository:** https://github.com/zhansayanurdaulet00/remote-work-burnout-study

## Overview

This project develops a reproducible research pipeline for investigating the relationship between remote work, work-life boundary blurring, and employee emotional burnout.

The repository includes configuration files, a small synthetic dataset, and a Python script for validating the input data and generating descriptive statistics.

## Research Questions

- **RQ1:** To what extent does work-life boundary blurring predict employee emotional exhaustion and burnout?
- **RQ2:** Do schedule autonomy and psychological detachment moderate the relationship between remote work intensity and employee emotional burnout?

## Research Design

The planned study uses a quantitative, observational, cross-sectional design. The research hypotheses will be evaluated using appropriate regression models when a sufficiently large and documented research dataset is available.

The included 10-row synthetic sample is intended only for pipeline testing. It must not be interpreted as empirical evidence.

## System Requirements

- Docker, or Python 3.10 with pip.
- Required Python packages listed in `requirements.txt`.
- A terminal or command prompt.

## Directory Structure

```text
remote-work-burnout-study/
├── data/
│   └── sample/
│       └── sample_data.csv
├── src/
│   └── main.py
├── outputs/
├── tests/
├── docs/
├── config.yaml
├── Dockerfile
├── environment.yml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Quickstart Guide

### Option 1: Docker

Build the container:

```bash
docker build -t burnout-study .
```

Run the pipeline:

```bash
docker run --rm -v "%cd%/outputs:/app/outputs" burnout-study
```

These commands are intended for Windows Command Prompt. The mounted output directory allows the generated log to remain available after the container exits.

### Option 2: Local Python

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python src/main.py
```

The script validates the sample data, computes descriptive statistics, and writes a log to `outputs/benchmark.log`.

## Planned Statistical Analysis

| Analysis | Purpose |
|---|---|
| H1 regression model | Estimate the association between boundary blurring and burnout |
| H2 moderation model | Evaluate interactions between remote work intensity, schedule autonomy, and psychological detachment |
| Diagnostic checks | Assess model assumptions and data quality |

## Reproducibility

The analysis configuration is stored in `config.yaml`. Python dependencies are pinned in `requirements.txt`. The sample dataset supports pipeline verification before the main empirical analysis.

## Citation

Nurdaulet, Zh., & Kabygali, N. (2026). *The Impact of Remote Work Formats on Employee Emotional Burnout: Focusing on Boundary Blurring and Psychosocial Stressors*. GitHub repository.

## License

This project is distributed under the MIT License. See `LICENSE` for details.
