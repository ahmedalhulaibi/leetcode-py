import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_sum, run_get_sum
    from solution import Solution

    return Solution, assert_get_sum, run_get_sum


@app.cell
def _():
    # Example test case
    a = 1
    b = 2
    expected = 3
    return a, b, expected


@app.cell
def _(Solution, a, b, run_get_sum):
    result = run_get_sum(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_get_sum, expected, result):
    assert_get_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
