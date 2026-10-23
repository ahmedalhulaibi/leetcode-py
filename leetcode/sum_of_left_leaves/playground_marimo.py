import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_of_left_leaves, run_sum_of_left_leaves
    from solution import Solution

    return Solution, assert_sum_of_left_leaves, run_sum_of_left_leaves


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected = 24
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_sum_of_left_leaves):
    result = run_sum_of_left_leaves(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_sum_of_left_leaves, expected, result):
    assert_sum_of_left_leaves(result, expected)
    return


if __name__ == "__main__":
    app.run()
