import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_all_paths_source_target, run_all_paths_source_target
    from solution import Solution

    return (
        Solution,
        assert_all_paths_source_target,
        run_all_paths_source_target,
    )


@app.cell
def _():
    # Example test case
    graph = [[1, 2], [3], [3], []]
    expected = [[0, 1, 3], [0, 2, 3]]
    return expected, graph


@app.cell
def _(Solution, graph, run_all_paths_source_target):
    result = run_all_paths_source_target(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_all_paths_source_target, expected, result):
    assert_all_paths_source_target(result, expected)
    return


if __name__ == "__main__":
    app.run()
