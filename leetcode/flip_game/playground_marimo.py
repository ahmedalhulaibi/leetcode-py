import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_possible_next_moves, run_generate_possible_next_moves
    from solution import Solution

    return (
        Solution,
        assert_generate_possible_next_moves,
        run_generate_possible_next_moves,
    )


@app.cell
def _():
    # Example test case
    current_state = "++++"
    expected = ["--++", "+--+", "++--"]
    return current_state, expected


@app.cell
def _(Solution, current_state, run_generate_possible_next_moves):
    result = run_generate_possible_next_moves(Solution, current_state)
    result
    return (result,)


@app.cell
def _(assert_generate_possible_next_moves, expected, result):
    assert_generate_possible_next_moves(result, expected)
    return


if __name__ == "__main__":
    app.run()
