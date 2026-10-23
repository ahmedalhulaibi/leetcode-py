import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_evaluate_tree, run_evaluate_tree
    from solution import Solution

    return Solution, assert_evaluate_tree, run_evaluate_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 1, 3, None, None, 0, 1]
    expected = True
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_evaluate_tree):
    result = run_evaluate_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_evaluate_tree, expected, result):
    assert_evaluate_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
