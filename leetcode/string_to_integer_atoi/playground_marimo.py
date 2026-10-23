import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_atoi, run_my_atoi
    from solution import Solution

    return Solution, assert_my_atoi, run_my_atoi


@app.cell
def _():
    # Example test case
    s = "42"
    expected = 42
    return expected, s


@app.cell
def _(Solution, run_my_atoi, s):
    result = run_my_atoi(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_my_atoi, expected, result):
    assert_my_atoi(result, expected)
    return


if __name__ == "__main__":
    app.run()
