import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_xor_queries, run_xor_queries
    from solution import Solution

    return Solution, assert_xor_queries, run_xor_queries


@app.cell
def _():
    # Example test case
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    expected = [2, 7, 14, 8]
    return arr, expected, queries


@app.cell
def _(Solution, arr, queries, run_xor_queries):
    result = run_xor_queries(Solution, arr, queries)
    result
    return (result,)


@app.cell
def _(assert_xor_queries, expected, result):
    assert_xor_queries(result, expected)
    return


if __name__ == "__main__":
    app.run()
