import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_grammar, run_kth_grammar
    from solution import Solution

    return Solution, assert_kth_grammar, run_kth_grammar


@app.cell
def _():
    # Example test case
    n = 1
    k = 1
    expected = 0
    return expected, k, n


@app.cell
def _(Solution, k, n, run_kth_grammar):
    result = run_kth_grammar(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_kth_grammar, expected, result):
    assert_kth_grammar(result, expected)
    return


if __name__ == "__main__":
    app.run()
