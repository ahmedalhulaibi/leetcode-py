import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lru_cache, run_lru_cache
    from solution import LRUCache

    return LRUCache, assert_lru_cache, run_lru_cache


@app.cell
def _():
    # Example test case
    operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
    return expected, inputs, operations


@app.cell
def _(LRUCache, inputs, operations, run_lru_cache):
    result, cache = run_lru_cache(LRUCache, operations, inputs)
    print(result)
    cache
    return (result,)


@app.cell
def _(assert_lru_cache, expected, result):
    assert_lru_cache(result, expected)
    return


if __name__ == "__main__":
    app.run()
