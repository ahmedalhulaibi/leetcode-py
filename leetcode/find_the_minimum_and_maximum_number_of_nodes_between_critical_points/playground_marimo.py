import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nodes_between_critical_points, run_nodes_between_critical_points
    from solution import Solution

    return (
        Solution,
        assert_nodes_between_critical_points,
        run_nodes_between_critical_points,
    )


@app.cell
def _():
    # Example test case
    head_list = [5, 3, 1, 2, 5, 1, 2]
    expected = [1, 3]
    return expected, head_list


@app.cell
def _(Solution, head_list, run_nodes_between_critical_points):
    result = run_nodes_between_critical_points(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_nodes_between_critical_points, expected, result):
    assert_nodes_between_critical_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
