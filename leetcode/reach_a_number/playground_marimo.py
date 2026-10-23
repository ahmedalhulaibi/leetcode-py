import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reach_number, run_reach_number
    from solution import Solution

    return Solution, assert_reach_number, run_reach_number


@app.cell
def _():
    # Example test case
    target = 2
    expected = 3
    return expected, target


@app.cell
def _(Solution, run_reach_number, target):
    result = run_reach_number(Solution, target)
    result
    return (result,)


@app.cell
def _(assert_reach_number, expected, result):
    assert_reach_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
