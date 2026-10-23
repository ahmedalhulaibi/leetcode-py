import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_racecar, run_racecar
    from solution import Solution

    return Solution, assert_racecar, run_racecar


@app.cell
def _():
    # Example test case
    target = 3
    expected = 2
    return expected, target


@app.cell
def _(Solution, run_racecar, target):
    result = run_racecar(Solution, target)
    result
    return (result,)


@app.cell
def _(assert_racecar, expected, result):
    assert_racecar(result, expected)
    return


if __name__ == "__main__":
    app.run()
