import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_combination_sum_3, run_combination_sum_3
    from solution import Solution

    return Solution, assert_combination_sum_3, run_combination_sum_3


@app.cell
def _():
    # Example test case
    k = 3
    n = 7
    expected = [[1, 2, 4]]
    return expected, k, n


@app.cell
def _(Solution, k, n, run_combination_sum_3):
    result = run_combination_sum_3(Solution, k, n)
    result
    return (result,)


@app.cell
def _(assert_combination_sum_3, expected, result):
    assert_combination_sum_3(result, expected)
    return


if __name__ == "__main__":
    app.run()
