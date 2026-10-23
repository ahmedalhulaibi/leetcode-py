import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_total, run_minimum_total
    from solution import Solution

    return Solution, assert_minimum_total, run_minimum_total


@app.cell
def _():
    # Example test case
    triangle: list[list[int]] = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    expected: int = 11
    return expected, triangle


@app.cell
def _(Solution, run_minimum_total, triangle: list[list[int]]):
    result = run_minimum_total(Solution, triangle)
    result
    return (result,)


@app.cell
def _(assert_minimum_total, expected: int, result):
    assert_minimum_total(result, expected)
    return


if __name__ == "__main__":
    app.run()
