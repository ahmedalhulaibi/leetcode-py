import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_valid_cuts, run_check_valid_cuts
    from solution import Solution

    return Solution, assert_check_valid_cuts, run_check_valid_cuts


@app.cell
def _():
    # Example test case
    n = 5
    rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
    expected = True
    return expected, n, rectangles


@app.cell
def _(Solution, n, rectangles, run_check_valid_cuts):
    result = run_check_valid_cuts(Solution, n, rectangles)
    result
    return (result,)


@app.cell
def _(assert_check_valid_cuts, expected, result):
    assert_check_valid_cuts(result, expected)
    return


if __name__ == "__main__":
    app.run()
