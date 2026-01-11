#!/usr/bin/env python3
"""
Resume processing from checkpoint - specifically to complete the dependency graph phase.
"""

import asyncio
import sys
import os
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docscraper.core.processor import DocumentPostProcessor

async def resume_from_checkpoint():
    """Resume processing from the pre-classification checkpoint."""
    
    # Path to the pre-classification checkpoint
    checkpoint_path = "/Volumes/NvME-Satechi/VectorDatabase/20250824_083937_2025_Emanuels_Tech_Stack_Docs_VectorDB/checkpoints/checkpoint_pre_classification_10431.json"
    
    if not os.path.exists(checkpoint_path):
        print(f"❌ Checkpoint not found: {checkpoint_path}")
        return
    
    print(f"🔄 Resuming from checkpoint: {checkpoint_path}")
    
    # Create processor instance
    processor = DocumentPostProcessor(
        input_dir="/Volumes/NvME-Satechi/Documentation/2025_Emanuels_Tech_Stack_Docs",
        output_dir="/Volumes/NvME-Satechi/VectorDatabase/20250824_083937_2025_Emanuels_Tech_Stack_Docs_VectorDB",
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    # Load the checkpoint
    checkpoint_data = processor.load_checkpoint(checkpoint_path)
    
    print(f"✅ Loaded {len(processor.processed_docs)} documents")
    print(f"📊 Phase: {checkpoint_data.get('phase', 'unknown')}")
    
    # Since classification is already done, we need to:
    # 1. Create dependency graph (this is where it failed)
    # 2. Save final results
    
    try:
        print("🔗 Creating dependency graph with progress tracking...")
        dep_graph = processor.sorter.create_dependency_graph(processor.processed_docs)
        
        print("📊 Calculating complexity scores with progress tracking...")
        processor.sorter.calculate_complexity_scores(processor.processed_docs)
        
        print("💾 Saving checkpoint after classification...")
        processor.save_checkpoint("post_classification")
        
        print("💾 Saving final processed documents...")
        processor.save_processed_documents()
        
        print("🔍 Creating vector database index...")
        processor.create_vector_db_index()
        
        print("💾 Saving final checkpoint...")
        processor.save_checkpoint("completed")
        
        print("🎉 Processing completed successfully!")
        
        # Print summary
        categories = {}
        for doc in processor.processed_docs:
            categories[doc.category] = categories.get(doc.category, 0) + 1
        
        print(f"\n📊 Final Summary:")
        print(f"   Total documents: {len(processor.processed_docs)}")
        print(f"   Categories:")
        for category, count in sorted(categories.items()):
            print(f"     - {category}: {count}")
        
        print(f"\n📁 Output saved to: {processor.output_dir}")
        
    except Exception as e:
        print(f"❌ Error during resume: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(resume_from_checkpoint())
