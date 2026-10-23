import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sub_array_len, run_max_sub_array_len
    from solution import Solution

    return Solution, assert_max_sub_array_len, run_max_sub_array_len


@app.cell
def _():
    # Example test case
    nums = [1, -1, 5, -2, 3]
    k = 3
    expected = 4
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_max_sub_array_len):
    result = run_max_sub_array_len(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_max_sub_array_len, expected, result):
    assert_max_sub_array_len(result, expected)
    return


if __name__ == "__main__":
    app.run()
