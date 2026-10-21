# Max Profit Calculator (Streamlit)

## 1. Install dependencies
```bash
python -m pip install -r requirements.txt
```

## 2. Run the app
```bash
python -m streamlit run app.py
```

A browser tab should open. Enter `n` and click **Calculate maximum profit**.

## Algorithm note
The app follows the assignment's earnings rule: each building earns
`(n - completion_time) * earning_rate` after construction completes.
It checks possible construction sequences and returns the best earnings
and the corresponding counts of Theatres (T), Pubs (P), and Commercial Parks (C).
