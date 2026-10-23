import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_round_trip, run_serialize_deserialize
    from solution import Codec

    return Codec, assert_round_trip, run_serialize_deserialize


@app.cell
def _():
    # Example test case
    root_list = [2, 1, 3]
    return (root_list,)


@app.cell
def _(Codec, root_list, run_serialize_deserialize):
    result = run_serialize_deserialize(Codec, root_list)
    result
    return (result,)


@app.cell
def _(assert_round_trip, result, root_list):
    assert_round_trip(result, root_list)
    return


if __name__ == "__main__":
    app.run()
