import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_confusing_number_ii, run_confusing_number_ii
    from solution import Solution

    return Solution, assert_confusing_number_ii, run_confusing_number_ii


@app.cell
def _():
    # Example test case
    n = 20
    expected = 6
    return expected, n


@app.cell
def _(Solution, n, run_confusing_number_ii):
    result = run_confusing_number_ii(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_confusing_number_ii, expected, result):
    assert_confusing_number_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
