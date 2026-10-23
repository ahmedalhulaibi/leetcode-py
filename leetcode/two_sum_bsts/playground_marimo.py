import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_two_sum_bsts, run_two_sum_bsts
    from solution import Solution

    return Solution, assert_two_sum_bsts, run_two_sum_bsts


@app.cell
def _():
    # Example test case
    root1_list: list[int | None] = [2, 1, 4]
    root2_list: list[int | None] = [1, 0, 3]
    target = 5
    expected = True
    return expected, root1_list, root2_list, target


@app.cell
def _(
    Solution,
    root1_list: list[int | None],
    root2_list: list[int | None],
    run_two_sum_bsts,
    target,
):
    result = run_two_sum_bsts(Solution, root1_list, root2_list, target)
    result
    return (result,)


@app.cell
def _(assert_two_sum_bsts, expected, result):
    assert_two_sum_bsts(result, expected)
    return


if __name__ == "__main__":
    app.run()
