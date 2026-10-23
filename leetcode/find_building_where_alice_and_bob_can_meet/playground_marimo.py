import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_leftmost_building_queries, run_leftmost_building_queries
    from solution import Solution

    return (
        Solution,
        assert_leftmost_building_queries,
        run_leftmost_building_queries,
    )


@app.cell
def _():
    # Example test case
    heights = [6, 4, 8, 5, 2, 7]
    queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    expected = [2, 5, -1, 5, 2]
    return expected, heights, queries


@app.cell
def _(Solution, heights, queries, run_leftmost_building_queries):
    result = run_leftmost_building_queries(Solution, heights, queries)
    result
    return (result,)


@app.cell
def _(assert_leftmost_building_queries, expected, result):
    assert_leftmost_building_queries(result, expected)
    return


if __name__ == "__main__":
    app.run()
