import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_distance_after_queries, run_shortest_distance_after_queries
    from solution import Solution

    return (
        Solution,
        assert_shortest_distance_after_queries,
        run_shortest_distance_after_queries,
    )


@app.cell
def _():
    # Example test case
    n = 5
    queries = [[2, 4], [0, 2], [0, 4]]
    expected = [3, 2, 1]
    return expected, n, queries


@app.cell
def _(Solution, n, queries, run_shortest_distance_after_queries):
    result = run_shortest_distance_after_queries(Solution, n, queries)
    result
    return (result,)


@app.cell
def _(assert_shortest_distance_after_queries, expected, result):
    assert_shortest_distance_after_queries(result, expected)
    return


if __name__ == "__main__":
    app.run()
