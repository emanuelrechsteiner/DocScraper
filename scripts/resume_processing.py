#!/usr/bin/env python3
"""Resume processing from checkpoint — specifically to complete the dependency graph phase.

Usage:
    python scripts/resume_processing.py --checkpoint <path> --input-dir <path> --output-dir <path>
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from docscraper.core.processor import DocumentPostProcessor


async def resume_from_checkpoint(
    checkpoint_path: Path,
    input_dir: Path,
    output_dir: Path,
) -> None:
    """Resume processing from the pre-classification checkpoint.

    Args:
        checkpoint_path: Path to the checkpoint JSON file.
        input_dir: Directory containing raw documentation files.
        output_dir: Directory for processed output.
    """
    if not checkpoint_path.exists():
        print(f"Checkpoint not found: {checkpoint_path}")
        return

    print(f"Resuming from checkpoint: {checkpoint_path}")

    # Create processor instance
    processor = DocumentPostProcessor(
        input_dir=str(input_dir),
        output_dir=str(output_dir),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Load the checkpoint
    checkpoint_data = processor.load_checkpoint(str(checkpoint_path))

    print(f"Loaded {len(processor.processed_docs)} documents")
    print(f"Phase: {checkpoint_data.get('phase', 'unknown')}")

    try:
        print("Creating dependency graph with progress tracking...")
        processor.sorter.create_dependency_graph(processor.processed_docs)

        print("Calculating complexity scores with progress tracking...")
        processor.sorter.calculate_complexity_scores(processor.processed_docs)

        print("Saving checkpoint after classification...")
        processor.save_checkpoint("post_classification")

        print("Saving final processed documents...")
        processor.save_processed_documents()

        print("Creating vector database index...")
        processor.create_vector_db_index()

        print("Saving final checkpoint...")
        processor.save_checkpoint("completed")

        print("Processing completed successfully!")

        # Print summary
        categories: dict[str, int] = {}
        for doc in processor.processed_docs:
            categories[doc.category] = categories.get(doc.category, 0) + 1

        print("\nFinal Summary:")
        print(f"   Total documents: {len(processor.processed_docs)}")
        print("   Categories:")
        for category, count in sorted(categories.items()):
            print(f"     - {category}: {count}")

        print(f"\n   Output saved to: {processor.output_dir}")

    except Exception as e:
        print(f"Error during resume: {e}")
        import traceback
        traceback.print_exc()


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Resume document processing from a checkpoint file.",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        required=True,
        help="Path to the checkpoint JSON file",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Directory containing raw documentation files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory for processed output",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(
        resume_from_checkpoint(
            checkpoint_path=args.checkpoint,
            input_dir=args.input_dir,
            output_dir=args.output_dir,
        )
    )
