import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_unival_subtrees, run_count_unival_subtrees
    from solution import Solution

    return Solution, assert_count_unival_subtrees, run_count_unival_subtrees


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 1, 5, 5, 5, None, 5]
    expected = 4
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_count_unival_subtrees):
    result = run_count_unival_subtrees(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_count_unival_subtrees, expected, result):
    assert_count_unival_subtrees(result, expected)
    return


if __name__ == "__main__":
    app.run()
