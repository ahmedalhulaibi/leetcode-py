import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_serialize_deserialize, run_serialize_deserialize
    from solution import Codec

    return Codec, assert_serialize_deserialize, run_serialize_deserialize


@app.cell
def _():
    # Example test case
    root_list = [1, 2, 3, None, None, 4, 5]
    return (root_list,)


@app.cell
def _(Codec, root_list, run_serialize_deserialize):
    result = run_serialize_deserialize(Codec, root_list)
    result
    return (result,)


@app.cell
def _(assert_serialize_deserialize, result, root_list):
    assert_serialize_deserialize(result, root_list)
    return


if __name__ == "__main__":
    app.run()
