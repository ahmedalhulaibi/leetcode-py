import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_students, run_count_students
    from solution import Solution

    return Solution, assert_count_students, run_count_students


@app.cell
def _():
    # Example test case
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    expected = 0
    return expected, sandwiches, students


@app.cell
def _(Solution, run_count_students, sandwiches, students):
    result = run_count_students(Solution, students, sandwiches)
    result
    return (result,)


@app.cell
def _(assert_count_students, expected, result):
    assert_count_students(result, expected)
    return


if __name__ == "__main__":
    app.run()
