import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_deck_revealed_increasing, run_deck_revealed_increasing
    from solution import Solution

    return (
        Solution,
        assert_deck_revealed_increasing,
        run_deck_revealed_increasing,
    )


@app.cell
def _():
    # Example test case
    deck = [17, 13, 11, 2, 3, 5, 7]
    expected = [2, 13, 3, 11, 5, 17, 7]
    return deck, expected


@app.cell
def _(Solution, deck, run_deck_revealed_increasing):
    result = run_deck_revealed_increasing(Solution, deck)
    result
    return (result,)


@app.cell
def _(assert_deck_revealed_increasing, expected, result):
    assert_deck_revealed_increasing(result, expected)
    return


if __name__ == "__main__":
    app.run()
