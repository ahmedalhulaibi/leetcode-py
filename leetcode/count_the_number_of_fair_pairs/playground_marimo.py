import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_fair_pairs, run_count_fair_pairs
    from solution import Solution

    return Solution, assert_count_fair_pairs, run_count_fair_pairs


@app.cell
def _():
    # Example test case
    nums: list[int] = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    expected = 6
    return expected, lower, nums, upper


@app.cell
def _(Solution, lower, nums: list[int], run_count_fair_pairs, upper):
    result = run_count_fair_pairs(Solution, nums, lower, upper)
    result
    return (result,)


@app.cell
def _(assert_count_fair_pairs, expected, result):
    assert_count_fair_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
