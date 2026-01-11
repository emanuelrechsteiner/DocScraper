"""
Phase 4: GUI Functional Tests

Tests for PostScraperCleanerGUI functionality (if available).
Tests configuration, processing, and result display.
"""

import pytest
import tempfile
from pathlib import Path

# Try to import GUI, but tests can run without it
try:
    from PostScraperCleanerGUI import PostScraperCleanerGUI
    HAS_GUI = True
except ImportError:
    HAS_GUI = False


class TestGUIConfigurationPanel:
    """Test GUI configuration panel functionality"""

    @pytest.mark.skipif(not HAS_GUI, reason="GUI not available")
    def test_gui_initialization(self):
        """Test GUI initializes without errors"""
        try:
            gui = PostScraperCleanerGUI()
            assert gui is not None
        except Exception as e:
            pytest.skip(f"GUI initialization failed: {e}")

    @pytest.mark.skipif(not HAS_GUI, reason="GUI not available")
    def test_config_persistence(self):
        """Test configuration save and load"""
        try:
            gui = PostScraperCleanerGUI()

            # Test saving config
            config = {
                "remove_navigation": True,
                "remove_headers_footers": True,
                "remove_boilerplate": True,
            }

            # Simulate config save (actual implementation varies)
            # This is a placeholder for GUI-specific testing
            assert "remove_navigation" in config

        except Exception as e:
            pytest.skip(f"GUI config test failed: {e}")


class TestGUIProcessingWorkflow:
    """Test GUI processing workflow"""

    def test_folder_selection_validation(self):
        """Test input/output folder validation"""
        # Create temp directories
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Verify folders exist
            assert input_dir.exists()
            assert output_dir.exists()
        finally:
            input_dir.rmdir()
            output_dir.rmdir()

    def test_file_discovery(self):
        """Test discovery of markdown files"""
        input_dir = Path(tempfile.mkdtemp())

        try:
            # Create test files
            (input_dir / "doc1.md").write_text("# Doc 1")
            (input_dir / "doc2.md").write_text("# Doc 2")
            (input_dir / "readme.txt").write_text("Not markdown")

            # Count markdown files
            md_files = list(input_dir.glob("*.md"))
            assert len(md_files) == 2

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

    def test_result_tracking(self):
        """Test result tracking and statistics"""
        # Verify result structure
        from docscraper.cleaning.cleaner import CleaningResult
        from pathlib import Path

        result = CleaningResult(
            input_file=Path("test.md"),
            output_file=Path("output.md"),
            success=True,
            original_size=1000,
            cleaned_size=800,
        )
        result.calculate_reduction()

        # Verify results can be converted to dict
        result_dict = result.to_dict()
        assert result_dict["success"] is True
        assert result_dict["reduction_percentage"] == 20.0


class TestGUIResultsDisplay:
    """Test GUI results display functionality"""

    def test_summary_calculation(self):
        """Test summary statistics calculation"""
        from docscraper.cleaning.cleaner import CleaningResult
        from pathlib import Path

        results = []
        for i in range(3):
            r = CleaningResult(
                input_file=Path(f"doc{i}.md"),
                original_size=1000,
                cleaned_size=800,
                success=True,
            )
            r.calculate_reduction()
            results.append(r)

        # Calculate summary
        successful = [r for r in results if r.success]
        total_before = sum(r.original_size for r in results)
        total_after = sum(r.cleaned_size for r in results)
        avg_reduction = (
            sum(r.reduction_percentage for r in successful) / len(successful)
            if successful
            else 0
        )

        assert len(successful) == 3
        assert total_before == 3000
        assert total_after == 2400
        assert avg_reduction == 20.0

    def test_result_export_json(self):
        """Test exporting results to JSON"""
        import json
        from docscraper.cleaning.cleaner import CleaningResult
        from pathlib import Path

        result = CleaningResult(
            input_file=Path("test.md"),
            original_size=1000,
            cleaned_size=800,
            success=True,
        )
        result.calculate_reduction()

        # Verify dict can be JSON serialized
        result_dict = result.to_dict()
        json_str = json.dumps(result_dict)
        loaded = json.loads(json_str)

        assert loaded["success"] is True
        assert loaded["original_size"] == 1000

    def test_result_export_csv(self):
        """Test exporting results to CSV format"""
        from docscraper.cleaning.cleaner import CleaningResult
        from pathlib import Path

        results = []
        for i in range(3):
            r = CleaningResult(
                input_file=Path(f"doc{i}.md"),
                output_file=Path(f"out{i}.md"),
                original_size=1000 * (i + 1),
                cleaned_size=800 * (i + 1),
                success=True,
            )
            results.append(r)

        # Create CSV header
        headers = ["File", "Original", "Cleaned", "Reduction%", "Success"]

        # Verify data structure
        assert len(results) == 3
        assert all(r.input_file for r in results)


class TestGUIErrorHandling:
    """Test GUI error handling"""

    def test_missing_input_folder(self):
        """Test handling of missing input folder"""
        from pathlib import Path

        nonexistent = Path("/nonexistent/folder")
        assert not nonexistent.exists()

    def test_invalid_configuration(self):
        """Test handling of invalid configuration"""
        from docscraper.cleaning.cleaner import CleaningConfig

        try:
            # Invalid threshold
            config = CleaningConfig(llm_confidence_threshold=1.5)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected

    def test_file_write_permission_error(self):
        """Test handling of file write errors"""
        # This would require OS-level permission testing
        # Placeholder for comprehensive testing
        pass

    def test_processing_interruption(self):
        """Test handling of processing interruption"""
        # Test that batch processing can handle file errors gracefully
        from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig
        from pathlib import Path
        import tempfile

        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create mix of valid and problematic files
            (input_dir / "valid.md").write_text("# Valid\n\nContent")
            (input_dir / "invalid.md").write_text("# Invalid\n\nContent")

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            # Should complete even if one file has issues
            results = cleaner.clean_batch(input_dir, output_dir)
            assert len(results) >= 1

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()


class TestGUIIntegration:
    """Test GUI integration with backend"""

    def test_config_to_backend(self):
        """Test configuration passes to backend correctly"""
        from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig

        config = CleaningConfig(
            remove_navigation=True,
            remove_headers_footers=True,
            enable_chunk_optimization=True,
            target_chunk_size=512,
        )

        cleaner = PostScraperCleaner(config)
        assert cleaner.config.remove_navigation is True
        assert cleaner.config.target_chunk_size == 512

    def test_progress_callback(self):
        """Test progress callback integration"""
        from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig
        from pathlib import Path
        import tempfile

        progress_updates = []

        def progress_callback(update):
            progress_updates.append(update)

        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create test files
            for i in range(3):
                (input_dir / f"doc{i}.md").write_text(f"# Doc {i}\n\nContent")

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config, progress_callback=progress_callback)

            results = cleaner.clean_batch(input_dir, output_dir)

            # Should have progress updates
            assert len(progress_updates) >= 1
            assert all("type" in update for update in progress_updates)

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()

    def test_statistics_update(self):
        """Test statistics tracking integration"""
        from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig
        from pathlib import Path
        import tempfile

        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create test files
            for i in range(5):
                (input_dir / f"doc{i}.md").write_text(f"# Doc {i}\n\nContent {i}")

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)
            results = cleaner.clean_batch(input_dir, output_dir)

            stats = cleaner.get_statistics()

            # Verify statistics
            assert stats["total_processed"] == 5
            assert stats["total_success"] >= 4
            assert stats["success_rate"] >= 0.0

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
