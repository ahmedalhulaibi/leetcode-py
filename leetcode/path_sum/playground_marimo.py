import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_path_sum, run_has_path_sum
    from solution import Solution

    return Solution, assert_has_path_sum, run_has_path_sum


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    target_sum: int = 22
    expected: bool = True
    return expected, root_list, target_sum


@app.cell
def _(
    Solution,
    root_list: list[int | None],
    run_has_path_sum,
    target_sum: int,
):
    result = run_has_path_sum(Solution, root_list, target_sum)
    result
    return (result,)


@app.cell
def _(assert_has_path_sum, expected: bool, result):
    assert_has_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
