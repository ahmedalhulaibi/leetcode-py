import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_max_form, run_find_max_form
    from solution import Solution

    return Solution, assert_find_max_form, run_find_max_form


@app.cell
def _():
    # Example test case
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    expected = 4
    return expected, m, n, strs


@app.cell
def _(Solution, m, n, run_find_max_form, strs):
    result = run_find_max_form(Solution, strs, m, n)
    result
    return (result,)


@app.cell
def _(assert_find_max_form, expected, result):
    assert_find_max_form(result, expected)
    return


if __name__ == "__main__":
    app.run()
