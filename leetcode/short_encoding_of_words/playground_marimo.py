import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_length_encoding, run_minimum_length_encoding
    from solution import Solution

    return (
        Solution,
        assert_minimum_length_encoding,
        run_minimum_length_encoding,
    )


@app.cell
def _():
    # Example test case
    words = ["time", "me", "bell"]
    expected = 10
    return expected, words


@app.cell
def _(Solution, run_minimum_length_encoding, words):
    result = run_minimum_length_encoding(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_minimum_length_encoding, expected, result):
    assert_minimum_length_encoding(result, expected)
    return


if __name__ == "__main__":
    app.run()
