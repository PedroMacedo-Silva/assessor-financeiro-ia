"""Tools usadas pelos agentes para montar operações sem persistir dados."""
import json

from langchain.tools import tool
from app.tools.financeiro import AddTransactionArgs, UpdateTransactionArgs
from app.tools.agenda import AddEventArgs


def _serializar(operacao: str, argumentos: dict) -> str:
    return json.dumps({
        "status": "ok",
        "pending": True,
        "operation": operacao,
        "arguments": argumentos,
        "message": "Proposta preparada; aguardando o juiz antes da gravação.",
    }, ensure_ascii=False)


@tool("add_transaction", args_schema=AddTransactionArgs)
def preparar_add_transaction(**kwargs) -> str:
    """Prepara uma transação; a persistência ocorre após o juiz aprovar."""
    return _serializar("add_transaction", kwargs)


@tool("update_transaction", args_schema=UpdateTransactionArgs)
def preparar_update_transaction(**kwargs) -> str:
    """Prepara uma atualização financeira para persistência após o juiz."""
    return _serializar("update_transaction", kwargs)


@tool("add_event", args_schema=AddEventArgs)
def preparar_add_event(**kwargs) -> str:
    """Prepara um compromisso; a persistência ocorre após o juiz aprovar."""
    return _serializar("add_event", kwargs)
