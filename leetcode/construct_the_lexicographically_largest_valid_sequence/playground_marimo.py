import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_distanced_sequence, run_construct_distanced_sequence
    from solution import Solution

    return (
        Solution,
        assert_construct_distanced_sequence,
        run_construct_distanced_sequence,
    )


@app.cell
def _():
    # Example test case
    n = 3
    expected = [3, 1, 2, 3, 2]
    return expected, n


@app.cell
def _(Solution, n, run_construct_distanced_sequence):
    result = run_construct_distanced_sequence(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_construct_distanced_sequence, expected, result):
    assert_construct_distanced_sequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
