import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_next_closest_time, run_next_closest_time
    from solution import Solution

    return Solution, assert_next_closest_time, run_next_closest_time


@app.cell
def _():
    # Example test case
    time = "19:34"
    expected = "19:39"
    return expected, time


@app.cell
def _(Solution, run_next_closest_time, time):
    result = run_next_closest_time(Solution, time)
    result
    return (result,)


@app.cell
def _(assert_next_closest_time, expected, result):
    assert_next_closest_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
