import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_trap, run_trap
    from solution import Solution

    return Solution, assert_trap, run_trap


@app.cell
def _():
    # Example test case
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6
    return expected, height


@app.cell
def _(Solution, height, run_trap):
    result = run_trap(Solution, height)
    result
    return (result,)


@app.cell
def _(assert_trap, expected, result):
    assert_trap(result, expected)
    return


if __name__ == "__main__":
    app.run()
