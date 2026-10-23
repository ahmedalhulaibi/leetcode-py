import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reconstruct_queue, run_reconstruct_queue
    from solution import Solution

    return Solution, assert_reconstruct_queue, run_reconstruct_queue


@app.cell
def _():
    # Example test case
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    return expected, people


@app.cell
def _(Solution, people, run_reconstruct_queue):
    result = run_reconstruct_queue(Solution, people)
    result
    return (result,)


@app.cell
def _(assert_reconstruct_queue, expected, result):
    assert_reconstruct_queue(result, expected)
    return


if __name__ == "__main__":
    app.run()
