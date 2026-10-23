import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_completing_word, run_shortest_completing_word
    from solution import Solution

    return (
        Solution,
        assert_shortest_completing_word,
        run_shortest_completing_word,
    )


@app.cell
def _():
    # Example test case
    license_plate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    expected = "steps"
    return expected, license_plate, words


@app.cell
def _(Solution, license_plate, run_shortest_completing_word, words):
    result = run_shortest_completing_word(Solution, license_plate, words)
    result
    return (result,)


@app.cell
def _(assert_shortest_completing_word, expected, result):
    assert_shortest_completing_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
