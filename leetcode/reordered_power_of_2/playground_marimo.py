import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reordered_power_of_2, run_reordered_power_of_2
    from solution import Solution

    return Solution, assert_reordered_power_of_2, run_reordered_power_of_2


@app.cell
def _():
    # Example test case
    n = 1
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_reordered_power_of_2):
    result = run_reordered_power_of_2(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_reordered_power_of_2, expected, result):
    assert_reordered_power_of_2(result, expected)
    return


if __name__ == "__main__":
    app.run()
