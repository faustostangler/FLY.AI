import re
from pydantic import RootModel, ValidationInfo, field_validator


class CNPJ(RootModel[str]):
    """Brazilian National Corporate Taxpayer Registry (CNPJ) Value Object.

    CNPJ is a fundamental identifier in the Brazilian financial domain.
    By encapsulating it in a Value Object, we guarantee that any Company
    entity possessing a CNPJ has been mathematically validated, preventing
    corrupt data from polluting the domain or database.

    Attributes:
        root (str): The raw, cleaned 14-digit CNPJ string.
    """

    @field_validator("root")
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
            return "0" if remainder < 2 else str(11 - remainder)

        # Standard weights for the first and second check digits.
        weights_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        weights_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        digit_1 = calculate_digit(cnpj[:12], weights_1)
        digit_2 = calculate_digit(cnpj[:12] + digit_1, weights_2)

        return cnpj[-2:] == f"{digit_1}{digit_2}"

    def format(self) -> str:
        """Returns the CNPJ in its canonical human-readable format.

        Used primarily for presentation in the API (Swagger/OpenAPI)
        and CLI tools to match the format expected by financial users.

        Returns:
            str: Formatted CNPJ (e.g., 'XX.XXX.XXX/XXXX-XX').
        """
        c = self.root
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"
