import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_number, run_is_number
    from solution import Solution

    return Solution, assert_is_number, run_is_number


@app.cell
def _():
    # Example test case
    s = "0"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_is_number, s):
    result = run_is_number(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_is_number, expected, result):
    assert_is_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
