import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_monotonic, run_is_monotonic
    from solution import Solution

    return Solution, assert_is_monotonic, run_is_monotonic


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2, 3]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_is_monotonic):
    result = run_is_monotonic(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_is_monotonic, expected, result):
    assert_is_monotonic(result, expected)
    return


if __name__ == "__main__":
    app.run()
