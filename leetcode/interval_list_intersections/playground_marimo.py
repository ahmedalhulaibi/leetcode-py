import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_interval_intersection, run_interval_intersection
    from solution import Solution

    return Solution, assert_interval_intersection, run_interval_intersection


@app.cell
def _():
    # Example test case
    first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
    second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    return expected, first_list, second_list


@app.cell
def _(Solution, first_list, run_interval_intersection, second_list):
    result = run_interval_intersection(Solution, first_list, second_list)
    result
    return (result,)


@app.cell
def _(assert_interval_intersection, expected, result):
    assert_interval_intersection(result, expected)
    return


if __name__ == "__main__":
    app.run()
