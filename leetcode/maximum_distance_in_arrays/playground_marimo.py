import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_distance, run_max_distance
    from solution import Solution

    return Solution, assert_max_distance, run_max_distance


@app.cell
def _():
    # Example test case
    arrays: list[list[int]] = [[1, 2, 3], [4, 5], [1, 2, 3]]
    expected = 4
    return arrays, expected


@app.cell
def _(Solution, arrays: list[list[int]], run_max_distance):
    result = run_max_distance(Solution, arrays)
    result
    return (result,)


@app.cell
def _(assert_max_distance, expected, result):
    assert_max_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
