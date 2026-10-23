import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_largest_level_sum, run_kth_largest_level_sum
    from solution import Solution

    return Solution, assert_kth_largest_level_sum, run_kth_largest_level_sum


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 8, 9, 2, 1, 3, 7, 4, 6]
    k = 2
    expected = 13
    return expected, k, root_list


@app.cell
def _(Solution, k, root_list: list[int | None], run_kth_largest_level_sum):
    result = run_kth_largest_level_sum(Solution, root_list, k)
    result
    return (result,)


@app.cell
def _(assert_kth_largest_level_sum, expected, result):
    assert_kth_largest_level_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
