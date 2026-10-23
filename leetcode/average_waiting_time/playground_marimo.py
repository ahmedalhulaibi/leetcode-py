import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_average_waiting_time, run_average_waiting_time
    from solution import Solution

    return Solution, assert_average_waiting_time, run_average_waiting_time


@app.cell
def _():
    # Example test case
    customers: list[list[int]] = [[1, 2], [2, 5], [4, 3]]
    expected = 5.0
    return customers, expected


@app.cell
def _(Solution, customers: list[list[int]], run_average_waiting_time):
    result = run_average_waiting_time(Solution, customers)
    result
    return (result,)


@app.cell
def _(assert_average_waiting_time, expected, result):
    assert_average_waiting_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
