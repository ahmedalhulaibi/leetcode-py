import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_broken_calc, run_broken_calc
    from solution import Solution

    return Solution, assert_broken_calc, run_broken_calc


@app.cell
def _():
    # Example test case
    start_value = 2
    target = 3
    expected = 2
    return expected, start_value, target


@app.cell
def _(Solution, run_broken_calc, start_value, target):
    result = run_broken_calc(Solution, start_value, target)
    result
    return (result,)


@app.cell
def _(assert_broken_calc, expected, result):
    assert_broken_calc(result, expected)
    return


if __name__ == "__main__":
    app.run()
