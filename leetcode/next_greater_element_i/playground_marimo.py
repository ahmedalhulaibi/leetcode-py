import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_next_greater_element, run_next_greater_element
    from solution import Solution

    return Solution, assert_next_greater_element, run_next_greater_element


@app.cell
def _():
    # Example test case
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    expected = [-1, 3, -1]
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_next_greater_element):
    result = run_next_greater_element(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_next_greater_element, expected, result):
    assert_next_greater_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
