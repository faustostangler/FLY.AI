import re
import string
import unidecode
from typing import List, Optional
from shared.infrastructure.config import settings
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


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
            cls._words_to_remove_pattern = re.compile(rf"\b(?:{pattern_str})\b", re.IGNORECASE)
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
            text = unidecode.unidecode(text).translate(cls._translation_table).upper().strip()
            
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
