import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_ugly, run_is_ugly
    from solution import Solution

    return Solution, assert_is_ugly, run_is_ugly


@app.cell
def _():
    # Example test case
    n = 6
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_is_ugly):
    result = run_is_ugly(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_is_ugly, expected, result):
    assert_is_ugly(result, expected)
    return


if __name__ == "__main__":
    app.run()
