import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_one_row, run_add_one_row
    from solution import Solution

    return Solution, assert_add_one_row, run_add_one_row


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 6, 3, 1, 5]
    val = 1
    depth = 2
    expected_list: list[int | None] = [4, 1, 1, 2, None, None, 6, 3, 1, 5]
    return depth, expected_list, root_list, val


@app.cell
def _(Solution, depth, root_list: list[int | None], run_add_one_row, val):
    result = run_add_one_row(Solution, root_list, val, depth)
    result
    return (result,)


@app.cell
def _(assert_add_one_row, expected_list: list[int | None], result):
    assert_add_one_row(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
