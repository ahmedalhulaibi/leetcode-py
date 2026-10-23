import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_duplicate_letters, run_remove_duplicate_letters
    from solution import Solution

    return (
        Solution,
        assert_remove_duplicate_letters,
        run_remove_duplicate_letters,
    )


@app.cell
def _():
    # Example test case
    s = "cbacdcbc"
    expected = "acdb"
    return expected, s


@app.cell
def _(Solution, run_remove_duplicate_letters, s):
    result = run_remove_duplicate_letters(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_remove_duplicate_letters, expected, result):
    assert_remove_duplicate_letters(result, expected)
    return


if __name__ == "__main__":
    app.run()
