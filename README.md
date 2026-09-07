# task-0 IEEE AI/ML vertical

**Name:** [Ishaan Gupta]

## Structure
```
task-0/
├── README.md
├── q1.py   # List analyzer
├── q2.py   # process_list() with .copy()
├── q3.py   # is_prime() using for-else
├── q4.py   # NumPy basics
├── q5.py   # Pandas CSV analysis
├── q6.py   # Matplotlib visualizations
├── data/
│   ├── student_performance.csv
│   └── processed_student_performance.csv
└── plots/
    ├── final_scores.png
    ├── study_vs_score.png
    ├── score_distribution.png
    └── custom_plot.png
```

## Setup
```bash
pip install numpy pandas matplotlib
```

## Running
```bash
python3 q1.py   # enter N, then N space-separated integers
python3 q2.py   
python3 q3.py   # enter N when prompted
python3 q4.py
python3 q5.py   # writes data/processed_student_performance.csv
python3 q6.py   # writes plots/*.png (run q5.py first)
```

## Notes
- Q1 avoids `max()`, `min()`, `sum()`, `sort()`, `sorted()` as required.
- Q3's `for-else`: the `else` block runs only if the loop finishes without
  hitting `break` (see comment in `q3.py`).
- Q5 and Q6 use the provided `student_performance.csv`; Q6 must be run after
  Q5 since it reads the processed CSV.
