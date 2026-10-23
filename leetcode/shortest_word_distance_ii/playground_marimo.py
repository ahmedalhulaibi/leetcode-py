import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_word_distance_ii, run_shortest_word_distance_ii
    from solution import WordDistance

    return (
        WordDistance,
        assert_shortest_word_distance_ii,
        run_shortest_word_distance_ii,
    )


@app.cell
def _():
    # Example test case
    operations = ["WordDistance", "shortest", "shortest"]
    inputs = [
        ["practice", "makes", "perfect", "coding", "makes"],
        ["coding", "practice"],
        ["makes", "coding"],
    ]
    expected = [None, 3, 1]
    return expected, inputs, operations


@app.cell
def _(WordDistance, inputs, operations, run_shortest_word_distance_ii):
    result, distance = run_shortest_word_distance_ii(WordDistance, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_shortest_word_distance_ii, expected, result):
    assert_shortest_word_distance_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
