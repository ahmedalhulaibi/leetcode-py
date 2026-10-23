import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_job_scheduling, run_job_scheduling
    from solution import Solution

    return Solution, assert_job_scheduling, run_job_scheduling


@app.cell
def _():
    # Example test case
    start_time = [1, 2, 3, 3]
    end_time = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    expected = 120
    return end_time, expected, profit, start_time


@app.cell
def _(Solution, end_time, profit, run_job_scheduling, start_time):
    result = run_job_scheduling(Solution, start_time, end_time, profit)
    result
    return (result,)


@app.cell
def _(assert_job_scheduling, expected, result):
    assert_job_scheduling(result, expected)
    return


if __name__ == "__main__":
    app.run()
