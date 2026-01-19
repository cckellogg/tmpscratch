import daft
from daft.functions import (
    convert_image,
    decode_image,
    embed_image,
    embed_text,
    resize,
)


def text_embeddings(model="openai/gpt-5-nano"):
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
        embed_text(daft.col("text"), model=model),
    )

    df.show()


def image_embeddings(model="Alibaba-NLP/gme-Qwen2-VL-2B-Instruct"):
    df = (
        # Discover a few images from HuggingFace
        daft.from_glob_path("hf://datasets/datasets-examples/doc-image-3/images")
        # Read the 4 PNG, JPEG, TIFF, WEBP Images
        .with_column("image_bytes", daft.col("path").download())
        # Decode the image bytes into a daft Image DataType
        .with_column("image_type", decode_image(daft.col("image_bytes")))
        # Convert Image to RGB and resize the image to 288x288
        .with_column(
            "image_resized",
            resize(convert_image(daft.col("image_type"), "RGB"), 288, 288),
        )
        # Embed the image
        .with_column(
            "image_embeddings",
            embed_image(
                daft.col("image_resized"),
                provider="transformers",
                model=model,
            ),
        )
    )

    # Show the dataframe
    df.show()
