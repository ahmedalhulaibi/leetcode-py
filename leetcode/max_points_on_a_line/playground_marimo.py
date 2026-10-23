import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_points, run_max_points
    from solution import Solution

    return Solution, assert_max_points, run_max_points


@app.cell
def _():
    # Example test case
    points: list[list[int]] = [[1, 1], [2, 2], [3, 3]]
    expected: int = 3
    return expected, points


@app.cell
def _(Solution, points: list[list[int]], run_max_points):
    result = run_max_points(Solution, points)
    print(f"Max points on a line: {result}")
    result
    return (result,)


@app.cell
def _(assert_max_points, expected: int, result):
    assert_max_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
