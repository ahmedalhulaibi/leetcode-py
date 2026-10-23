import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_letter_case_permutation, run_letter_case_permutation
    from solution import Solution

    return (
        Solution,
        assert_letter_case_permutation,
        run_letter_case_permutation,
    )


@app.cell
def _():
    # Example test case
    s = "a1b2"
    expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
    return expected, s


@app.cell
def _(Solution, run_letter_case_permutation, s):
    result = run_letter_case_permutation(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_letter_case_permutation, expected, result):
    assert_letter_case_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
