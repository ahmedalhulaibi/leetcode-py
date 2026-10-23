import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repeated_dna_sequences, run_repeated_dna_sequences
    from solution import Solution

    return Solution, assert_repeated_dna_sequences, run_repeated_dna_sequences


@app.cell
def _():
    # Example test case
    s: str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    expected: list[str] = ["AAAAACCCCC", "CCCCCAAAAA"]
    return expected, s


@app.cell
def _(Solution, run_repeated_dna_sequences, s: str):
    result = run_repeated_dna_sequences(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_repeated_dna_sequences, expected: list[str], result):
    assert_repeated_dna_sequences(result, expected)
    return


if __name__ == "__main__":
    app.run()
