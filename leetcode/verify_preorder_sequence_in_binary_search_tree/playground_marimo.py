import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_verify_preorder, run_verify_preorder
    from solution import Solution

    return Solution, assert_verify_preorder, run_verify_preorder


@app.cell
def _():
    # Example test case
    preorder = [5, 2, 1, 3, 6]
    expected = True
    return expected, preorder


@app.cell
def _(Solution, preorder, run_verify_preorder):
    result = run_verify_preorder(Solution, preorder)
    result
    return (result,)


@app.cell
def _(assert_verify_preorder, expected, result):
    assert_verify_preorder(result, expected)
    return


if __name__ == "__main__":
    app.run()
