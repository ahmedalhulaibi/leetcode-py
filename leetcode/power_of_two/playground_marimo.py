import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_power_of_two, run_is_power_of_two
    from solution import Solution

    return Solution, assert_is_power_of_two, run_is_power_of_two


@app.cell
def _():
    # Example test case
    n = 16
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_is_power_of_two):
    result = run_is_power_of_two(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_is_power_of_two, expected, result):
    assert_is_power_of_two(result, expected)
    return


if __name__ == "__main__":
    app.run()
