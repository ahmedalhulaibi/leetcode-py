import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_simplify_path, run_simplify_path
    from solution import Solution

    return Solution, assert_simplify_path, run_simplify_path


@app.cell
def _():
    # Example test case
    path = "/home/"
    expected = "/home"
    return expected, path


@app.cell
def _(Solution, path, run_simplify_path):
    result = run_simplify_path(Solution, path)
    result
    return (result,)


@app.cell
def _(assert_simplify_path, expected, result):
    assert_simplify_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
