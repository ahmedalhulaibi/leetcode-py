import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_height_checker, run_height_checker
    from solution import Solution

    return Solution, assert_height_checker, run_height_checker


@app.cell
def _():
    # Example test case
    heights = [1, 1, 4, 2, 1, 3]
    expected = 3
    return expected, heights


@app.cell
def _(Solution, heights, run_height_checker):
    result = run_height_checker(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_height_checker, expected, result):
    assert_height_checker(result, expected)
    return


if __name__ == "__main__":
    app.run()
