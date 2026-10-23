import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_magic_dictionary, run_magic_dictionary
    from solution import MagicDictionary

    return MagicDictionary, assert_magic_dictionary, run_magic_dictionary


@app.cell
def _():
    # Example test case
    operations = ["MagicDictionary", "build_dict", "search", "search", "search", "search"]
    inputs = [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    expected = [None, None, False, True, False, False]
    return expected, inputs, operations


@app.cell
def _(MagicDictionary, inputs, operations, run_magic_dictionary):
    result, magic = run_magic_dictionary(MagicDictionary, operations, inputs)
    print(result)
    magic
    return (result,)


@app.cell
def _(assert_magic_dictionary, expected, result):
    assert_magic_dictionary(result, expected)
    return


if __name__ == "__main__":
    app.run()
