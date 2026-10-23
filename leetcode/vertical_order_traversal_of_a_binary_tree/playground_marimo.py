import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_vertical_traversal, run_vertical_traversal
    from solution import Solution

    return Solution, assert_vertical_traversal, run_vertical_traversal


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected_list: list[list[int]] = [[9], [3, 15], [20], [7]]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_vertical_traversal):
    result = run_vertical_traversal(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_vertical_traversal, expected_list: list[list[int]], result):
    assert_vertical_traversal(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
