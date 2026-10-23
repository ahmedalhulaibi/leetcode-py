import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_steps, run_minimum_steps
    from solution import Solution

    return Solution, assert_minimum_steps, run_minimum_steps


@app.cell
def _():
    # Example test case
    s = "101"
    expected = 1
    return expected, s


@app.cell
def _(Solution, run_minimum_steps, s):
    result = run_minimum_steps(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_minimum_steps, expected, result):
    assert_minimum_steps(result, expected)
    return


if __name__ == "__main__":
    app.run()
