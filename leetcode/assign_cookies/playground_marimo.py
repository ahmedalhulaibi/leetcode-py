import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_content_children, run_find_content_children
    from solution import Solution

    return Solution, assert_find_content_children, run_find_content_children


@app.cell
def _():
    # Example test case
    g = [1, 2, 3]
    s = [1, 1]
    expected = 1
    return expected, g, s


@app.cell
def _(Solution, g, run_find_content_children, s):
    result = run_find_content_children(Solution, g, s)
    result
    return (result,)


@app.cell
def _(assert_find_content_children, expected, result):
    assert_find_content_children(result, expected)
    return


if __name__ == "__main__":
    app.run()
