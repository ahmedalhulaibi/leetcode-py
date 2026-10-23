import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_postorder, run_postorder
    from solution import Solution

    return Solution, assert_postorder, run_postorder


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    expected = [5, 6, 3, 2, 4, 1]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_postorder):
    result = run_postorder(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_postorder, expected, result):
    assert_postorder(result, expected)
    return


if __name__ == "__main__":
    app.run()
