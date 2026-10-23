import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_diameter_after_merge, run_minimum_diameter_after_merge
    from solution import Solution

    return (
        Solution,
        assert_minimum_diameter_after_merge,
        run_minimum_diameter_after_merge,
    )


@app.cell
def _():
    # Example test case
    edges1: list[list[int]] = [[0, 1], [0, 2], [0, 3]]
    edges2: list[list[int]] = [[0, 1]]
    expected = 3
    return edges1, edges2, expected


@app.cell
def _(
    Solution,
    edges1: list[list[int]],
    edges2: list[list[int]],
    run_minimum_diameter_after_merge,
):
    result = run_minimum_diameter_after_merge(Solution, edges1, edges2)
    result
    return (result,)


@app.cell
def _(assert_minimum_diameter_after_merge, expected, result):
    assert_minimum_diameter_after_merge(result, expected)
    return


if __name__ == "__main__":
    app.run()
