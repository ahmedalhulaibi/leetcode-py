import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_sub_array_len, run_min_sub_array_len
    from solution import Solution

    return Solution, assert_min_sub_array_len, run_min_sub_array_len


@app.cell
def _():
    # Example test case
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = 2
    return expected, nums, target


@app.cell
def _(Solution, nums, run_min_sub_array_len, target):
    result = run_min_sub_array_len(Solution, target, nums)
    result
    return (result,)


@app.cell
def _(assert_min_sub_array_len, expected, result):
    assert_min_sub_array_len(result, expected)
    return


if __name__ == "__main__":
    app.run()
