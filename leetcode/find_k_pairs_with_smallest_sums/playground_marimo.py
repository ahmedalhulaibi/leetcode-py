import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_k_smallest_pairs, run_k_smallest_pairs
    from solution import Solution

    return Solution, assert_k_smallest_pairs, run_k_smallest_pairs


@app.cell
def _():
    # Example test case
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected = [[1, 2], [1, 4], [1, 6]]
    return expected, k, nums1, nums2


@app.cell
def _(Solution, k, nums1, nums2, run_k_smallest_pairs):
    result = run_k_smallest_pairs(Solution, nums1, nums2, k)
    result
    return (result,)


@app.cell
def _(assert_k_smallest_pairs, expected, result):
    assert_k_smallest_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
