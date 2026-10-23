import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_schedule_course, run_schedule_course
    from solution import Solution

    return Solution, assert_schedule_course, run_schedule_course


@app.cell
def _():
    # Example test case
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    expected = 3
    return courses, expected


@app.cell
def _(Solution, courses, run_schedule_course):
    result = run_schedule_course(Solution, courses)
    result
    return (result,)


@app.cell
def _(assert_schedule_course, expected, result):
    assert_schedule_course(result, expected)
    return


if __name__ == "__main__":
    app.run()
