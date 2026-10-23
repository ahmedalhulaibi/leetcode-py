import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_average_subtree, run_maximum_average_subtree
    from solution import Solution

    return (
        Solution,
        assert_maximum_average_subtree,
        run_maximum_average_subtree,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 6, 1]
    expected = 6.0
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_maximum_average_subtree):
    result = run_maximum_average_subtree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_maximum_average_subtree, expected, result):
    assert_maximum_average_subtree(result, expected)
    return


if __name__ == "__main__":
    app.run()
