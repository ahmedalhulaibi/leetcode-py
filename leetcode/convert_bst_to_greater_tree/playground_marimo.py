import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_convert_bst, run_convert_bst
    from solution import Solution

    return Solution, assert_convert_bst, run_convert_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    expected_list: list[int | None] = [
        30,
        36,
        21,
        36,
        35,
        26,
        15,
        None,
        None,
        None,
        33,
        None,
        None,
        None,
        8,
    ]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_convert_bst):
    result = run_convert_bst(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_convert_bst, expected_list: list[int | None], result):
    assert_convert_bst(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
