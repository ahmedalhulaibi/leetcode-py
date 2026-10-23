import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_time_taken, run_time_taken
    from solution import Solution

    return Solution, assert_time_taken, run_time_taken


@app.cell
def _():
    # Example test case
    arrival = [0, 1, 1, 2, 4]
    state = [0, 1, 0, 0, 1]
    expected = [0, 3, 1, 2, 4]
    return arrival, expected, state


@app.cell
def _(Solution, arrival, run_time_taken, state):
    result = run_time_taken(Solution, arrival, state)
    result
    return (result,)


@app.cell
def _(assert_time_taken, expected, result):
    assert_time_taken(result, expected)
    return


if __name__ == "__main__":
    app.run()
