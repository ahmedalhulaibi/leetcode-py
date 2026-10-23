import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lfu_cache, run_lfu_cache
    from solution import LFUCache

    return LFUCache, assert_lfu_cache, run_lfu_cache


@app.cell
def _():
    # Example test case (operations, inputs, expected outputs)
    operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    expected = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
    return expected, inputs, operations


@app.cell
def _(LFUCache, inputs, operations, run_lfu_cache):
    result, cache = run_lfu_cache(LFUCache, operations, inputs)
    print(result)
    cache
    return (result,)


@app.cell
def _(assert_lfu_cache, expected, result):
    assert_lfu_cache(result, expected)
    return


if __name__ == "__main__":
    app.run()
