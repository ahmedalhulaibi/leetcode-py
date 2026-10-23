import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_missing_element, run_missing_element
    from solution import Solution

    return Solution, assert_missing_element, run_missing_element


@app.cell
def _():
    # Example test case
    nums = [4, 7, 9, 10]
    k = 3
    expected = 8
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_missing_element):
    result = run_missing_element(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_missing_element, expected, result):
    assert_missing_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
