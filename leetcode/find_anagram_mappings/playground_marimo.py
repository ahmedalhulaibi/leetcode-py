import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_anagram_mappings, run_anagram_mappings
    from solution import Solution

    return Solution, assert_anagram_mappings, run_anagram_mappings


@app.cell
def _():
    # Example test case
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    expected = [1, 4, 3, 2, 0]
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_anagram_mappings):
    result = run_anagram_mappings(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_anagram_mappings, expected, result):
    assert_anagram_mappings(result, expected)
    return


if __name__ == "__main__":
    app.run()
