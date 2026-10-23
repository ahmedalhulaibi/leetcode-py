import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_vowel_permutation, run_count_vowel_permutation
    from solution import Solution

    return (
        Solution,
        assert_count_vowel_permutation,
        run_count_vowel_permutation,
    )


@app.cell
def _():
    # Example test case
    n = 5
    expected = 68
    return expected, n


@app.cell
def _(Solution, n, run_count_vowel_permutation):
    result = run_count_vowel_permutation(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_vowel_permutation, expected, result):
    assert_count_vowel_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
