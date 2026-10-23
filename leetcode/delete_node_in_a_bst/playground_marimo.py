import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_node, run_delete_node
    from solution import Solution

    return Solution, assert_delete_node, run_delete_node


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 3, 6, 2, 4, None, 7]
    key = 3
    expected = [2, 4, 5, 6, 7]
    return expected, key, root_list


@app.cell
def _(Solution, key, root_list: list[int | None], run_delete_node):
    result = run_delete_node(Solution, root_list, key)
    result
    return (result,)


@app.cell
def _(assert_delete_node, expected, result):
    assert_delete_node(result, expected)
    return


if __name__ == "__main__":
    app.run()
