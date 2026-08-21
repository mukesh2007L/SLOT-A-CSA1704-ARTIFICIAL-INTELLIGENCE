# Integrated Experiments: Decision Tree Classification & Q-Learning Grid World

**Course:** Artificial Intelligence (CSA17) — CO4, Assessment Tool 3
**Experiments:**
1. Decision Tree Classification on the Iris dataset
2. Q-Learning reinforcement learning in a 4x4 Grid World

This repository contains the complete, runnable solution to both integrated experiments.

---

## Files in this Submission

| # | File | Description |
|---|------|-------------|
| 1 | `01_Problem_Statement.pdf` | Full restatement of both experiments (all sub-parts a/b/c) and the evaluation rubric. |
| 2 | `02_Solution.pdf` | Complete written solution — explanations, tables, tree structure, Q-value tables and charts for every sub-question. |
| 3 | `integrated_experiments.py` | Python source code implementing both experiments end-to-end. |
| 4 | `integrated_experiments_dashboard.png` | Single consolidated output visualisation (decision tree, confusion matrix, feature importance, grid world, learned policy, reward curve). |
| 5 | `03_Report.pdf` | Professional project report (executive summary, methodology, results, discussion, recommendations). |
| 6 | `README.md` | This file. |

*(Supporting files also produced by the script: `iris_dataset.csv`, `misclassified_instances.csv`,
`q_table_final.csv`, and `results_summary.json`.)*

---

## What the Code Does

Running `integrated_experiments.py` executes both experiments in sequence:

### Experiment 1 — Decision Tree Classification
- Loads the built-in **Iris dataset** (150 samples, 4 features, 3 classes) via scikit-learn.
- Displays the first 5 rows, data types, and confirms there are no missing values.
- Splits the data 70:30 (stratified) into train/test sets.
- Builds a `DecisionTreeClassifier` (Gini criterion), prints the full textual tree structure,
  and identifies the root node with a Gini-importance justification.
- Evaluates the model with Accuracy, Confusion Matrix, and a full Classification Report, and
  lists the misclassified test instances (saved to `misclassified_instances.csv`).

### Experiment 2 — Q-Learning Grid World
- Defines a 4x4 Grid World MDP: 16 states, 4 actions (Up/Down/Left/Right), a Goal cell
  (+10 reward), 3 Obstacle cells (-5 reward), and a per-step penalty (-1).
- Initialises a 16x4 Q-table with zeros and trains the agent for **100 episodes** using
  tabular Q-Learning with an &epsilon;-greedy policy (&alpha;=0.1, &gamma;=0.9, &epsilon;=0.1).
- Records and prints Q-values for two representative states at Episodes 1, 50, and 100.
- Extracts the final greedy policy, saves the Q-table (`q_table_final.csv`), and plots
  cumulative reward per episode with a moving average to demonstrate convergence.

All console output, the datasets, the metrics summary, and the results dashboard PNG are
written to the working directory when the script runs.

---

## How to Run

### Requirements
```
Python 3.9+
numpy
pandas
scikit-learn
matplotlib
```

### Install dependencies
```bash
pip install numpy pandas scikit-learn matplotlib
```

### Run the full pipeline
```bash
python3 integrated_experiments.py
```

This prints all results (Experiment 1 & 2) to the console and generates:
- `iris_dataset.csv` — the Iris dataset with species labels
- `misclassified_instances.csv` — the Decision Tree's misclassified test rows
- `q_table_final.csv` — the final learned Q-table
- `results_summary.json` — key metrics in machine-readable form
- `integrated_experiments_dashboard.png` — the consolidated results dashboard
- `figs/*.png` — individual chart panels (used in the PDF reports)

Total runtime: a few seconds on a standard laptop (no GPU required).

---

## Key Results Summary

### Experiment 1 — Decision Tree
| Metric | Value |
|---|---|
| Accuracy | 0.889 (40/45 correct) |
| Root Node | petal length (cm) &le; 2.45 (Gini importance 0.549) |
| Top Predictors | petal length (0.549), petal width (0.436) |
| Misclassified Instances | 5 (all between versicolor / virginica) |

### Experiment 2 — Q-Learning
| Hyperparameter | Value |
|---|---|
| Learning rate (&alpha;) | 0.1 |
| Discount factor (&gamma;) | 0.9 |
| Exploration rate (&epsilon;) | 0.1 |
| Episodes | 100 |
| Mean reward (last 10 episodes) | 4.40 |

The final learned policy reliably guides the agent from the Start cell to the Goal cell while
avoiding all three obstacle cells, converging after roughly 40 training episodes.

---

## Author

Prepared as the deliverable for the SIMATS Engineering Assessment Tool 3
(Artificial Intelligence, CSA17, CO4 — Integrated Experiments).
