import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hash_set, run_hash_set
    from solution import MyHashSet

    return MyHashSet, assert_hash_set, run_hash_set


@app.cell
def _():
    # Example test case
    operations = [
        "MyHashSet",
        "add",
        "add",
        "contains",
        "contains",
        "add",
        "contains",
        "remove",
        "contains",
    ]
    inputs = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    expected = [None, None, None, True, False, None, True, None, False]
    return expected, inputs, operations


@app.cell
def _(MyHashSet, inputs, operations, run_hash_set):
    result, hash_set = run_hash_set(MyHashSet, operations, inputs)
    print(result)
    hash_set
    return (result,)


@app.cell
def _(assert_hash_set, expected, result):
    assert_hash_set(result, expected)
    return


if __name__ == "__main__":
    app.run()
