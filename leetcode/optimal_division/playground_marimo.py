import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_optimal_division, run_optimal_division
    from solution import Solution

    return Solution, assert_optimal_division, run_optimal_division


@app.cell
def _():
    # Example test case
    nums = [1000, 100, 10, 2]
    expected = "1000/(100/10/2)"
    return expected, nums


@app.cell
def _(Solution, nums, run_optimal_division):
    result = run_optimal_division(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_optimal_division, expected, result):
    assert_optimal_division(result, expected)
    return


if __name__ == "__main__":
    app.run()
