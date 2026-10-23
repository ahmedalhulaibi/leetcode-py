import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_n_straight_hand, run_is_n_straight_hand
    from solution import Solution

    return Solution, assert_is_n_straight_hand, run_is_n_straight_hand


@app.cell
def _():
    # Example test case
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    group_size = 3
    expected = True
    return expected, group_size, hand


@app.cell
def _(Solution, group_size, hand, run_is_n_straight_hand):
    result = run_is_n_straight_hand(Solution, hand, group_size)
    result
    return (result,)


@app.cell
def _(assert_is_n_straight_hand, expected, result):
    assert_is_n_straight_hand(result, expected)
    return


if __name__ == "__main__":
    app.run()
