import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subsets_with_dup, run_subsets_with_dup
    from solution import Solution

    return Solution, assert_subsets_with_dup, run_subsets_with_dup


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2]
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    return expected, nums


@app.cell
def _(Solution, nums, run_subsets_with_dup):
    result = run_subsets_with_dup(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_subsets_with_dup, expected, result):
    assert_subsets_with_dup(result, expected)
    return


if __name__ == "__main__":
    app.run()
