"""Static storage."""
from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """Static file storage configuration."""

    manifest_strict = False
