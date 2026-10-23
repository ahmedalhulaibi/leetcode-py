import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_if_prerequisite, run_check_if_prerequisite
    from solution import Solution

    return Solution, assert_check_if_prerequisite, run_check_if_prerequisite


@app.cell
def _():
    # Example test case
    num_courses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    expected = [False, True]
    return expected, num_courses, prerequisites, queries


@app.cell
def _(
    Solution,
    num_courses,
    prerequisites,
    queries,
    run_check_if_prerequisite,
):
    result = run_check_if_prerequisite(Solution, num_courses, prerequisites, queries)
    result
    return (result,)


@app.cell
def _(assert_check_if_prerequisite, expected, result):
    assert_check_if_prerequisite(result, expected)
    return


if __name__ == "__main__":
    app.run()
