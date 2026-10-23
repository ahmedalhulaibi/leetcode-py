import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_spellchecker, run_spellchecker
    from solution import Solution

    return Solution, assert_spellchecker, run_spellchecker


@app.cell
def _():
    # Example test case
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite"]
    expected = ["kite", "KiTe"]
    return expected, queries, wordlist


@app.cell
def _(Solution, queries, run_spellchecker, wordlist):
    result = run_spellchecker(Solution, wordlist, queries)
    result
    return (result,)


@app.cell
def _(assert_spellchecker, expected, result):
    assert_spellchecker(result, expected)
    return


if __name__ == "__main__":
    app.run()
