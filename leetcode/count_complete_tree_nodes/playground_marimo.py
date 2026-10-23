import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_nodes, run_count_nodes
    from solution import Solution

    return Solution, assert_count_nodes, run_count_nodes


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5, 6]
    expected = 6
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_count_nodes):
    result = run_count_nodes(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_count_nodes, expected, result):
    assert_count_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
