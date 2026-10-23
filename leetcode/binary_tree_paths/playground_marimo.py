import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_binary_tree_paths, run_binary_tree_paths
    from solution import Solution

    return Solution, assert_binary_tree_paths, run_binary_tree_paths


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, None, 5]
    expected: list[str] = ["1->2->5", "1->3"]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_binary_tree_paths):
    result = run_binary_tree_paths(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_binary_tree_paths, expected: list[str], result):
    assert_binary_tree_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
