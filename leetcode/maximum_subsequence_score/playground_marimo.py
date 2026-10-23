import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_score, run_max_score
    from solution import Solution

    return Solution, assert_max_score, run_max_score


@app.cell
def _():
    # Example test case
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    expected = 12
    return expected, k, nums1, nums2


@app.cell
def _(Solution, k, nums1, nums2, run_max_score):
    result = run_max_score(Solution, nums1, nums2, k)
    result
    return (result,)


@app.cell
def _(assert_max_score, expected, result):
    assert_max_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
