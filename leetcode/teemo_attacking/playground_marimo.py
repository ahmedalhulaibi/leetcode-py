import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_poisoned_duration, run_find_poisoned_duration
    from solution import Solution

    return Solution, assert_find_poisoned_duration, run_find_poisoned_duration


@app.cell
def _():
    # Example test case
    time_series: list[int] = [1, 4]
    duration = 2
    expected = 4
    return duration, expected, time_series


@app.cell
def _(Solution, duration, run_find_poisoned_duration, time_series: list[int]):
    result = run_find_poisoned_duration(Solution, time_series, duration)
    result
    return (result,)


@app.cell
def _(assert_find_poisoned_duration, expected, result):
    assert_find_poisoned_duration(result, expected)
    return


if __name__ == "__main__":
    app.run()
