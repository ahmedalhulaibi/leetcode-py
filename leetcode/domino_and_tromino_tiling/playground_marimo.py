import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_tilings, run_num_tilings
    from solution import Solution

    return Solution, assert_num_tilings, run_num_tilings


@app.cell
def _():
    # Example test case
    n = 3
    expected = 5
    return expected, n


@app.cell
def _(Solution, n, run_num_tilings):
    result = run_num_tilings(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_num_tilings, expected, result):
    assert_num_tilings(result, expected)
    return


if __name__ == "__main__":
    app.run()
