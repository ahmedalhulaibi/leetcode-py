import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_right_side_view, run_right_side_view
    from solution import Solution

    return Solution, assert_right_side_view, run_right_side_view


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, None, 5, None, 4]
    expected = [1, 3, 4]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_right_side_view):
    result = run_right_side_view(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_right_side_view, expected, result):
    assert_right_side_view(result, expected)
    return


if __name__ == "__main__":
    app.run()
