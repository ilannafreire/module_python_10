# MATERIAL DE DEFESA - MÓDULO 10

**Projeto:** FuncMage - Functional Programming

## 1. Visão geral do projeto

O projeto FuncMage é uma coleção de cinco exercícios de Python sobre programação funcional. O tema usa uma narrativa de magia, mas o objetivo técnico é mostrar como funções podem ser tratadas como valores: podem ser passadas como argumentos, retornadas por outras funções e combinadas para criar comportamentos reutilizáveis.

O projeto resolve pequenos problemas de transformação e composição de dados: organiza artefatos, filtra magos, transforma nomes, combina feitiços, mantém estado privado, agrega valores, economiza cálculos repetidos e adiciona comportamentos como validação, medição de tempo e tentativas de repetição.

A progressão é:

- `ex0` - expressões lambda e `map`/`filter`/`sorted`
- `ex1` - funções de primeira classe e funções de ordem superior
- `ex2` - escopo léxico, closures e estado privado
- `ex3` - ferramentas do módulo `functools`
- `ex4` - decorators, decorator factories e `staticmethod`

### Requisitos gerais do enunciado

- Python 3.10 ou mais recente.
- Type hints nas assinaturas e nos retornos.
- Cada exercício fica em seu próprio arquivo.
- Sem bibliotecas externas, I/O de arquivos, `eval()`, `exec()` ou variáveis globais.
- O foco deve ser explicar o padrão funcional, e não criar algoritmos complexos.

## 2. Como executar e testar

Na raiz do projeto:

