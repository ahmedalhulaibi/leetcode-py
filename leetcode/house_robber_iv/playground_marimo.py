import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_capability, run_min_capability
    from solution import Solution

    return Solution, assert_min_capability, run_min_capability


@app.cell
def _():
    # Example test case
    nums = [2, 3, 5, 9]
    k = 2
    expected = 5
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_min_capability):
    result = run_min_capability(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_min_capability, expected, result):
    assert_min_capability(result, expected)
    return


if __name__ == "__main__":
    app.run()
