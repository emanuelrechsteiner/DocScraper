"""
Phase 4: Performance Benchmarks

Measures performance metrics for all components.
Tests execution time, memory usage, and throughput.
"""

import time
import tempfile
import pytest
from pathlib import Path
from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig
from docscraper.optimization.chunker import ChunkOptimizer
from docscraper.cleaning.rules import PatternRegistry


class TestPerformanceBenchmarks:
    """Performance benchmarks for core operations"""

    def create_sample_content(self, size_kb: int = 10) -> str:
        """Create sample markdown content of specified size"""
        base = """# Main Document

## Section 1
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor.

```python
def example():
    return "Hello, World!"
```

- Item 1
- Item 2
- Item 3

### Subsection 1.1
More content here with additional information.

## Section 2
Additional section content.

Navigation: [Home](#) [Next](#)

---

Footer content here.
"""
        # Repeat to reach target size
        repetitions = max(1, (size_kb * 1024) // len(base))
        return base * repetitions

    def test_single_file_cleaning_performance(self):
        """Benchmark single file cleaning"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            content = self.create_sample_content(50)  # 50KB file
            f.write(content)
            f.flush()
            input_path = Path(f.name)

        try:
            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            # Warm-up
            output_path = Path(tempfile.mktemp(suffix='.md'))
            cleaner.clean_document(input_path, output_path)
            output_path.unlink()

            # Benchmark
            start = time.time()
            output_path = Path(tempfile.mktemp(suffix='.md'))
            result = cleaner.clean_document(input_path, output_path)
            elapsed = time.time() - start

            # Assertions
            assert result.success is True
            assert elapsed < 1.0, f"Single file cleaning took {elapsed:.2f}s, target <1.0s"
            print(f"Single file (50KB): {elapsed*1000:.2f}ms")

            output_path.unlink()
        finally:
            input_path.unlink()

    def test_batch_cleaning_performance(self):
        """Benchmark batch file cleaning"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create 10 test files
            for i in range(10):
                file_path = input_dir / f"doc{i}.md"
                content = self.create_sample_content(10)  # 10KB each
                file_path.write_text(content)

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            start = time.time()
            results = cleaner.clean_batch(input_dir, output_dir)
            elapsed = time.time() - start

            # Assertions
            assert len(results) == 10
            assert all(r.success for r in results)
            avg_time = elapsed / 10
            assert avg_time < 0.5, f"Average per-file time: {avg_time:.2f}s, target <0.5s"
            print(f"Batch (10 files, 10KB each): {elapsed:.2f}s total ({avg_time*1000:.2f}ms/file)")

        finally:
            for f in input_dir.glob("*.md"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*.md"):
                f.unlink()
            output_dir.rmdir()

    def test_pattern_registry_performance(self):
        """Benchmark pattern registry operations"""
        registry = PatternRegistry()

        # Benchmark pattern lookup
        start = time.time()
        for _ in range(1000):
            registry.get_pattern("skip_navigation")
        elapsed = time.time() - start
        per_call = (elapsed * 1_000_000) / 1000  # microseconds
        assert per_call < 100, f"Pattern lookup: {per_call:.2f}µs, target <100µs"
        print(f"Pattern lookup (1000 calls): {per_call:.2f}µs per call")

        # Benchmark getting patterns by category
        start = time.time()
        for _ in range(100):
            registry.get_patterns_by_category(registry.patterns[0].category)
        elapsed = time.time() - start
        assert elapsed < 0.1, f"Category query took {elapsed:.3f}s, target <0.1s"
        print(f"Category query (100 calls): {(elapsed/100)*1000:.2f}ms per call")

    def test_chunk_optimizer_performance(self):
        """Benchmark chunk optimizer"""
        optimizer = ChunkOptimizer()
        content = self.create_sample_content(100)  # 100KB

        # Benchmark optimization
        start = time.time()
        optimized, metadata = optimizer.optimize(content)
        elapsed = time.time() - start

        assert elapsed < 0.5, f"Chunk optimization took {elapsed:.3f}s, target <0.5s"
        print(f"Chunk optimization (100KB): {elapsed*1000:.2f}ms")

        # Benchmark chunking
        start = time.time()
        chunks = optimizer.split_into_chunks(content)
        elapsed = time.time() - start

        assert elapsed < 0.1, f"Chunking took {elapsed:.3f}s, target <0.1s"
        print(f"Chunking (100KB): {elapsed*1000:.2f}ms ({len(chunks)} chunks)")

    def test_throughput_single_thread(self):
        """Measure throughput (files per second)"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create 20 files
            num_files = 20
            for i in range(num_files):
                file_path = input_dir / f"doc{i}.md"
                content = self.create_sample_content(5)  # 5KB each
                file_path.write_text(content)

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            start = time.time()
            results = cleaner.clean_batch(input_dir, output_dir)
            elapsed = time.time() - start

            throughput = num_files / elapsed
            assert throughput > 2.0, f"Throughput: {throughput:.1f} files/sec, target >2.0"
            print(f"Throughput: {throughput:.1f} files/second")

        finally:
            for f in input_dir.glob("*.md"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*.md"):
                f.unlink()
            output_dir.rmdir()

    def test_memory_efficiency_large_file(self):
        """Test memory efficiency with large files"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            # 1MB file
            content = self.create_sample_content(1024)
            f.write(content)
            f.flush()
            input_path = Path(f.name)

        try:
            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            output_path = Path(tempfile.mktemp(suffix='.md'))
            result = cleaner.clean_document(input_path, output_path)

            # Should complete successfully without memory issues
            assert result.success is True
            assert result.original_size > 1_000_000  # > 1MB
            print(f"Large file (1MB): Success, {result.reduction_percentage:.1f}% reduction")

            output_path.unlink()
        finally:
            input_path.unlink()


class TestPerformanceScaling:
    """Test performance scaling with increasing workload"""

    def test_scaling_files_count(self):
        """Test scaling with increasing number of files"""
        config = CleaningConfig()

        for num_files in [5, 10, 20]:
            input_dir = Path(tempfile.mkdtemp())
            output_dir = Path(tempfile.mkdtemp())

            try:
                # Create test files
                for i in range(num_files):
                    (input_dir / f"doc{i}.md").write_text(f"# Doc {i}\n\nContent {i}")

                cleaner = PostScraperCleaner(config)

                start = time.time()
                results = cleaner.clean_batch(input_dir, output_dir)
                elapsed = time.time() - start

                assert len(results) == num_files
                assert all(r.success for r in results)
                avg_time = elapsed / num_files
                print(f"{num_files} files: {elapsed:.3f}s total ({avg_time*1000:.2f}ms/file)")

            finally:
                for f in input_dir.glob("*.md"):
                    f.unlink()
                input_dir.rmdir()

                for f in output_dir.glob("*.md"):
                    f.unlink()
                output_dir.rmdir()

    def test_scaling_file_size(self):
        """Test scaling with increasing file sizes"""
        config = CleaningConfig()

        for size_kb in [5, 50, 100]:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                base = "# Heading\n\nContent " * 50
                repetitions = max(1, (size_kb * 1024) // len(base))
                f.write(base * repetitions)
                f.flush()
                input_path = Path(f.name)

            try:
                cleaner = PostScraperCleaner(config)
                output_path = Path(tempfile.mktemp(suffix='.md'))

                start = time.time()
                result = cleaner.clean_document(input_path, output_path)
                elapsed = time.time() - start

                assert result.success is True
                print(f"{size_kb}KB file: {elapsed*1000:.2f}ms")

                output_path.unlink()
            finally:
                input_path.unlink()


class TestResourceUsage:
    """Test resource usage patterns"""

    def test_config_initialization_time(self):
        """Test configuration initialization time"""
        start = time.time()
        for _ in range(100):
            config = CleaningConfig()
        elapsed = time.time() - start

        per_init = (elapsed / 100) * 1000  # milliseconds
        assert per_init < 1.0, f"Config init: {per_init:.3f}ms, target <1.0ms"
        print(f"Config initialization: {per_init:.3f}ms")

    def test_cleaner_initialization_time(self):
        """Test cleaner initialization time"""
        config = CleaningConfig()

        start = time.time()
        for _ in range(10):
            cleaner = PostScraperCleaner(config)
        elapsed = time.time() - start

        per_init = (elapsed / 10) * 1000  # milliseconds
        assert per_init < 50.0, f"Cleaner init: {per_init:.1f}ms, target <50ms"
        print(f"Cleaner initialization: {per_init:.1f}ms")

    def test_pattern_registry_initialization(self):
        """Test pattern registry initialization"""
        start = time.time()
        for _ in range(10):
            registry = PatternRegistry()
        elapsed = time.time() - start

        per_init = (elapsed / 10) * 1000  # milliseconds
        assert per_init < 10.0, f"Registry init: {per_init:.1f}ms, target <10ms"
        print(f"Pattern registry initialization: {per_init:.1f}ms")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])  # -s for print output
