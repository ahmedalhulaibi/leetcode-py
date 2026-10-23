import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_length, run_min_length
    from solution import Solution

    return Solution, assert_min_length, run_min_length


@app.cell
def _():
    # Example test case
    s = "ABFCACDB"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_min_length, s):
    result = run_min_length(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_length, expected, result):
    assert_min_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
