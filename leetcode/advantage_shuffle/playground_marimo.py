import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_advantage_count, run_advantage_count
    from solution import Solution

    return Solution, assert_advantage_count, run_advantage_count


@app.cell
def _():
    # Example test case
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    expected = 4
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_advantage_count):
    result = run_advantage_count(Solution, nums1, nums2)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_advantage_count, expected, result):
    assert_advantage_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
