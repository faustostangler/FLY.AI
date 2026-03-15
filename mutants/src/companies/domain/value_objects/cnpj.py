import re
from pydantic import RootModel, ValidationInfo, field_validator
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

class CNPJ(RootModel[str]):
    """Brazilian National Corporate Taxpayer Registry (CNPJ) Value Object.

    CNPJ is a fundamental identifier in the Brazilian financial domain. 
    By encapsulating it in a Value Object, we guarantee that any Company 
    entity possessing a CNPJ has been mathematically validated, preventing 
    corrupt data from polluting the domain or database.

    Attributes:
        root (str): The raw, cleaned 14-digit CNPJ string.
    """
    
    @field_validator('root')
    @classmethod
    def validate_cnpj(cls, v: str, info: ValidationInfo) -> str:
        """Validates the structure and veracity of the CNPJ string.

        Simple length checks are insufficient; calculating check digits 
        is the only way to programmatically verify that a CNPJ is legitimate 
        before committing it to the Primary Store.

        Args:
            v (str): The input CNPJ string (raw or formatted).
            info (ValidationInfo): Pydantic validation context.

        Returns:
            str: The cleaned 14-digit numeric string.

        Raises:
            ValueError: If the CNPJ is empty, has an invalid length, 
                contains identical digits, or fails the Modulo 11 check.
        """
        if not v:
            raise ValueError("CNPJ cannot be empty")
            
        # Strip non-numeric characters to normalize the input.
        cleaned = re.sub(r"[^\d]", "", v)
        
        if len(cleaned) != 14:
            raise ValueError(f"CNPJ must have exactly 14 digits, got {len(cleaned)}")
            
        # Filter out sequences like '00000000000000' which pass length but are invalid.
        if len(set(cleaned)) == 1:
            raise ValueError("CNPJ has invalid format (all digits are the same)")
            
        # Verify the veracity using the official mathematical algorithm.
        if not cls._validate_check_digits(cleaned):
            raise ValueError("CNPJ has invalid check digits")
            
        return cleaned
        
    @classmethod
    def _validate_check_digits(cls, cnpj: str) -> bool:
        """Calculates the check digits using the Modulo 11 algorithm.

        This is the standard validation logic defined by the 
        Brazilian Federal Revenue Service (Receita Federal).
        """
        
        def calculate_digit(cnpj_partial: str, weights: list[int]) -> str:
            sum_val = sum(int(n) * w for n, w in zip(cnpj_partial, weights))
            remainder = sum_val % 11
            return '0' if remainder < 2 else str(11 - remainder)
            
        # Standard weights for the first and second check digits.
        weights_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        weights_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        digit_1 = calculate_digit(cnpj[:12], weights_1)
        digit_2 = calculate_digit(cnpj[:12] + digit_1, weights_2)
        
        return cnpj[-2:] == f"{digit_1}{digit_2}"

    def format(self) -> str:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCNPJǁformat__mutmut_orig'), object.__getattribute__(self, 'xǁCNPJǁformat__mutmut_mutants'), args, kwargs, self)

    def xǁCNPJǁformat__mutmut_orig(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_1(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = None
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_2(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:3]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_3(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[3:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_4(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:6]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_5(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[6:8]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_6(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:9]}/{c[8:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_7(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[9:12]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_8(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:13]}-{c[12:]}"

    def xǁCNPJǁformat__mutmut_9(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI) 
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[13:]}"
    
    xǁCNPJǁformat__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCNPJǁformat__mutmut_1': xǁCNPJǁformat__mutmut_1, 
        'xǁCNPJǁformat__mutmut_2': xǁCNPJǁformat__mutmut_2, 
        'xǁCNPJǁformat__mutmut_3': xǁCNPJǁformat__mutmut_3, 
        'xǁCNPJǁformat__mutmut_4': xǁCNPJǁformat__mutmut_4, 
        'xǁCNPJǁformat__mutmut_5': xǁCNPJǁformat__mutmut_5, 
        'xǁCNPJǁformat__mutmut_6': xǁCNPJǁformat__mutmut_6, 
        'xǁCNPJǁformat__mutmut_7': xǁCNPJǁformat__mutmut_7, 
        'xǁCNPJǁformat__mutmut_8': xǁCNPJǁformat__mutmut_8, 
        'xǁCNPJǁformat__mutmut_9': xǁCNPJǁformat__mutmut_9
    }
    xǁCNPJǁformat__mutmut_orig.__name__ = 'xǁCNPJǁformat'
