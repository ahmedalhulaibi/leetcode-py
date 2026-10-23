import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_partition_labels, run_partition_labels
    from solution import Solution

    return Solution, assert_partition_labels, run_partition_labels


@app.cell
def _():
    # Example test case
    s = "ababcbacadefegdehijhklij"
    expected = [9, 7, 8]
    return expected, s


@app.cell
def _(Solution, run_partition_labels, s):
    result = run_partition_labels(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_partition_labels, expected, result):
    assert_partition_labels(result, expected)
    return


if __name__ == "__main__":
    app.run()
