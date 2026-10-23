import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_stones, run_merge_stones
    from solution import Solution

    return Solution, assert_merge_stones, run_merge_stones


@app.cell
def _():
    # Example test case
    stones = [3, 2, 4, 1]
    k = 2
    expected = 20
    return expected, k, stones


@app.cell
def _(Solution, k, run_merge_stones, stones):
    result = run_merge_stones(Solution, stones, k)
    result
    return (result,)


@app.cell
def _(assert_merge_stones, expected, result):
    assert_merge_stones(result, expected)
    return


if __name__ == "__main__":
    app.run()
