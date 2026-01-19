import daft
from daft.functions import embed_text


def text_embeddings():
    # Create a knowledge base with documents
    df = daft.from_pydict(
        {
            "doc_id": [1, 2, 3, 4],
            "text": [
                "Python is a high-level programming language",
                "Machine learning models require training data",
                "Daft is a distributed dataframe library",
                "Embeddings capture semantic meaning of text",
            ],
        }
    )

    df = df.with_column(
        "embeddings",
        embed_text(daft.col("text"), model="text-embedding-3-small"),
    )

    df.show()


def image_embeddings():
    pass
