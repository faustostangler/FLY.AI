import pandas as pd
from unittest.mock import patch
from datetime import datetime

from shared.infrastructure.adapters.pandas.types import (
    ensure_datetime_col,
    ensure_list_col,
)


def test_ensure_datetime_col_already_datetime():
    s = pd.Series([datetime(2021, 1, 1), datetime(2022, 1, 1)])
    result = ensure_datetime_col(s)
    assert result is s


def test_ensure_datetime_col_convertible_strings():
    s = pd.Series(["2020-01-01", "2021-02-01"])
    result = ensure_datetime_col(s)
    assert pd.api.types.is_datetime64_any_dtype(result)
    assert result[0] == pd.Timestamp("2020-01-01")


def test_ensure_datetime_col_invalid_strings_become_nat():
    s = pd.Series(["not-a-date", "2021-02-01"])
    result = ensure_datetime_col(s)
    assert pd.isna(result[0])
    assert result[1] == pd.Timestamp("2021-02-01")


def test_ensure_list_col_already_list_or_tuple():
    s = pd.Series([["a", "b"], ("c", "d")])
    result = ensure_list_col(s)
    assert result[0] == ["a", "b"]
    assert result[1] == ("c", "d")


def test_ensure_list_col_none_becomes_empty_list():
    s = pd.Series([None, [1, 2]])
    result = ensure_list_col(s)
    assert result[0] == []
    assert result[1] == [1, 2]


def test_ensure_list_col_scalar_becomes_list():
    s = pd.Series(["single_val", 123])
    result = ensure_list_col(s)
    assert result[0] == ["single_val"]
    assert result[1] == [123]


def test_ensure_datetime_col_bypasses_conversion_if_already_datetime():
    """
    Testa se a otimização de CPU está funcionando.
    Se a série já for datetime, o Pandas NÃO deve ser acionado.
    """
    # Dado uma série perfeitamente formatada como datetime
    s = pd.Series(pd.to_datetime(["2024-01-01", "2024-01-02"]))

    # Fazemos um patch (mock) DIRETAMENTE na referência que o seu módulo usa
    # SOTA: Patching the 'pd' object inside the target module to verify bypass
    with patch(
        "shared.infrastructure.adapters.pandas.types.pd.to_datetime"
    ) as mock_to_datetime:
        # Quando executamos a função
        result = ensure_datetime_col(s)

        # Então a função de conversão NÃO deve ter sido chamada (Otimização preservada)
        mock_to_datetime.assert_not_called()

        # E o resultado deve ser exatamente o objeto original na memória
        assert result is s


def test_ensure_datetime_col_calls_pandas_with_exact_safeguards():
    """
    Testa se o motor de conversão do Pandas é invocado com as salvaguardas
    exatas de performance e resiliência (errors='coerce' e format='mixed').
    Isto previne regressões onde desenvolvedores removam estes kwargs.
    """
    # Dado uma série de strings que precisa de conversão
    s = pd.Series(["2024-01-01"])

    # Interceptamos a chamada ao Pandas
    with patch(
        "shared.infrastructure.adapters.pandas.types.pd.to_datetime"
    ) as mock_to_datetime:
        # Configuramos o mock para devolver um valor qualquer para não quebrar a lógica
        mock_to_datetime.return_value = pd.Series([pd.Timestamp("2024-01-01")])

        # Quando a função é executada
        ensure_datetime_col(s)

        # Então GARANTIMOS que foi chamada com os parâmetros arquiteturais corretos
        # Qualquer mutação no 'errors' ou 'format' falhará esta asserção imediatamente
        mock_to_datetime.assert_called_once_with(s, errors="coerce", format="mixed")
