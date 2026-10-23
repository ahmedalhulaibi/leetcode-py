import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rearrange_sticks, run_rearrange_sticks
    from solution import Solution

    return Solution, assert_rearrange_sticks, run_rearrange_sticks


@app.cell
def _():
    # Example test case
    n = 3
    k = 2
    expected = 3
    return expected, k, n


@app.cell
def _(Solution, k, n, run_rearrange_sticks):
    result = run_rearrange_sticks(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_rearrange_sticks, expected, result):
    assert_rearrange_sticks(result, expected)
    return


if __name__ == "__main__":
    app.run()
