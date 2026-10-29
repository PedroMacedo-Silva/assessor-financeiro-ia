# Decisão técnica — escrita após o juiz

## Decisão

As tools financeiras e de agenda usadas pelo chat agora preparam propostas. O nó `juiz` julga a resposta antes de qualquer gravação. O nó `efetivar_escritas` executa as propostas somente quando o juiz retorna aprovação explícita (`juiz:apoiada` com pontuação acima do limiar). Falta de chave, timeout, exceção, resposta inválida ou recusa não grava no PostgreSQL.

O nó final substitui a resposta candidata por uma confirmação baseada no resultado real da gravação, ou por uma mensagem de falha sem afirmar sucesso.

## Escritas abrangidas

- `add_transaction`
- `update_transaction`
- `add_event`

O fallback financeiro que gravava diretamente foi removido do caminho de execução. Se o agente não preparar a tool, nenhuma gravação é feita.

## Limites conhecidos

- As chamadas MCP diretas continuam usando as tools de domínio e não passam pelo juiz do grafo de chat.
- Se um turno propuser mais de uma escrita e uma delas falhar, as tools existentes usam commits próprios; não há atomicidade entre essas gravações.

## Arquivos

### Criados

- `app/tools/propostas.py` — tools de preparação sem persistência.
- `decisao_tecnica.md` — registro desta decisão.

### Modificados

- `app/agents.py` — especialistas usam as tools de preparação para as três escritas locais.
- `app/graph.py` — guarda propostas no estado do turno e adiciona o nó pós-juiz que executa as gravações.
- `app/juiz.py` — registra no estado se houve aprovação explícita.
