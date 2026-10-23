import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_copy_random_list, run_copy_random_list
    from solution import Solution

    return Solution, assert_copy_random_list, run_copy_random_list


@app.cell
def _():
    # Example test case (each node is [val, random_index])
    nodes = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    expected = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    return expected, nodes


@app.cell
def _(Solution, nodes, run_copy_random_list):
    result = run_copy_random_list(Solution, nodes)
    result
    return (result,)


@app.cell
def _(assert_copy_random_list, expected, result):
    assert_copy_random_list(result, expected)
    return


if __name__ == "__main__":
    app.run()
