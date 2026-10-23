import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_decodings, run_num_decodings
    from solution import Solution

    return Solution, assert_num_decodings, run_num_decodings


@app.cell
def _():
    # Example test case
    s = "1*"
    expected = 18
    return expected, s


@app.cell
def _(Solution, run_num_decodings, s):
    result = run_num_decodings(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_num_decodings, expected, result):
    assert_num_decodings(result, expected)
    return


if __name__ == "__main__":
    app.run()
