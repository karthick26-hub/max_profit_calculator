import streamlit as st

st.set_page_config(
    page_title="Max Profit Calculator",
    layout="centered",
)

BUILDINGS = {
    "T": {"name": "Theatre", "duration": 5, "rate": 1500},
    "P": {"name": "Pub", "duration": 4, "rate": 1000},
    "C": {"name": "Commercial Park", "duration": 10, "rate": 2000},
}


def calculate_max_profit(n: int):
    """
    Try every valid sequence of buildings in construction order.
    A completed building earns (n - its completion time) * its earning rate.
    Previously completed buildings keep earning while later buildings are built.
    """
    # dp[t] = best profit for a sequence that has used exactly t construction units.
    dp = [0] * (n + 1)
    # Keep building counts for the best sequence reaching each construction time.
    counts = [(0, 0, 0) for _ in range(n + 1)]
    # Index order is T, P, C.
    building_order = [("T", 5, 1500), ("P", 4, 1000), ("C", 10, 2000)]

    for t in range(n + 1):
        for idx, (code, duration, rate) in enumerate(building_order):
            finish_time = t + duration
            if finish_time > n:
                continue

            candidate_profit = dp[t] + (n - finish_time) * rate
            candidate_counts = list(counts[t])
            candidate_counts[idx] += 1
            candidate_counts = tuple(candidate_counts)

            if candidate_profit > dp[finish_time]:
                dp[finish_time] = candidate_profit
                counts[finish_time] = candidate_counts

    best_time = max(range(n + 1), key=lambda t: dp[t])
    return dp[best_time], counts[best_time], best_time


st.title(" Max Profit Calculator")
st.write(
    "Enter the total available time units to find the best mix of "
    "Theatres, Pubs, and Commercial Parks."
)

with st.expander("Building details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Theatre (T)", "$1,500 / unit", "5 time units to build")
    with col2:
        st.metric("Pub (P)", "$1,000 / unit", "4 time units to build")
    with col3:
        st.metric("Commercial Park (C)", "$2,000 / unit", "10 time units to build")

n = st.number_input(
    "Enter total time units (n)",
    min_value=0,
    max_value=10000,
    value=13,
    step=1,
)

if st.button("Calculate maximum profit", type="primary", use_container_width=True):
    max_profit, counts, used_time = calculate_max_profit(int(n))
    theatre_count, pub_count, commercial_count = counts

    st.subheader("Result")
    st.metric("Maximum earnings", f"${max_profit:,.0f}")

    result_col1, result_col2, result_col3 = st.columns(3)
    result_col1.metric("Theatres (T)", theatre_count)
    result_col2.metric("Pubs (P)", pub_count)
    result_col3.metric("Commercial Parks (C)", commercial_count)

    st.caption(f"Construction time used: {used_time} of {int(n)} units.")

    with st.expander("How was this calculated?"):
        st.write(
            "Each building starts earning when construction is complete. "
            "Its earnings are (total time − completion time) × earning rate. "
            "The algorithm compares valid construction sequences and keeps "
            "the most profitable result."
        )
        st.code(
            f"T: {theatre_count}, P: {pub_count}, C: {commercial_count}",
            language="text",
        )

st.divider()
st.caption("Based on the Max Profit Problem interview assignment.")
