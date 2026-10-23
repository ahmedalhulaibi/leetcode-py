import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_array_strings_are_equal, run_array_strings_are_equal
    from solution import Solution

    return (
        Solution,
        assert_array_strings_are_equal,
        run_array_strings_are_equal,
    )


@app.cell
def _():
    # Example test case
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    expected = True
    return expected, word1, word2


@app.cell
def _(Solution, run_array_strings_are_equal, word1, word2):
    result = run_array_strings_are_equal(Solution, word1, word2)
    result
    return (result,)


@app.cell
def _(assert_array_strings_are_equal, expected, result):
    assert_array_strings_are_equal(result, expected)
    return


if __name__ == "__main__":
    app.run()
