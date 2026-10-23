import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_detonation, run_maximum_detonation
    from solution import Solution

    return Solution, assert_maximum_detonation, run_maximum_detonation


@app.cell
def _():
    # Example test case
    bombs: list[list[int]] = [[2, 1, 3], [6, 1, 4]]
    expected = 2
    return bombs, expected


@app.cell
def _(Solution, bombs: list[list[int]], run_maximum_detonation):
    result = run_maximum_detonation(Solution, bombs)
    result
    return (result,)


@app.cell
def _(assert_maximum_detonation, expected, result):
    assert_maximum_detonation(result, expected)
    return


if __name__ == "__main__":
    app.run()
