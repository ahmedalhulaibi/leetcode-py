import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_available_duration, run_min_available_duration
    from solution import Solution

    return Solution, assert_min_available_duration, run_min_available_duration


@app.cell
def _():
    # Example test case
    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 8
    expected = [60, 68]
    return duration, expected, slots1, slots2


@app.cell
def _(Solution, duration, run_min_available_duration, slots1, slots2):
    result = run_min_available_duration(Solution, slots1, slots2, duration)
    result
    return (result,)


@app.cell
def _(assert_min_available_duration, expected, result):
    assert_min_available_duration(result, expected)
    return


if __name__ == "__main__":
    app.run()
