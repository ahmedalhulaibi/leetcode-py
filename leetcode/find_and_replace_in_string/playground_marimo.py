import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_replace_string, run_find_replace_string
    from solution import Solution

    return Solution, assert_find_replace_string, run_find_replace_string


@app.cell
def _():
    # Example test case
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    expected = "eeebffff"
    return expected, indices, s, sources, targets


@app.cell
def _(Solution, indices, run_find_replace_string, s, sources, targets):
    result = run_find_replace_string(Solution, s, indices, sources, targets)
    result
    return (result,)


@app.cell
def _(assert_find_replace_string, expected, result):
    assert_find_replace_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
