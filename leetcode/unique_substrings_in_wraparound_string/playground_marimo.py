import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import (
        assert_find_substring_in_wrapround_string,
        run_find_substring_in_wrapround_string,
    )
    from solution import Solution

    return (
        Solution,
        assert_find_substring_in_wrapround_string,
        run_find_substring_in_wrapround_string,
    )


@app.cell
def _():
    # Example test case
    s = "zab"
    expected = 6
    return expected, s


@app.cell
def _(Solution, run_find_substring_in_wrapround_string, s):
    result = run_find_substring_in_wrapround_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_find_substring_in_wrapround_string, expected, result):
    assert_find_substring_in_wrapround_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
