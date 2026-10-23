import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_derangement, run_find_derangement
    from solution import Solution

    return Solution, assert_find_derangement, run_find_derangement


@app.cell
def _():
    # Example test case
    n = 3
    expected = 2
    return expected, n


@app.cell
def _(Solution, n, run_find_derangement):
    result = run_find_derangement(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_find_derangement, expected, result):
    assert_find_derangement(result, expected)
    return


if __name__ == "__main__":
    app.run()
