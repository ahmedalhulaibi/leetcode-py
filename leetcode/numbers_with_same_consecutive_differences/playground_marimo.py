import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nums_same_consec_diff, run_nums_same_consec_diff
    from solution import Solution

    return Solution, assert_nums_same_consec_diff, run_nums_same_consec_diff


@app.cell
def _():
    # Example test case
    n = 3
    k = 7
    expected = [181, 292, 707, 818, 929]
    return expected, k, n


@app.cell
def _(Solution, k, n, run_nums_same_consec_diff):
    result = run_nums_same_consec_diff(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_nums_same_consec_diff, expected, result):
    assert_nums_same_consec_diff(result, expected)
    return


if __name__ == "__main__":
    app.run()
