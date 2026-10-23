import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_unique_morse_representations, run_unique_morse_representations
    from solution import Solution

    return (
        Solution,
        assert_unique_morse_representations,
        run_unique_morse_representations,
    )


@app.cell
def _():
    # Example test case
    words = ["gin", "zen", "gig", "msg"]
    expected = 2
    return expected, words


@app.cell
def _(Solution, run_unique_morse_representations, words):
    result = run_unique_morse_representations(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_unique_morse_representations, expected, result):
    assert_unique_morse_representations(result, expected)
    return


if __name__ == "__main__":
    app.run()
