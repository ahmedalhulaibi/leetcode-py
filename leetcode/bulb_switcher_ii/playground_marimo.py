import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flip_lights, run_flip_lights
    from solution import Solution

    return Solution, assert_flip_lights, run_flip_lights


@app.cell
def _():
    # Example test case
    n = 1
    presses = 1
    expected = 2
    return expected, n, presses


@app.cell
def _(Solution, n, presses, run_flip_lights):
    result = run_flip_lights(Solution, n, presses)
    result
    return (result,)


@app.cell
def _(assert_flip_lights, expected, result):
    assert_flip_lights(result, expected)
    return


if __name__ == "__main__":
    app.run()
