import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_k_similarity, run_k_similarity
    from solution import Solution

    return Solution, assert_k_similarity, run_k_similarity


@app.cell
def _():
    # Example test case
    s1 = "abc"
    s2 = "bca"
    expected = 2
    return expected, s1, s2


@app.cell
def _(Solution, run_k_similarity, s1, s2):
    result = run_k_similarity(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_k_similarity, expected, result):
    assert_k_similarity(result, expected)
    return


if __name__ == "__main__":
    app.run()
