import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_decode_string, run_decode_string
    from solution import Solution

    return Solution, assert_decode_string, run_decode_string


@app.cell
def _():
    # Example test case
    s = "3[a]2[bc]"
    expected = "aaabcbc"
    return expected, s


@app.cell
def _(Solution, run_decode_string, s):
    result = run_decode_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_decode_string, expected, result):
    assert_decode_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
