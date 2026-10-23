import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_compress, run_compress
    from solution import Solution

    return Solution, assert_compress, run_compress


@app.cell
def _():
    # Example test case
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    expected = ["a", "2", "b", "2", "c", "3"]
    return chars, expected


@app.cell
def _(Solution, chars, run_compress):
    result = run_compress(Solution, chars)
    result
    return (result,)


@app.cell
def _(assert_compress, expected, result):
    assert_compress(result, expected)
    return


if __name__ == "__main__":
    app.run()
