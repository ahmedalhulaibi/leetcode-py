import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_sub_path, run_is_sub_path
    from solution import Solution

    return Solution, assert_is_sub_path, run_is_sub_path


@app.cell
def _():
    # Example test case
    head_list: list[int] = [4, 2, 8]
    root_list: list[int | None] = [
        1,
        4,
        4,
        None,
        2,
        2,
        None,
        1,
        None,
        6,
        8,
        None,
        None,
        None,
        None,
        1,
        3,
    ]
    expected = True
    return expected, head_list, root_list


@app.cell
def _(
    Solution,
    head_list: list[int],
    root_list: list[int | None],
    run_is_sub_path,
):
    result = run_is_sub_path(Solution, head_list, root_list)
    result
    return (result,)


@app.cell
def _(assert_is_sub_path, expected, result):
    assert_is_sub_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
