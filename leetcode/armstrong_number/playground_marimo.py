import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_armstrong, run_is_armstrong
    from solution import Solution

    return Solution, assert_is_armstrong, run_is_armstrong


@app.cell
def _():
    # Example test case
    n = 153
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_is_armstrong):
    result = run_is_armstrong(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_is_armstrong, expected, result):
    assert_is_armstrong(result, expected)
    return


if __name__ == "__main__":
    app.run()
