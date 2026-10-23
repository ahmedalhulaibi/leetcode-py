import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_preorder_traversal, run_preorder_traversal
    from solution import Solution

    return Solution, assert_preorder_traversal, run_preorder_traversal


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 2, 3]
    expected: list[int] = [1, 2, 3]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_preorder_traversal):
    result = run_preorder_traversal(Solution, root_list)
    print(f"Preorder traversal: {result}")
    result
    return (result,)


@app.cell
def _(assert_preorder_traversal, expected: list[int], result):
    assert_preorder_traversal(result, expected)
    return


if __name__ == "__main__":
    app.run()
