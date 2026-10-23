import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_decode_at_index, run_decode_at_index
    from solution import Solution

    return Solution, assert_decode_at_index, run_decode_at_index


@app.cell
def _():
    # Example test case
    s = "leet2code3"
    k = 10
    expected = "o"
    return expected, k, s


@app.cell
def _(Solution, k, run_decode_at_index, s):
    result = run_decode_at_index(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_decode_at_index, expected, result):
    assert_decode_at_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
