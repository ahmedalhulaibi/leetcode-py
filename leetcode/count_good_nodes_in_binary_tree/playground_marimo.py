import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_good_nodes, run_good_nodes
    from solution import Solution

    return Solution, assert_good_nodes, run_good_nodes


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 1, 4, 3, None, 1, 5]
    expected = 4
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_good_nodes):
    result = run_good_nodes(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_good_nodes, expected, result):
    assert_good_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
