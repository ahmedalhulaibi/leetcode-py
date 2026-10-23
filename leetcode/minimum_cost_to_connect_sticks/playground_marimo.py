import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_connect_sticks, run_connect_sticks
    from solution import Solution

    return Solution, assert_connect_sticks, run_connect_sticks


@app.cell
def _():
    # Example test case
    sticks = [2, 4, 3]
    expected = 14
    return expected, sticks


@app.cell
def _(Solution, run_connect_sticks, sticks):
    result = run_connect_sticks(Solution, sticks)
    result
    return (result,)


@app.cell
def _(assert_connect_sticks, expected, result):
    assert_connect_sticks(result, expected)
    return


if __name__ == "__main__":
    app.run()
