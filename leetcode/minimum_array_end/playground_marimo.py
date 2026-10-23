import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_end, run_min_end
    from solution import Solution

    return Solution, assert_min_end, run_min_end


@app.cell
def _():
    # Example test case
    n = 3
    x = 4
    expected = 6
    return expected, n, x


@app.cell
def _(Solution, n, run_min_end, x):
    result = run_min_end(Solution, n, x)
    result
    return (result,)


@app.cell
def _(assert_min_end, expected, result):
    assert_min_end(result, expected)
    return


if __name__ == "__main__":
    app.run()
