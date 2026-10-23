import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_of_minutes, run_num_of_minutes
    from solution import Solution

    return Solution, assert_num_of_minutes, run_num_of_minutes


@app.cell
def _():
    # Example test case
    n = 6
    head_id = 2
    manager = [2, 2, -1, 2, 2, 2]
    inform_time = [0, 0, 1, 0, 0, 0]
    expected = 1
    return expected, head_id, inform_time, manager, n


@app.cell
def _(Solution, head_id, inform_time, manager, n, run_num_of_minutes):
    result = run_num_of_minutes(Solution, n, head_id, manager, inform_time)
    result
    return (result,)


@app.cell
def _(assert_num_of_minutes, expected, result):
    assert_num_of_minutes(result, expected)
    return


if __name__ == "__main__":
    app.run()
