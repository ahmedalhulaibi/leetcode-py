import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_depth, run_max_depth
    from solution import Solution

    return Solution, assert_max_depth, run_max_depth


@app.cell
def _():
    # Example test case
    root_list = [3, 9, 20, None, None, 15, 7]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list, run_max_depth):
    result = run_max_depth(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_max_depth, expected, result):
    assert_max_depth(result, expected)
    return


if __name__ == "__main__":
    app.run()
