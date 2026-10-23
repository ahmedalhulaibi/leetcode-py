import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_jewels_in_stones, run_num_jewels_in_stones
    from solution import Solution

    return Solution, assert_num_jewels_in_stones, run_num_jewels_in_stones


@app.cell
def _():
    # Example test case
    jewels = "aA"
    stones = "aAAbbbb"
    expected = 3
    return expected, jewels, stones


@app.cell
def _(Solution, jewels, run_num_jewels_in_stones, stones):
    result = run_num_jewels_in_stones(Solution, jewels, stones)
    result
    return (result,)


@app.cell
def _(assert_num_jewels_in_stones, expected, result):
    assert_num_jewels_in_stones(result, expected)
    return


if __name__ == "__main__":
    app.run()
