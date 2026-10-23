import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_kth_bit, run_find_kth_bit
    from solution import Solution

    return Solution, assert_find_kth_bit, run_find_kth_bit


@app.cell
def _():
    # Example test case
    n = 3
    k = 1
    expected = "0"
    return expected, k, n


@app.cell
def _(Solution, k, n, run_find_kth_bit):
    result = run_find_kth_bit(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_find_kth_bit, expected, result):
    assert_find_kth_bit(result, expected)
    return


if __name__ == "__main__":
    app.run()
