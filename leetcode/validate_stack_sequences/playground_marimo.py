import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_validate_stack_sequences, run_validate_stack_sequences
    from solution import Solution

    return (
        Solution,
        assert_validate_stack_sequences,
        run_validate_stack_sequences,
    )


@app.cell
def _():
    # Example test case
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    expected = True
    return expected, popped, pushed


@app.cell
def _(Solution, popped, pushed, run_validate_stack_sequences):
    result = run_validate_stack_sequences(Solution, pushed, popped)
    result
    return (result,)


@app.cell
def _(assert_validate_stack_sequences, expected, result):
    assert_validate_stack_sequences(result, expected)
    return


if __name__ == "__main__":
    app.run()
