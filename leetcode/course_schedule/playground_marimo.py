import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_finish, run_can_finish
    from solution import Solution

    return Solution, assert_can_finish, run_can_finish


@app.cell
def _():
    # Example test case
    num_courses = 2
    prerequisites = [[1, 0]]
    expected = True
    return expected, num_courses, prerequisites


@app.cell
def _(Solution, num_courses, prerequisites, run_can_finish):
    result = run_can_finish(Solution, num_courses, prerequisites)
    result
    return (result,)


@app.cell
def _(assert_can_finish, expected, result):
    assert_can_finish(result, expected)
    return


if __name__ == "__main__":
    app.run()
