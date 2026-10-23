import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_intersection_size_two, run_intersection_size_two
    from solution import Solution

    return Solution, assert_intersection_size_two, run_intersection_size_two


@app.cell
def _():
    # Example test case
    intervals = [[1, 3], [3, 7], [8, 9]]
    expected = 5
    return expected, intervals


@app.cell
def _(Solution, intervals, run_intersection_size_two):
    result = run_intersection_size_two(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_intersection_size_two, expected, result):
    assert_intersection_size_two(result, expected)
    return


if __name__ == "__main__":
    app.run()
