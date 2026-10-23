import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_online_election, run_online_election
    from solution import TopVotedCandidate

    return TopVotedCandidate, assert_online_election, run_online_election


@app.cell
def _():
    # Example test case
    operations = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    inputs = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
    expected = [None, 0, 1, 1, 0, 0, 1]
    return expected, inputs, operations


@app.cell
def _(TopVotedCandidate, inputs, operations, run_online_election):
    result, candidate = run_online_election(TopVotedCandidate, operations, inputs)
    print(result)
    candidate
    return (result,)


@app.cell
def _(assert_online_election, expected, result):
    assert_online_election(result, expected)
    return


if __name__ == "__main__":
    app.run()
