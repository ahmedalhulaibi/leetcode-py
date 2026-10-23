import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_trie_operations, run_trie_operations
    from solution import Trie

    return Trie, assert_trie_operations, run_trie_operations


@app.cell
def _():
    # Example test case
    operations = ["Trie", "insert", "search", "search", "starts_with", "insert", "search"]
    inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected = [None, None, True, False, True, None, True]
    return expected, inputs, operations


@app.cell
def _(Trie, inputs, operations, run_trie_operations):
    result, trie = run_trie_operations(Trie, operations, inputs)
    print(result)
    trie
    return (result,)


@app.cell
def _(assert_trie_operations, expected, result):
    assert_trie_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
