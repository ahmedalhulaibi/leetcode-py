import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_maximum_binary_tree, run_construct_maximum_binary_tree
    from solution import Solution

    return (
        Solution,
        assert_construct_maximum_binary_tree,
        run_construct_maximum_binary_tree,
    )


@app.cell
def _():
    # Example test case
    nums: list[int] = [3, 2, 1, 6, 0, 5]
    expected_list: list[int | None] = [6, 3, 5, None, 2, 0, None, None, 1]
    return expected_list, nums


@app.cell
def _(Solution, nums: list[int], run_construct_maximum_binary_tree):
    result = run_construct_maximum_binary_tree(Solution, nums)
    result
    return (result,)


@app.cell
def _(
    assert_construct_maximum_binary_tree,
    expected_list: list[int | None],
    result,
):
    assert_construct_maximum_binary_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
