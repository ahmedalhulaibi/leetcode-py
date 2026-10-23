import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_common_supersequence, run_shortest_common_supersequence
    from solution import Solution

    return (
        Solution,
        assert_shortest_common_supersequence,
        run_shortest_common_supersequence,
    )


@app.cell
def _():
    # Example test case
    str1 = "abac"
    str2 = "cab"
    expected_length = 5
    return expected_length, str1, str2


@app.cell
def _(Solution, run_shortest_common_supersequence, str1, str2):
    result = run_shortest_common_supersequence(Solution, str1, str2)
    result
    return (result,)


@app.cell
def _(
    assert_shortest_common_supersequence,
    expected_length,
    result,
    str1,
    str2,
):
    assert_shortest_common_supersequence(result, str1, str2, expected_length)
    return


if __name__ == "__main__":
    app.run()
