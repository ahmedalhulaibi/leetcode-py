import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_similar_groups, run_num_similar_groups
    from solution import Solution

    return Solution, assert_num_similar_groups, run_num_similar_groups


@app.cell
def _():
    # Example test case
    strs = ["tars", "rats", "arts", "star"]
    expected = 2
    return expected, strs


@app.cell
def _(Solution, run_num_similar_groups, strs):
    result = run_num_similar_groups(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_num_similar_groups, expected, result):
    assert_num_similar_groups(result, expected)
    return


if __name__ == "__main__":
    app.run()
