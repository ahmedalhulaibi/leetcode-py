import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_majority_element, run_majority_element
    from solution import Solution

    return Solution, assert_majority_element, run_majority_element


@app.cell
def _():
    # Example test case
    nums = [3, 2, 3]
    expected = [3]
    return expected, nums


@app.cell
def _(Solution, nums, run_majority_element):
    result = run_majority_element(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_majority_element, expected, result):
    assert_majority_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
