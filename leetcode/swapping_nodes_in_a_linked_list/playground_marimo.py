import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_swap_nodes, run_swap_nodes
    from solution import Solution

    return Solution, assert_swap_nodes, run_swap_nodes


@app.cell
def _():
    # Example test case
    head_list: list[int] = [1, 2, 3, 4, 5]
    k = 2
    expected: list[int] = [1, 4, 3, 2, 5]
    return expected, head_list, k


@app.cell
def _(Solution, head_list: list[int], k, run_swap_nodes):
    result = run_swap_nodes(Solution, head_list, k)
    result
    return (result,)


@app.cell
def _(assert_swap_nodes, expected: list[int], result):
    assert_swap_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
