import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_interleave, run_is_interleave
    from solution import Solution

    return Solution, assert_is_interleave, run_is_interleave


@app.cell
def _():
    # Example test case
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    expected = True
    return expected, s1, s2, s3


@app.cell
def _(Solution, run_is_interleave, s1, s2, s3):
    result = run_is_interleave(Solution, s1, s2, s3)
    result
    return (result,)


@app.cell
def _(assert_is_interleave, expected, result):
    assert_is_interleave(result, expected)
    return


if __name__ == "__main__":
    app.run()
