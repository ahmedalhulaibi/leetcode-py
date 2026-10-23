import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min_arrow_shots, run_find_min_arrow_shots
    from solution import Solution

    return Solution, assert_find_min_arrow_shots, run_find_min_arrow_shots


@app.cell
def _():
    # Example test case
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected = 2
    return expected, points


@app.cell
def _(Solution, points, run_find_min_arrow_shots):
    result = run_find_min_arrow_shots(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_find_min_arrow_shots, expected, result):
    assert_find_min_arrow_shots(result, expected)
    return


if __name__ == "__main__":
    app.run()
