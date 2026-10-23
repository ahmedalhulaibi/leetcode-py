import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_encode_decode, run_encode_decode
    from solution import Solution

    return Solution, assert_encode_decode, run_encode_decode


@app.cell
def _():
    # Example test case
    strs = ["Hello", "World"]
    expected = strs
    return expected, strs


@app.cell
def _(Solution, run_encode_decode, strs):
    result = run_encode_decode(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_encode_decode, expected, result):
    assert_encode_decode(result, expected)
    return


if __name__ == "__main__":
    app.run()
