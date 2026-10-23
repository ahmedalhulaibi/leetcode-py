import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import (
        assert_max_length_between_equal_characters,
        run_max_length_between_equal_characters,
    )
    from solution import Solution

    return (
        Solution,
        assert_max_length_between_equal_characters,
        run_max_length_between_equal_characters,
    )


@app.cell
def _():
    # Example test case
    s = "abca"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_max_length_between_equal_characters, s):
    result = run_max_length_between_equal_characters(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_max_length_between_equal_characters, expected, result):
    assert_max_length_between_equal_characters(result, expected)
    return


if __name__ == "__main__":
    app.run()
