import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_of_substrings, run_count_of_substrings
    from solution import Solution

    return Solution, assert_count_of_substrings, run_count_of_substrings


@app.cell
def _():
    # Example test case
    word = "ieaouqqieaouqq"
    k = 1
    expected = 3
    return expected, k, word


@app.cell
def _(Solution, k, run_count_of_substrings, word):
    result = run_count_of_substrings(Solution, word, k)
    result
    return (result,)


@app.cell
def _(assert_count_of_substrings, expected, result):
    assert_count_of_substrings(result, expected)
    return


if __name__ == "__main__":
    app.run()
