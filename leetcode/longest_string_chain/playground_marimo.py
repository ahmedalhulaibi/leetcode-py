import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_str_chain, run_longest_str_chain
    from solution import Solution

    return Solution, assert_longest_str_chain, run_longest_str_chain


@app.cell
def _():
    # Example test case
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    expected = 4
    return expected, words


@app.cell
def _(Solution, run_longest_str_chain, words):
    result = run_longest_str_chain(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_longest_str_chain, expected, result):
    assert_longest_str_chain(result, expected)
    return


if __name__ == "__main__":
    app.run()
