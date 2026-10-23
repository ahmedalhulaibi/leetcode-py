import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_modified_list, run_modified_list
    from solution import Solution

    return Solution, assert_modified_list, run_modified_list


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 3]
    head_vals: list[int] = [1, 2, 3, 4, 5]
    expected_vals: list[int] = [4, 5]
    return expected_vals, head_vals, nums


@app.cell
def _(Solution, head_vals: list[int], nums: list[int], run_modified_list):
    result = run_modified_list(Solution, nums, head_vals)
    result
    return (result,)


@app.cell
def _(assert_modified_list, expected_vals: list[int], result):
    assert_modified_list(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
