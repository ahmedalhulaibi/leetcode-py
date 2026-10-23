import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_diameter_of_binary_tree, run_diameter_of_binary_tree
    from solution import Solution

    return (
        Solution,
        assert_diameter_of_binary_tree,
        run_diameter_of_binary_tree,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_diameter_of_binary_tree):
    result = run_diameter_of_binary_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_diameter_of_binary_tree, expected, result):
    assert_diameter_of_binary_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
