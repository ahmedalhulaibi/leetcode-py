import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_daily_temperatures, run_daily_temperatures
    from solution import Solution

    return Solution, assert_daily_temperatures, run_daily_temperatures


@app.cell
def _():
    # Example test case
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    return expected, temperatures


@app.cell
def _(Solution, run_daily_temperatures, temperatures):
    result = run_daily_temperatures(Solution, temperatures)
    result
    return (result,)


@app.cell
def _(assert_daily_temperatures, expected, result):
    assert_daily_temperatures(result, expected)
    return


if __name__ == "__main__":
    app.run()
