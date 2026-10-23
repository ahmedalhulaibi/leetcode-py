import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_employee_free_time, run_employee_free_time
    from solution import Solution

    return Solution, assert_employee_free_time, run_employee_free_time


@app.cell
def _():
    # Example test case
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    expected = [[3, 4]]
    return expected, schedule


@app.cell
def _(Solution, run_employee_free_time, schedule):
    result = run_employee_free_time(Solution, schedule)
    result
    return (result,)


@app.cell
def _(assert_employee_free_time, expected, result):
    assert_employee_free_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
