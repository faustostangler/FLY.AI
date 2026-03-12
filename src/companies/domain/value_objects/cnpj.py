import re
from pydantic import RootModel, ValidationInfo, field_validator

class CNPJ(RootModel[str]):
    """
    CNPJ Value Object.
    Validates the Brazilian CNPJ format and check digits.
    Uses Pydantic's RootModel to act seamlessly as a single string field in other entities.
    """
    
    @field_validator('root')
    @classmethod
    def validate_cnpj(cls, v: str, info: ValidationInfo) -> str:
        if not v:
            raise ValueError("CNPJ cannot be empty")
            
        # Strip punctuation
        cleaned = re.sub(r"[^\d]", "", v)
        
        if len(cleaned) != 14:
            raise ValueError(f"CNPJ must have exactly 14 digits, got {len(cleaned)}")
            
        # Check for known invalid CNPJs (all same digits)
        if len(set(cleaned)) == 1:
            raise ValueError("CNPJ has invalid format (all digits are the same)")
            
        # Check digit algorithm
        if not cls._validate_check_digits(cleaned):
            raise ValueError("CNPJ has invalid check digits")
            
        return cleaned
        
    @classmethod
    def _validate_check_digits(cls, cnpj: str) -> bool:
        """Fully calculates the Modulo 11 for the CNPJ"""
        
        def calculate_digit(cnpj_partial: str, weights: list[int]) -> str:
            sum_val = sum(int(n) * w for n, w in zip(cnpj_partial, weights))
            remainder = sum_val % 11
            return '0' if remainder < 2 else str(11 - remainder)
            
        weights_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        weights_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        digit_1 = calculate_digit(cnpj[:12], weights_1)
        digit_2 = calculate_digit(cnpj[:12] + digit_1, weights_2)
        
        return cnpj[-2:] == f"{digit_1}{digit_2}"

    def format(self) -> str:
        """Returns the CNPJ formatted as XX.XXX.XXX/XXXX-XX"""
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"
