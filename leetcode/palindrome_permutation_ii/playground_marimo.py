import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_palindromes, run_generate_palindromes
    from solution import Solution

    return Solution, assert_generate_palindromes, run_generate_palindromes


@app.cell
def _():
    # Example test case
    s = "aabb"
    expected = ["abba", "baab"]
    return expected, s


@app.cell
def _(Solution, run_generate_palindromes, s):
    result = run_generate_palindromes(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_generate_palindromes, expected, result):
    assert_generate_palindromes(result, expected)
    return


if __name__ == "__main__":
    app.run()
