import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_sentences, run_generate_sentences
    from solution import Solution

    return Solution, assert_generate_sentences, run_generate_sentences


@app.cell
def _():
    # Example test case
    synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "happy sad"
    expected = [
        "cheerful sad",
        "cheerful sorrow",
        "happy sad",
        "happy sorrow",
        "joy sad",
        "joy sorrow",
    ]
    return expected, synonyms, text


@app.cell
def _(Solution, run_generate_sentences, synonyms, text):
    result = run_generate_sentences(Solution, synonyms, text)
    result
    return (result,)


@app.cell
def _(assert_generate_sentences, expected, result):
    assert_generate_sentences(result, expected)
    return


if __name__ == "__main__":
    app.run()
