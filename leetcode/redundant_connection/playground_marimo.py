import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_redundant_connection, run_find_redundant_connection
    from solution import Solution

    return (
        Solution,
        assert_find_redundant_connection,
        run_find_redundant_connection,
    )


@app.cell
def _():
    # Example test case
    edges = [[1, 2], [1, 3], [2, 3]]
    expected = [2, 3]
    return edges, expected


@app.cell
def _(Solution, edges, run_find_redundant_connection):
    result = run_find_redundant_connection(Solution, edges)
    result
    return (result,)


@app.cell
def _(assert_find_redundant_connection, expected, result):
    assert_find_redundant_connection(result, expected)
    return


if __name__ == "__main__":
    app.run()
