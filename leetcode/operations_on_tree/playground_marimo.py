import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_operations_on_tree, run_operations_on_tree
    from solution import LockingTree

    return LockingTree, assert_operations_on_tree, run_operations_on_tree


@app.cell
def _():
    # Example test case
    operations = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
    inputs = [[-1, 0, 0, 1, 1, 2, 2], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
    expected = [None, True, False, True, True, True, False]
    return expected, inputs, operations


@app.cell
def _(LockingTree, inputs, operations, run_operations_on_tree):
    result, tree = run_operations_on_tree(LockingTree, operations, inputs)
    print(result)
    tree
    return (result,)


@app.cell
def _(assert_operations_on_tree, expected, result):
    assert_operations_on_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
