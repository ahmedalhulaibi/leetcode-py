import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_kelements, run_max_kelements
    from solution import Solution

    return Solution, assert_max_kelements, run_max_kelements


@app.cell
def _():
    # Example test case
    nums = [1, 10, 3, 3, 3]
    k = 3
    expected = 17
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_max_kelements):
    result = run_max_kelements(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_max_kelements, expected, result):
    assert_max_kelements(result, expected)
    return


if __name__ == "__main__":
    app.run()
