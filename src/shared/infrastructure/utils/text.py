import re
import string
import unidecode
from typing import Optional
from shared.infrastructure.config import settings


class TextCleaner:
    """
    SOTA Text Cleaning Utility that encapsulates legacy normalization logic.
    Handles punctuation removal, accent normalization, extra whitespace,
    and specific business-rule word removals.
    """

    _translation_table = str.maketrans("", "", string.punctuation)
    _words_to_remove_pattern: Optional[re.Pattern] = None

    @classmethod
    def _get_words_pattern(cls) -> re.Pattern:
        if cls._words_to_remove_pattern is None:
            # Compile pattern from settings, stripping leading/trailing spaces
            words = [w.strip() for w in settings.b3.words_to_remove if w.strip()]
            pattern_str = "|".join(map(re.escape, words))
            # Match word boundaries and many spaces
            cls._words_to_remove_pattern = re.compile(
                rf"\b(?:{pattern_str})\b", re.IGNORECASE
            )
        return cls._words_to_remove_pattern

    @classmethod
    def clean(cls, text: Optional[str]) -> Optional[str]:
        """
        Cleans and normalizes text following FLY's legacy rules:
        1. Remove punctuation
        2. Unidecode (accents to ASCII)
        3. Uppercase
        4. Normalize whitespace
        5. Remove corporate status terms (Recovery, Liquidation, etc.)
        """
        if text is None or not isinstance(text, str):
            return text

        try:
            # Primary cleaning: Accents -> ASCII, Punctuation removed, Uppercase
            text = (
                unidecode.unidecode(text)
                .translate(cls._translation_table)
                .upper()
                .strip()
            )

            # Normalize multiple spaces to single space
            text = re.sub(r"\s+", " ", text)

            # Remove specific legal status words defined in settings
            pattern = cls._get_words_pattern()
            text = pattern.sub("", text)

            # Final trim and space normalization post-removal
            text = re.sub(r"\s+", " ", text).strip()

        except Exception:
            # Fallback to original text if cleaning fails (Robustness)
            return text

        return text
