import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_encode, run_encode
    from solution import Solution

    return Solution, assert_encode, run_encode


@app.cell
def _():
    # Example test case
    s = "aaaaaaaaaa"
    expected_len = 5
    return expected_len, s


@app.cell
def _(Solution, run_encode, s):
    result = run_encode(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_encode, expected_len, result, s):
    assert_encode(result, s, expected_len)
    return


if __name__ == "__main__":
    app.run()
