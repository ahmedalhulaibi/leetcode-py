import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_relative_ranks, run_find_relative_ranks
    from solution import Solution

    return Solution, assert_find_relative_ranks, run_find_relative_ranks


@app.cell
def _():
    # Example test case
    score = [5, 4, 3, 2, 1]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    return expected, score


@app.cell
def _(Solution, run_find_relative_ranks, score):
    result = run_find_relative_ranks(Solution, score)
    result
    return (result,)


@app.cell
def _(assert_find_relative_ranks, expected, result):
    assert_find_relative_ranks(result, expected)
    return


if __name__ == "__main__":
    app.run()
