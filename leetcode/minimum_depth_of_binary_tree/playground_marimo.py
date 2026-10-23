import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_depth, run_min_depth
    from solution import Solution

    return Solution, assert_min_depth, run_min_depth


@app.cell
def _():
    # Example test case
    root_list = [3, 9, 20, None, None, 15, 7]
    expected = 2
    return expected, root_list


@app.cell
def _(Solution, root_list, run_min_depth):
    result = run_min_depth(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_min_depth, expected, result):
    assert_min_depth(result, expected)
    return


if __name__ == "__main__":
    app.run()
