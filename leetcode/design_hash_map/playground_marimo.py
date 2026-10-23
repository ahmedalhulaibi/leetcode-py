import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hash_map, run_hash_map
    from solution import MyHashMap

    return MyHashMap, assert_hash_map, run_hash_map


@app.cell
def _():
    # Example test case
    operations = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    inputs = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    expected = [None, None, None, 1, -1, None, 1, None, -1]
    return expected, inputs, operations


@app.cell
def _(MyHashMap, inputs, operations, run_hash_map):
    result, hash_map = run_hash_map(MyHashMap, operations, inputs)
    print(result)
    hash_map
    return (result,)


@app.cell
def _(assert_hash_map, expected, result):
    assert_hash_map(result, expected)
    return


if __name__ == "__main__":
    app.run()
