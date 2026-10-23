import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_duplicate_subtrees, run_find_duplicate_subtrees
    from solution import Solution

    return (
        Solution,
        assert_find_duplicate_subtrees,
        run_find_duplicate_subtrees,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 1, 1]
    expected: list[list[int | None]] = [[1]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_duplicate_subtrees):
    result = run_find_duplicate_subtrees(Solution, root_list)
    result
    return (result,)


@app.cell
def _(
    assert_find_duplicate_subtrees,
    expected: list[list[int | None]],
    result,
):
    assert_find_duplicate_subtrees(result, expected)
    return


if __name__ == "__main__":
    app.run()
