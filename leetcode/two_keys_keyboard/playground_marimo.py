import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_steps, run_min_steps
    from solution import Solution

    return Solution, assert_min_steps, run_min_steps


@app.cell
def _():
    # Example test case
    n = 3
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_min_steps):
    result = run_min_steps(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_min_steps, expected, result):
    assert_min_steps(result, expected)
    return


if __name__ == "__main__":
    app.run()
