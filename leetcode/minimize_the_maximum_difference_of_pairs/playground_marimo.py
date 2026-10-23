import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimize_max, run_minimize_max
    from solution import Solution

    return Solution, assert_minimize_max, run_minimize_max


@app.cell
def _():
    # Example test case
    nums = [10, 1, 2, 7, 1, 3]
    p = 2
    expected = 1
    return expected, nums, p


@app.cell
def _(Solution, nums, p, run_minimize_max):
    result = run_minimize_max(Solution, nums, p)
    result
    return (result,)


@app.cell
def _(assert_minimize_max, expected, result):
    assert_minimize_max(result, expected)
    return


if __name__ == "__main__":
    app.run()