```bash
python3 --version
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

Para verificar compilação:

```bash
python3 -m compileall -q ex0 ex1 ex2 ex3 ex4
```

## 3. Exercício 0 - Lambda Sanctum

**Arquivo:** `ex0/lambda_spells.py`

O exercício pede lambda nas transformações. Lambda é uma função anônima curta, apropriada para uma operação simples usada localmente.

- `artifact_sorter(artifacts)`: usa `sorted()` com `lambda item: item["power"]` e `reverse=True`. Retorna artefatos do maior para o menor poder. `sorted` cria uma nova lista.
- `power_filter(mages, min_power)`: usa `filter()` com `lambda mage: mage["power"] >= min_power` e converte o resultado para `list`.
- `spell_transformer(spells)`: usa `map()` com `lambda spell: f"* {spell} *"` e retorna os nomes transformados em uma lista.
- `mage_stats(mages)`: usa `max()` e `min()` com lambdas que extraem `power`, calcula a média com `sum()`/`len()` e arredonda com `round(..., 2)`. Para lista vazia, retorna zeros e evita divisão por zero.

### Teste

```bash
python3 ex0/lambda_spells.py
```

### Saída observada

```text
Testing artifact sorter...
Fire Staff (92 power) comes before Crystal Orb (85 power)
Testing power filter...
[{'name': 'Potira', 'power': 95, 'element': 'fire'}, {'name': 'Jutai', 'power': 80, 'element': 'wind'}]
Testing spell transformer...
* fireball * * heal * * shield *
Testing mage stats...
{'max_power': 95, 'min_power': 60, 'avg_power': 78.33}
```

**Defesa:** lambda deixa a operação concisa quando ela é pequena e local. Uma função `def` é melhor quando a lógica é reutilizada, tem várias instruções, precisa de nome ou de documentação detalhada.

## 4. Exercício 1 - Higher Realm

**Arquivo:** `ex1/higher_magic.py`

Funções de ordem superior recebem funções, retornam funções ou fazem as duas coisas. Em Python, funções são objetos de primeira classe: podem ser guardadas, passadas como argumentos e retornadas.

- `spell_combiner(spell1, spell2)`: cria uma função que envia os mesmos argumentos aos dois feitiços e retorna uma tupla com os resultados.
- `power_amplifier(base_spell, multiplier)`: cria uma função que multiplica `power` antes de chamar o feitiço original.
- `conditional_caster(condition, spell)`: cria uma função que chama `spell` quando `condition` é `True`; caso contrário, retorna `"Spell fizzled"`. Ambos recebem os mesmos argumentos.
- `spell_sequence(spells)`: cria uma função que percorre os feitiços na ordem, passando os mesmos argumentos, e retorna uma lista de resultados.

### Teste

```bash
python3 ex1/higher_magic.py
```

### Saída observada

```text
Testing spell combiner...
('Fireball hits Dragon for 10 damage', 'Heal restores Dragon for 10 HP')
Testing power amplifier...
Fireball hits Dragon for 30 damage
Testing conditional caster...
Spell fizzled
Fireball hits Dragon for 12 damage
Testing spell sequence...
['Fireball hits Knight for 7 damage', 'Heal restores Knight for 7 HP']
```

**Defesa:** o ganho é reuso e composição. `Callable` vem de `collections.abc` para anotação de tipos. `callable(obj)` é uma função built-in que verifica em tempo de execução se um objeto pode ser chamado; não substitui a anotação `Callable`.

## 5. Exercício 2 - Memory Depths

**Arquivo:** `ex2/scope_mysteries.py`

Closure é a função interna junto com as variáveis do escopo externo que ela capturou. O escopo léxico resolve nomes conforme o local em que a função foi criada.

- `mage_counter()`: cria `count=0` e retorna `counter`. A função interna usa `nonlocal count`, incrementa e retorna o contador. Cada chamada a `mage_counter` cria um estado independente.
- `spell_accumulator(initial_power)`: captura `total` e usa `nonlocal` para somar `amount`. O total permanece entre chamadas sem variável global.
- `enchantment_factory(enchantment_type)`: captura o tipo e retorna uma função que recebe `item_name` e produz `"tipo item"`. `flaming` e `frozen` carregam valores diferentes.
- `memory_vault()`: cria `storage` dentro da função e retorna um dicionário com `store` e `recall`. As duas funções compartilham o `storage` privado. `recall` usa `"Memory not found"` para chave ausente.

### Teste

```bash
python3 ex2/scope_mysteries.py
```

### Saída observada

```text
Testing mage counter...
1
2
1
Testing spell accumulator...
120
150
Testing enchantment factory...
Flaming Sword
Frozen Shield
Testing memory vault...
42
Memory not found
```

**Defesa:** uma closure lembra o ambiente de criação porque mantém referências a variáveis livres. Isso encapsula estado e cria objetos independentes sem classe ou global. `nonlocal` altera uma variável do escopo externo; `global` alteraria o escopo do módulo e compartilharia estado.

## 6. Exercício 3 - Ancient Library

**Arquivo:** `ex3/functools_artifacts.py`

- `spell_reducer(spells, operation)`: usa `functools.reduce` para combinar uma lista em um valor. `add` usa `operator.add`, `multiply` usa `operator.mul`, `max` e `min` usam lambdas. Lista vazia retorna `0`. Operação desconhecida gera `ValueError`.
- `partial_enchanter(base_enchantment)`: usa `functools.partial` para fixar `power=50` e cada elemento (`fire`, `ice` e `storm`). Retorna três funções especializadas e sobra apenas `target`.
- `memoized_fibonacci(n)`: usa `@lru_cache(maxsize=None)`. A recursão calcula $F(n)=F(n-1)+F(n-2)$, com caso-base `n<2`. `cache_info()` mostra hits, misses e tamanho do cache.
- `spell_dispatcher()`: usa `@singledispatch`. O caso base trata `Any` como desconhecido; registros específicos tratam `int` como dano, `str` como encantamento e `list` como multi-cast.

### Teste

```bash
python3 ex3/functools_artifacts.py
```

### Saída observada

```text
Testing spell reducer...
60
6000
30
Testing partial enchanter...
fire enchantment on dragon at power 50
Testing memoized fibonacci...
0
1
55
CacheInfo(hits=10, misses=11, maxsize=None, currsize=11)
Testing spell dispatcher...
Damage spell: 42 damage
Enchantment: fireball
Multi-cast: 3 spells
Unknown spell type
```

**Defesa:** `reduce` transforma vários valores em um acumulado. Memoização troca cálculo por memória e evita subproblemas repetidos. `singledispatch` escolhe a implementação pelo tipo do primeiro argumento.

## 7. Exercício 4 - Master's Tower

**Arquivo:** `ex4/decorator_mastery.py`

Decorator é uma função que recebe outra função e devolve uma versão envolvida. Ele adiciona uma preocupação transversal sem misturar essa lógica com a regra principal.

- `spell_timer(func)`: o wrapper imprime o início, mede com `time.perf_counter()`, executa `func` e imprime o tempo com três casas decimais. Retorna o resultado. `@wraps` preserva nome e docstring.
- `power_validator(min_power)`: é uma decorator factory. O wrapper procura `power` em `kwargs` e depois no último argumento posicional. Se for numérico e `>= min_power`, executa; senão retorna `"Insufficient power for this spell"`.
- `retry_spell(max_attempts)`: é outra decorator factory. O wrapper tenta executar até o limite, captura `Exception` e imprime cada tentativa. Se todas falham, retorna a mensagem final.
- `MageGuild.validate_mage_name`: é `@staticmethod` porque não depende de `self`. Remove espaços nas pontas, exige pelo menos três caracteres e usa `isalpha()` depois de remover espaços internos.
- `MageGuild.cast_spell`: é método de instância e usa `@power_validator(10)`. Com poder suficiente retorna a mensagem de sucesso; com pouco poder retorna a mensagem de validação.
- `make_flaky_spell()`: usa closure para contar chamadas; falha duas vezes e funciona na terceira, demonstrando retry.

### Teste

```bash
python3 ex4/decorator_mastery.py
```

### Saída observada

```text
Testing spell timer...
Casting fireball...
Spell completed in 0.000 seconds
Fireball cast!
Testing retrying spell...
Spell failed, retrying... (attempt 1/3)
Spell failed, retrying... (attempt 2/3)
Successful cast after retries
Testing MageGuild...
True
False
Successfully cast Lightning with 15 power
Insufficient power for this spell
```

O tempo varia entre execuções. O enunciado permite `time.sleep` para simular espera, mas o código atual não usa `sleep`; por isso o tempo fica normalmente próximo de `0.000` segundos.

**Defesa:** decorators separam preocupações. A função cuida do feitiço, enquanto timer, validação e retry cuidam de infraestrutura. `@staticmethod` não recebe `self` automaticamente e pode ser chamado pela classe; método de instância recebe `self`. `@wraps` preserva metadados.

## 8. O que há dentro do código

Todos os arquivos possuem funções pequenas, docstrings, type hints e um bloco `if __name__ == "__main__"` com dados de demonstração. Esse bloco roda somente quando o arquivo é executado diretamente; ao importar o módulo, as funções ficam disponíveis sem imprimir os testes.

Os tipos principais são `list`, `dict`, `str`, `int`, `float`, `Callable` e `Any`. Os dados ficam em memória. Não há leitura ou escrita de arquivos nos exercícios, nem dependências de terceiros.

## 9. Resumo para falar na defesa

> O módulo 10 ensina programação funcional em Python por uma progressão de abstrações. Começa com lambdas para operações locais, passa por funções de ordem superior para compor comportamentos, usa closures para manter estado privado, explora `reduce`, `partial`, `lru_cache` e `singledispatch` em `functools`, e termina com decorators para separar responsabilidades. Cada exercício tem uma função de demonstração e um bloco main para validar o resultado no terminal. O projeto evita estado global, I/O e bibliotecas externas, mantendo o foco no comportamento das funções.

### Perguntas práticas

- Por que converter `map`/`filter` para `list`? Para materializar o iterável e devolver o tipo pedido.
- O que acontece com dois `mage_counter`? Cada chamada cria uma closure e um `count` diferente.
- Como testar o cache? Executar `memoized_fibonacci` e consultar `cache_info()`.
- O que ocorre em operação inválida? `spell_reducer` levanta `ValueError`.
- O que ocorre quando retry consegue executar? O resultado é devolvido imediatamente.
- Por que usar `wraps`? Para preservar os metadados da função decorada.
