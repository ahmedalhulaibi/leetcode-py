import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_length_of_optimal_compression, run_get_length_of_optimal_compression
    from solution import Solution

    return (
        Solution,
        assert_get_length_of_optimal_compression,
        run_get_length_of_optimal_compression,
    )


@app.cell
def _():
    # Example test case
    s = "aaabcccd"
    k = 2
    expected = 4
    return expected, k, s


@app.cell
def _(Solution, k, run_get_length_of_optimal_compression, s):
    result = run_get_length_of_optimal_compression(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_get_length_of_optimal_compression, expected, result):
    assert_get_length_of_optimal_compression(result, expected)
    return


if __name__ == "__main__":
    app.run()
