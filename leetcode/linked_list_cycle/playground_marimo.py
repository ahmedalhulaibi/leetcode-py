import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_cycle, run_has_cycle
    from solution import Solution

    return Solution, assert_has_cycle, run_has_cycle


@app.cell
def _():
    # Example test case
    values = [3, 2, 0, -4]
    pos = 1
    expected = True
    return expected, pos, values


@app.cell
def _(Solution, pos, run_has_cycle, values):
    result = run_has_cycle(Solution, values, pos)
    result
    return (result,)


@app.cell
def _(assert_has_cycle, expected, result):
    assert_has_cycle(result, expected)
    return


if __name__ == "__main__":
    app.run()
