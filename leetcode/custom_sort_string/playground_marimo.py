import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_custom_sort_string, run_custom_sort_string
    from solution import Solution

    return Solution, assert_custom_sort_string, run_custom_sort_string


@app.cell
def _():
    # Example test case
    order = "cba"
    s = "abcd"
    expected = "cbad"
    return expected, order, s


@app.cell
def _(Solution, order, run_custom_sort_string, s):
    result = run_custom_sort_string(Solution, order, s)
    result
    return (result,)


@app.cell
def _(assert_custom_sort_string, expected, result):
    assert_custom_sort_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
