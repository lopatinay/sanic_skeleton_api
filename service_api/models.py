import sqlalchemy as sa


metadata = sa.MetaData()


DummyModel = sa.Table(
    "dummy_model",
    metadata,

    sa.Column("id", sa.Integer, primary_key=True),
)

models = (
    DummyModel,
)
