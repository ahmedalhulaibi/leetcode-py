import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_preimage_size_fzf, run_preimage_size_fzf
    from solution import Solution

    return Solution, assert_preimage_size_fzf, run_preimage_size_fzf


@app.cell
def _():
    # Example test case
    k = 0
    expected = 5
    return expected, k


@app.cell
def _(Solution, k, run_preimage_size_fzf):
    result = run_preimage_size_fzf(Solution, k)
    result
    return (result,)


@app.cell
def _(assert_preimage_size_fzf, expected, result):
    assert_preimage_size_fzf(result, expected)
    return


if __name__ == "__main__":
    app.run()
