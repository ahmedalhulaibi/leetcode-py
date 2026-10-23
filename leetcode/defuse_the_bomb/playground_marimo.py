import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_decrypt, run_decrypt
    from solution import Solution

    return Solution, assert_decrypt, run_decrypt


@app.cell
def _():
    # Example test case
    code = [5, 7, 1, 4]
    k = 3
    expected = [12, 10, 16, 13]
    return code, expected, k


@app.cell
def _(Solution, code, k, run_decrypt):
    result = run_decrypt(Solution, code, k)
    result
    return (result,)


@app.cell
def _(assert_decrypt, expected, result):
    assert_decrypt(result, expected)
    return


if __name__ == "__main__":
    app.run()
