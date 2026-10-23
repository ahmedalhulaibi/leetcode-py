import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_mask_pii, run_mask_pii
    from solution import Solution

    return Solution, assert_mask_pii, run_mask_pii


@app.cell
def _():
    # Example test case
    s = "LeetCode@LeetCode.com"
    expected = "l*****e@leetcode.com"
    return expected, s


@app.cell
def _(Solution, run_mask_pii, s):
    result = run_mask_pii(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_mask_pii, expected, result):
    assert_mask_pii(result, expected)
    return


if __name__ == "__main__":
    app.run()
