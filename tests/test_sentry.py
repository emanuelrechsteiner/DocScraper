"""Tests for Sentry integration (#52)."""

from unittest.mock import patch
from api.middleware.sentry_config import init_sentry


class TestSentryInit:
    def test_no_dsn_does_not_initialize(self) -> None:
        with patch("api.middleware.sentry_config.settings") as mock_settings:
            mock_settings.sentry_dsn = ""
            mock_settings.debug = True
            with patch("api.middleware.sentry_config.sentry_sdk") as mock_sentry:
                init_sentry()
                mock_sentry.init.assert_not_called()

    def test_with_dsn_initializes(self) -> None:
        with patch("api.middleware.sentry_config.settings") as mock_settings:
            mock_settings.sentry_dsn = "https://examplePublicKey@o0.ingest.sentry.io/0"
            mock_settings.debug = False
            with patch("api.middleware.sentry_config.sentry_sdk") as mock_sentry:
                init_sentry()
                mock_sentry.init.assert_called_once()
                call_kwargs = mock_sentry.init.call_args[1]
                assert call_kwargs["environment"] == "production"
                assert call_kwargs["send_default_pii"] is False
