#!/usr/bin/env python3
"""
Test script to verify the vector database connection and content
"""

import json
import os
from pathlib import Path

def test_vector_database():
    """Test the vector database to verify it's the new one"""
    
    # Path to the vector database
    db_path = "/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB"
    
    print("🔍 Testing Vector Database Connection")
    print("=" * 50)
    
    # Check if database exists
    if not Path(db_path).exists():
        print("❌ Vector database directory not found!")
        return False
    
    print(f"✅ Database directory found: {db_path}")
    
    # Check key files
    files_to_check = [
        "vector_db_index.json",
        "processing_summary.json"
    ]
    
    for file_name in files_to_check:
        file_path = Path(db_path) / file_name
        if file_path.exists():
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f"✅ {file_name}: {size_mb:.1f} MB")
        else:
            print(f"❌ {file_name}: Not found")
            return False
    
    # Load and analyze processing summary
    try:
        with open(Path(db_path) / "processing_summary.json", 'r') as f:
            summary = json.load(f)
        
        print("\n📊 Database Statistics:")
        print(f"   📅 Processed: {summary.get('processed_at', 'Unknown')}")
        print(f"   📄 Total Documents: {summary.get('total_documents', 0):,}")
        print(f"   🧩 Total Chunks: {summary.get('total_chunks', 0):,}")
        
        # Show first few documents
        print("\n📚 Sample Documents:")
        for i, doc in enumerate(summary.get('documents', [])[:5]):
            print(f"   {i+1}. {doc.get('title', 'Unknown')}")
            print(f"      Source: {doc.get('source_folder', 'Unknown')}")
            print(f"      Chunks: {doc.get('chunks', 0)}")
        
    except Exception as e:
        print(f"❌ Error reading processing summary: {e}")
        return False
    
    # Test vector index structure
    try:
        with open(Path(db_path) / "vector_db_index.json", 'r') as f:
            # Load the JSON array and get first chunk
            data = json.load(f)
            if data and len(data) > 0:
                first_chunk = data[0]
                
                print("\n🔍 Vector Index Sample:")
                print(f"   Chunk ID: {first_chunk.get('chunk_id', 'Unknown')}")
                print(f"   Content Preview: {first_chunk.get('content', '')[:100]}...")
                print(f"   Metadata Keys: {list(first_chunk.get('metadata', {}).keys())}")
            else:
                print("❌ Vector index is empty")
                return False
        
    except Exception as e:
        print(f"❌ Error reading vector index: {e}")
        return False
    
    print("\n✅ Vector Database Test Complete!")
    print("🎯 This appears to be the NEW vector database with tech stack documentation")
    
    return True

def search_for_crawl4ai():
    """Search for Crawl4ai content in the database"""
    
    db_path = "/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB"
    
    print("\n🔎 Searching for Crawl4ai Content")
    print("=" * 40)
    
    try:
        with open(Path(db_path) / "vector_db_index.json", 'r') as f:
            data = json.load(f)
            
        crawl4ai_chunks = []
        session_chunks = []
        quickstart_chunks = []
        
        # Search through chunks
        for chunk in data[:1000]:  # Check first 1000 chunks for speed
            content = chunk.get('content', '').lower()
            metadata = chunk.get('metadata', {})
            
            if 'crawl4ai' in content or 'crawl4ai' in str(metadata).lower():
                crawl4ai_chunks.append(chunk)
            
            if 'session-management' in content:
                session_chunks.append(chunk)
                
            if 'quickstart' in content:
                quickstart_chunks.append(chunk)
        
        print(f"📊 Content Analysis (first 1000 chunks):")
        print(f"   Crawl4ai chunks: {len(crawl4ai_chunks)}")
        print(f"   Session-management chunks: {len(session_chunks)}")
        print(f"   Quickstart chunks: {len(quickstart_chunks)}")
        
        if crawl4ai_chunks:
            print("\n📚 Sample Crawl4ai Content:")
            for i, chunk in enumerate(crawl4ai_chunks[:3]):
                print(f"   {i+1}. Chunk ID: {chunk.get('chunk_id')}")
                print(f"      Content: {chunk.get('content', '')[:80]}...")
                parent = chunk.get('metadata', {}).get('parent_title', 'Unknown')
                print(f"      Parent: {parent}")
        
        if len(crawl4ai_chunks) > 0:
            print("✅ Crawl4ai documentation confirmed in vector database!")
        else:
            print("❌ No Crawl4ai content found in sample")
            
    except Exception as e:
        print(f"❌ Error searching database: {e}")

if __name__ == "__main__":
    success = test_vector_database()
    if success:
        search_for_crawl4ai()
    
    print("\n" + "=" * 50)
    print("🚀 Vector Database Verification Complete!")
