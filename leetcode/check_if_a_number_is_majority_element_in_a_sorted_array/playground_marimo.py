import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_majority_element, run_is_majority_element
    from solution import Solution

    return Solution, assert_is_majority_element, run_is_majority_element


@app.cell
def _():
    # Example test case
    nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
    target = 5
    expected = True
    return expected, nums, target


@app.cell
def _(Solution, nums, run_is_majority_element, target):
    result = run_is_majority_element(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_is_majority_element, expected, result):
    assert_is_majority_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
