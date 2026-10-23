import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_upside_down_binary_tree, run_upside_down_binary_tree
    from solution import Solution

    return (
        Solution,
        assert_upside_down_binary_tree,
        run_upside_down_binary_tree,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5]
    expected_list: list[int | None] = [4, 5, 2, None, None, 3, 1]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_upside_down_binary_tree):
    result = run_upside_down_binary_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_upside_down_binary_tree, expected_list: list[int | None], result):
    assert_upside_down_binary_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
