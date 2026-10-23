import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_order, run_find_order
    from solution import Solution

    return Solution, assert_find_order, run_find_order


@app.cell
def _():
    # Example test case
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected = [0, 2, 1, 3]
    return expected, num_courses, prerequisites


@app.cell
def _(Solution, num_courses, prerequisites, run_find_order):
    result = run_find_order(Solution, num_courses, prerequisites)
    result
    return (result,)


@app.cell
def _(assert_find_order, expected, result):
    assert_find_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
