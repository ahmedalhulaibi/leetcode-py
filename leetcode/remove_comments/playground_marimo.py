import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_comments, run_remove_comments
    from solution import Solution

    return Solution, assert_remove_comments, run_remove_comments


@app.cell
def _():
    # Example test case
    source = ["a/*comment", "line", "more_comment*/b"]
    expected = ["ab"]
    return expected, source


@app.cell
def _(Solution, expected, run_remove_comments, source):
    result = run_remove_comments(Solution, source, expected)
    result
    return (result,)


@app.cell
def _(assert_remove_comments, expected, result):
    assert_remove_comments(result, expected)
    return


if __name__ == "__main__":
    app.run()
