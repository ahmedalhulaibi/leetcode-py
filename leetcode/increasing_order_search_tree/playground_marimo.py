import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_increasing_bst, run_increasing_bst
    from solution import Solution

    return Solution, assert_increasing_bst, run_increasing_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    expected_list: list[int | None] = [
        1,
        None,
        2,
        None,
        3,
        None,
        4,
        None,
        5,
        None,
        6,
        None,
        7,
        None,
        8,
        None,
        9,
    ]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_increasing_bst):
    result = run_increasing_bst(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_increasing_bst, expected_list: list[int | None], result):
    assert_increasing_bst(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
