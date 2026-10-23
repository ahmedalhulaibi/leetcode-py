import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_frequency, run_max_frequency
    from solution import Solution

    return Solution, assert_max_frequency, run_max_frequency


@app.cell
def _():
    # Example test case
    nums = [1, 2, 4]
    k = 5
    expected = 3
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_max_frequency):
    result = run_max_frequency(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_max_frequency, expected, result):
    assert_max_frequency(result, expected)
    return


if __name__ == "__main__":
    app.run()
