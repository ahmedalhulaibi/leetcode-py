import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rearrange_string, run_rearrange_string
    from solution import Solution

    return Solution, assert_rearrange_string, run_rearrange_string


@app.cell
def _():
    # Example test case
    s = "aabbcc"
    k = 3
    return k, s


@app.cell
def _(Solution, k, run_rearrange_string, s):
    result = run_rearrange_string(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_rearrange_string, k, result, s):
    assert_rearrange_string(result, s, k)
    return


if __name__ == "__main__":
    app.run()
