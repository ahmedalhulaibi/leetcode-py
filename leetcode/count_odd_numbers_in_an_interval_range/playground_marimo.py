import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_odds, run_count_odds
    from solution import Solution

    return Solution, assert_count_odds, run_count_odds


@app.cell
def _():
    # Example test case
    low = 3
    high = 7
    expected = 3
    return expected, high, low


@app.cell
def _(Solution, high, low, run_count_odds):
    result = run_count_odds(Solution, low, high)
    result
    return (result,)


@app.cell
def _(assert_count_odds, expected, result):
    assert_count_odds(result, expected)
    return


if __name__ == "__main__":
    app.run()
