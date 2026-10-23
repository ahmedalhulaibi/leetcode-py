import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_uncommon_from_sentences, run_uncommon_from_sentences
    from solution import Solution

    return (
        Solution,
        assert_uncommon_from_sentences,
        run_uncommon_from_sentences,
    )


@app.cell
def _():
    # Example test case
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    expected = ["sweet", "sour"]
    return expected, s1, s2


@app.cell
def _(Solution, run_uncommon_from_sentences, s1, s2):
    result = run_uncommon_from_sentences(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_uncommon_from_sentences, expected, result):
    assert_uncommon_from_sentences(result, expected)
    return


if __name__ == "__main__":
    app.run()
