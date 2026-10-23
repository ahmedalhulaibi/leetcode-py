import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_bulb_switch, run_bulb_switch
    from solution import Solution

    return Solution, assert_bulb_switch, run_bulb_switch


@app.cell
def _():
    # Example test case
    n: int = 3
    expected: int = 1
    return expected, n


@app.cell
def _(Solution, n: int, run_bulb_switch):
    result = run_bulb_switch(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_bulb_switch, expected: int, result):
    assert_bulb_switch(result, expected)
    return


if __name__ == "__main__":
    app.run()
