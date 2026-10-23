import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_kth_number, run_find_kth_number
    from solution import Solution

    return Solution, assert_find_kth_number, run_find_kth_number


@app.cell
def _():
    # Example test case
    m = 3
    n = 3
    k = 5
    expected = 3
    return expected, k, m, n


@app.cell
def _(Solution, k, m, n, run_find_kth_number):
    result = run_find_kth_number(Solution, m, n, k)
    result
    return (result,)


@app.cell
def _(assert_find_kth_number, expected, result):
    assert_find_kth_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
