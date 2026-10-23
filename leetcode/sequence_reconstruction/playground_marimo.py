import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sequence_reconstruction, run_sequence_reconstruction
    from solution import Solution

    return (
        Solution,
        assert_sequence_reconstruction,
        run_sequence_reconstruction,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    sequences = [[1, 2], [1, 3], [2, 3]]
    expected = True
    return expected, nums, sequences


@app.cell
def _(Solution, nums, run_sequence_reconstruction, sequences):
    result = run_sequence_reconstruction(Solution, nums, sequences)
    result
    return (result,)


@app.cell
def _(assert_sequence_reconstruction, expected, result):
    assert_sequence_reconstruction(result, expected)
    return


if __name__ == "__main__":
    app.run()
