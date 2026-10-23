import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_vowel_strings, run_vowel_strings
    from solution import Solution

    return Solution, assert_vowel_strings, run_vowel_strings


@app.cell
def _():
    # Example test case
    words: list[str] = ["aba", "bcb", "ece", "aa", "e"]
    queries: list[list[int]] = [[0, 2], [1, 4], [1, 1]]
    expected: list[int] = [2, 3, 0]
    return expected, queries, words


@app.cell
def _(Solution, queries: list[list[int]], run_vowel_strings, words: list[str]):
    result = run_vowel_strings(Solution, words, queries)
    result
    return (result,)


@app.cell
def _(assert_vowel_strings, expected: list[int], result):
    assert_vowel_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
