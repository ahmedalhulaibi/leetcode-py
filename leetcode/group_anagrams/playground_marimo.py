import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_group_anagrams, run_group_anagrams
    from solution import Solution

    return Solution, assert_group_anagrams, run_group_anagrams


@app.cell
def _():
    # Example test case
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    return expected, strs


@app.cell
def _(Solution, run_group_anagrams, strs):
    result = run_group_anagrams(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_group_anagrams, expected, result):
    assert_group_anagrams(result, expected)
    return


if __name__ == "__main__":
    app.run()
