import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_subfolders, run_remove_subfolders
    from solution import Solution

    return Solution, assert_remove_subfolders, run_remove_subfolders


@app.cell
def _():
    # Example test case
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    expected = ["/a", "/c/d", "/c/f"]
    return expected, folder


@app.cell
def _(Solution, folder, run_remove_subfolders):
    result = run_remove_subfolders(Solution, folder)
    result
    return (result,)


@app.cell
def _(assert_remove_subfolders, expected, result):
    assert_remove_subfolders(result, expected)
    return


if __name__ == "__main__":
    app.run()
