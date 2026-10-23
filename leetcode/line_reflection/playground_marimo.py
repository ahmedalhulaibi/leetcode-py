import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_reflected, run_is_reflected
    from solution import Solution

    return Solution, assert_is_reflected, run_is_reflected


@app.cell
def _():
    # Example test case
    points: list[list[int]] = [[1, 1], [-1, 1]]
    expected = True
    return expected, points


@app.cell
def _(Solution, points: list[list[int]], run_is_reflected):
    result = run_is_reflected(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_is_reflected, expected, result):
    assert_is_reflected(result, expected)
    return


if __name__ == "__main__":
    app.run()
