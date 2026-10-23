import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_valid, run_is_valid
    from solution import Solution

    return Solution, assert_is_valid, run_is_valid


@app.cell
def _():
    # Example test case
    s = "()"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_is_valid, s):
    result = run_is_valid(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_is_valid, expected, result):
    assert_is_valid(result, expected)
    return


if __name__ == "__main__":
    app.run()
