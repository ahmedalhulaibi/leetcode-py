import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_element, run_remove_element
    from solution import Solution

    return Solution, assert_remove_element, run_remove_element


@app.cell
def _():
    # Example test case
    nums = [3, 2, 2, 3]
    val = 3
    expected = (2, [2, 2])
    return expected, nums, val


@app.cell
def _(Solution, nums, run_remove_element, val):
    result = run_remove_element(Solution, nums, val)
    result
    return (result,)


@app.cell
def _(assert_remove_element, expected, result):
    assert_remove_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
