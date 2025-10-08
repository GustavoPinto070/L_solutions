# test_extensivo_fp.py
import pytest
import builtins

import FP2526P1 as fp

# -----------------------
# Helpers para simular input()/output() em processa_jogada
# -----------------------
class FakeInput:
    def __init__(self, lines):
        self.lines = list(lines)
    def __call__(self, prompt=''):
        if not self.lines:
            raise EOFError("No more input")
        return self.lines.pop(0)

def conta_prefixo_jogada(output, jogador_id):
    """Count how many times the player prompt appears in output"""
    prefix = f"Jogada J{jogador_id}:"
    return output.count(prefix)

# -----------------------
# Testes para cria_conjunto
# -----------------------
def test_cria_conjunto_valido_vazio():
    # deve aceitar tuplos vazios e devolver dict vazio
    assert fp.cria_conjunto((), ()) == {}

@pytest.mark.parametrize("letras, occ", [
    (('A','B'), (1,2)),          # normal
    (('Ç',), (2,)),              # acento
])
def test_cria_conjunto_valido(letras, occ):
    d = fp.cria_conjunto(letras, occ)
    for i, l in enumerate(letras):
        assert d[l] == occ[i]

@pytest.mark.parametrize("letras, occ", [
    (('A','B'), (1,)),               # tamanhos diferentes
    ('A,B', (1,2)),                  # letras não tuplo
    (('A','B'), [1,2]),              # occ não tuplo
    (('A','A'), (1,1)),              # letra repetida
    (('a',), (1,)),                  # letra minúscula -> inválido
    (('Z',), (0,)),                  # ocorrencia zero -> inválido
    (('X',), (-1,)),                 # ocorrencia negativa -> inválido
    (('Y',), (1,)),                  # letra não em LETRAS -> inválido
    (('A',), (1.0,)),                # occ não int
])
def test_cria_conjunto_invalidos(letras, occ):
    with pytest.raises(ValueError):
        fp.cria_conjunto(letras, occ)

# -----------------------
# Testes para gera_numero_aleatorio (determinístico)
# -----------------------
def test_gera_numero_aleatorio_valores_conhecidos():
    # valores usados por outros testes
    assert fp.gera_numero_aleatorio(1) == 270369
    assert fp.gera_numero_aleatorio(25) == 6759192

# -----------------------
# Testes para permuta_letras (efeito destrutivo + determinismo)
# -----------------------
def test_permuta_letras_vazia_e_unitaria():
    l = []
    assert fp.permuta_letras(l, 123) is None
    assert l == []  # permanece vazia

    l2 = ['A']
    assert fp.permuta_letras(l2, 5) is None
    assert l2 == ['A']  # singleton não muda

def test_permuta_letras_resultados_deterministicos():
    letras = ['A','B','C','D','E','F','G','H','I','J']
    letras_copy = letras.copy()
    fp.permuta_letras(letras_copy, 1)
    assert letras_copy == ['D', 'B', 'A', 'C', 'G', 'H', 'I', 'F', 'E', 'J']
    letras2 = letras.copy()
    fp.permuta_letras(letras2, 2)
    assert letras2 == ['H', 'A', 'J', 'F', 'G', 'E', 'B', 'C', 'D', 'I']

# -----------------------
# Testes para baralha_conjunto
# -----------------------
def test_baralha_conjunto_tamanho():
    conj = {'A': 3, 'B': 2, 'Ç': 1}
    lst = fp.baralha_conjunto(conj, 7)
    assert len(lst) == 6
    for ch in lst:
        assert ch in conj  # só contém letras do conjunto

def test_baralha_conjunto_vazio():
    assert fp.baralha_conjunto({}, 1) == []

# -----------------------
# Testes para testa_palavra_padrao
# -----------------------
def test_testa_palavra_padrao_basico():
    conj = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
    assert not fp.testa_palavra_padrao('VACA', '....', conj)
    assert not fp.testa_palavra_padrao('VACA', '.A.', conj)
    assert fp.testa_palavra_padrao('VACA', '.A..', conj)

def test_testa_palavra_padrao_tamanho_diferente():
    conj = fp.cria_conjunto(('A',), (1,))
    assert not fp.testa_palavra_padrao('A', '..', conj)  # tamanhos diferentes -> False

def test_testa_palavra_padrao_usa_mais_que_há():
    conj = fp.cria_conjunto(('A',), (1,))
    # precisa de duas A mas só há uma
    assert not fp.testa_palavra_padrao('AA', '..', conj)

# -----------------------
# Testes para o tabuleiro e criação de casas
# -----------------------
def test_cria_tabuleiro_formato():
    tab = fp.cria_tabuleiro()
    assert isinstance(tab, list)
    assert len(tab) == 15
    assert all(len(linha) == 15 for linha in tab)
    assert all(elem == '.' for linha in tab for elem in linha)

def test_cria_tabuleiro_not_all_lines_same_reference():
    tab = fp.cria_tabuleiro()
    # garante que todas as linhas são listas diferentes
    assert all(tab[i] is not tab[j] for i in range(len(tab)) for j in range(i+1, len(tab)))

def test_cria_casa_valida_e_invalida():
    assert fp.cria_casa(8,8) == (8,8)
    with pytest.raises(ValueError):
        fp.cria_casa(0, 5)
    with pytest.raises(ValueError):
        fp.cria_casa(1, 20)
    with pytest.raises(ValueError):
        fp.cria_casa(1.5, 3)
    with pytest.raises(ValueError):
        fp.cria_casa(True, 7)

# -----------------------
# Testes para obtem_valor, insere_letra, obtem_sequencia, insere_palavra
# -----------------------
def test_insere_e_obtem_valor_e_sequencias():
    tab = fp.cria_tabuleiro()
    c1 = fp.cria_casa(8,6)
    c2 = fp.cria_casa(6,8)
    fp.insere_letra(tab, c1, 'A')
    fp.insere_letra(tab, c2, 'B')
    assert tab[7][5] == 'A' and tab[5][7] == 'B'
    assert fp.obtem_valor(tab, c1) == 'A'
    assert fp.obtem_valor(tab, c2) == 'B'

    # insere palavra horizontal e obter sequência
    tab2 = fp.cria_tabuleiro()
    fp.insere_palavra(tab2, fp.cria_casa(8,3), 'H', 'COMPUTADOR')
    assert fp.obtem_sequencia(tab2, fp.cria_casa(8,10), 'H', 3) == 'DOR'
    assert fp.obtem_sequencia(tab2, fp.cria_casa(7,5), 'V', 4) == '.M..'

# -----------------------
# Testes para tabuleiro_para_str (formato textual)
# -----------------------
import FP2526P1 as fp

# Representação esperada para um tabuleiro *vazio*
EXPECTED_EMPTY = '''                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+'''

# Representação esperada para um tabuleiro com palavras (caso que enviaste)
EXPECTED_FILLED = '''                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . P . . . . . . . . . |
 3 | . . . . . R . . . . . . . . . |
 4 | . . . . . O . . . . . . . . . |
 5 | . . . . . G . . . . . . . . . |
 6 | . . . . . R . . . . . . . . . |
 7 | . . . . . A . . . . . . . . . |
 8 | F U N D A M E N T O S . . . . |
 9 | . . . A . A . . . . . . . . . |
10 | . . . . . Ç . . . . . . . . . |
11 | . . . . . A . . . . . . . . . |
12 | . . . . . O . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+'''

def test_tabuleiro_para_str_exact_empty():
    """Compara a string inteira do tabuleiro vazio com o valor esperado (carácter a carácter)."""
    tab = fp.cria_tabuleiro()
    s = fp.tabuleiro_para_str(tab)
    assert s == EXPECTED_EMPTY, "Representação do tabuleiro vazio difere do esperado.\nDiferenças podem ser espaços/newlines extras ou formatação do header."

def test_tabuleiro_para_str_exact_filled():
    """Insere palavras tal como no exemplo e compara a string inteira com o esperado."""
    tab = fp.cria_tabuleiro()
    # Inserções tal como no exemplo que forneceste
    fp.insere_palavra(tab, fp.cria_casa(8,1), 'H', 'FUNDAMENTOS')
    fp.insere_palavra(tab, fp.cria_casa(8,4), 'V', 'DA')
    fp.insere_palavra(tab, fp.cria_casa(2,6), 'V', 'PROGRAMAÇAO')
    s = fp.tabuleiro_para_str(tab)
    assert s == EXPECTED_FILLED, "Representação do tabuleiro preenchido difere do esperado.\nVerifica espaços, alinhamento, e ausência de newlines extras."

def test_tabuleiro_para_str_components_and_whitespace():
    """
    Verificações granulares:
    - header (duas linhas) exatamente iguais;
    - top/bottom border exatamente iguais;
    - 15 linhas do corpo; cada linha comparada exatamente com a linha esperada;
    - ausência de espaços finais em cada linha;
    - ausência de newline extra final.
    """
    tab = fp.cria_tabuleiro()
    s = fp.tabuleiro_para_str(tab)
    got_lines = s.splitlines()
    expect_lines = EXPECTED_EMPTY.splitlines()

    # Comprimento e correspondência linha-a-linha
    assert len(got_lines) == len(expect_lines), f"Nº de linhas difere: obtidas {len(got_lines)} vs esperadas {len(expect_lines)}"

    # Header completo = primeiras 2 linhas
    assert got_lines[0] == expect_lines[0], f"Primeira linha do header difere.\nObtido: {got_lines[0]!r}\nEsperado: {expect_lines[0]!r}"
    assert got_lines[1] == expect_lines[1], f"Segunda linha do header difere.\nObtido: {got_lines[1]!r}\nEsperado: {expect_lines[1]!r}"

    # Top border (linha 2 no exemplo "expect_lines" é a terceira linha do ficheiro)
    assert got_lines[2] == expect_lines[2], f"Top border difere.\nObtido: {got_lines[2]!r}\nEsperado: {expect_lines[2]!r}"
    # Bottom border (última linha)
    assert got_lines[-1] == expect_lines[-1], f"Bottom border difere.\nObtido: {got_lines[-1]!r}\nEsperado: {expect_lines[-1]!r}"

    # Corpo: 15 linhas (entre border topo e border base)
    body_got = got_lines[3:-1]
    body_expect = expect_lines[3:-1]
    assert len(body_got) == 15, f"Corpo - linhas obtidas: {len(body_got)} (esperado 15)."

    # Linha a linha: igualdade exacta e sem espaços finais
    for i, (g, e) in enumerate(zip(body_got, body_expect), start=1):
        assert g == e, f"Linha de corpo {i} difere.\nObtido: {g!r}\nEsperado: {e!r}"
        # sem espaços finais
        assert g == g.rstrip(), f"Linha {i} tem espaços finais: {g!r}"

    # Garantir que não há newline duplo no fim (i.e. a string não termina com '\n\n')
    assert not s.endswith("\n\n"), "A representação termina com newline extra (\\n\\n)."

    # Garantir que a função não adiciona um newline final (consistente com EXPECTED_EMPTY)
    # EXPECTED_EMPTY não termina com '\n', por isso
    assert s.endswith(expect_lines[-1]), "A string final não termina exatamente com a border esperada."

# -----------------------
# Testes para cria_jogador e jogador_para_str
# -----------------------
def test_cria_jogador_valido_e_str():
    conj = fp.cria_conjunto(('C','A','O','N'), (2,1,3,1))
    j = fp.cria_jogador(1, 0, conj)
    assert j['id'] == 1 and j['pontos'] == 0 and isinstance(j['letras'], dict)
    s = fp.jogador_para_str(j)
    assert s.startswith("#1")

@pytest.mark.parametrize("ordem, pontos", [
    (5, 0),    # ordem inválida
    (1, -1),   # pontos negativos
    (True, 0), # ordem bool
    (1.0, 67), # ordem float
])
def test_cria_jogador_invalidos(ordem, pontos):
    with pytest.raises(ValueError):
        fp.cria_jogador(ordem, pontos, fp.cria_conjunto((),()))

def test_cria_jogador_too_many_letters():
    # mais de 7 peças deve ser inválido
    conj = {'A':8}
    with pytest.raises(ValueError):
        fp.cria_jogador(1, 0, conj)

# -----------------------
# Testes para distribui_letra
# -----------------------
def test_distribui_letra_basico():
    jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
    letras = ['A','B','C','A']
    assert fp.distribui_letra(letras, jog)  # True
    assert letras == ['A','B','C']
    assert jog['letras'] == {'A':1}

def test_distribui_letra_ate_vazio():
    jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
    letras = ['A','B','C','A']
    while letras:
        assert fp.distribui_letra(letras, jog)
    assert not fp.distribui_letra(letras, jog)
    assert jog['letras'] == {'A':2, 'C':1, 'B':1}

def test_distribui_letra_saco_vazio_nao_muda():
    jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
    saco = []
    assert not fp.distribui_letra(saco, jog)
    assert jog['letras'] == {}

# -----------------------
# Testes para joga_palavra (validações e regras)
# -----------------------
def test_joga_palavra_primeira_nao_centro():
    tab = fp.cria_tabuleiro()
    conj = fp.cria_conjunto(('C','A','O','N'),(2,1,3,1))
    assert fp.joga_palavra(tab, 'VACA', fp.cria_casa(1,1), 'H', conj, True) == (), "primeira jogada mas a palavra não passa pelo centro (must fail -> ())"

def test_joga_palavra_primeira_e_valida():
    tab = fp.cria_tabuleiro()
    conj = fp.cria_conjunto(('C','A','O','N'),(2,1,3,1))
    # colocar "VACA" com ponto de aplicação (8,8) horizontal vai atravessar centro?
    # Test similar ao ficheiro original: jogar 'VACA' no centro deve falhar porque não há letras no conj
    assert fp.joga_palavra(tab, 'VACA', fp.cria_casa(8,8), 'H', conj, True) == (), "jogar 'VACA' no centro deve falhar porque não há letras no conj (must fail -> ())"

def test_joga_palavra_nao_primeira_deve_conter_letra_existente():
    tab = fp.cria_tabuleiro()
    conj1 = fp.cria_conjunto(('C','A','O','N'),(2,1,3,1))
    # Jogar CAO no centro para preencher o tabuleiro
    assert fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj1, True) == ('A','C','O'), "jogar 'CAO' devia resultar, jogada no meio, primeira jogada"
    # Agora jogar 'PERO' que não intersecta nenhuma letra já no tab -> deve falhar (())
    conj2 = fp.cria_conjunto(('P','E','O','R'), (2,1,3,1))
    assert fp.joga_palavra(tab, 'PERO', fp.cria_casa(1,1), 'V', conj2, False) == (), "jogar 'PERO' que não intersecta nenhuma letra já no tab (must fail -> ())"

# -----------------------
# Testes para processa_jogada e scrabble
# -----------------------

def test_processa_jogada_pass(monkeypatch):
    """Se o jogador introduzir 'P' a função deve devolver False (passar)."""
    jogador = fp.cria_jogador(1, 0, fp.cria_conjunto((), ()))  # sem letras, id=1
    pilha = []
    pontos = {}  # não usado nesta jogada
    # Simular input "P"
    monkeypatch.setattr(builtins, 'input', FakeInput(["P"]))
    assert fp.processa_jogada(fp.cria_tabuleiro(), jogador, pilha, pontos, True) is False

def test_processa_jogada_troca_valida(monkeypatch):
    """
    Testa troca válida: jogador tem A,B; pilha tem >=7;
    invoca "T A B" e espera True e que A/B deixem de estar nas letras do jogador.
    """
    conj = fp.cria_conjunto(('A','B'), (1,1))
    jogador = fp.cria_jogador(1, 0, conj)
    # pilha com pelo menos 7 letras (o conteúdo importa porque são distribuídas)
    pilha = ['C','D','E','F','G','H','I']
    monkeypatch.setattr(builtins, 'input', FakeInput(["T A B"]))
    # usar um tabuleiro qualquer
    tab = fp.cria_tabuleiro()
    pontos = {}  # não usado na troca
    res = fp.processa_jogada(tab, jogador, pilha, pontos, True)
    assert res is True
    # As letras trocadas já não devem existir; o jogador deve ter recebido 2 novas letras
    assert 'A' not in jogador['letras'] and 'B' not in jogador['letras']
    assert sum(jogador['letras'].values()) == 2

def test_processa_jogada_troca_insufficient_pilha_then_pass(monkeypatch):
    """
    Se o jogador tentar trocar mas a pilha tiver < 7 letras, a troca não é aceite.
    Depois introduzimos "P" para terminar e validar que retorna False.
    """
    conj = fp.cria_conjunto(('A',), (1,))
    jogador = fp.cria_jogador(1, 0, conj)
    pilha = ['A', 'B']  # <7
    # Primeiro tenta trocar (ignorado porque pilha <7), depois passa
    monkeypatch.setattr(builtins, 'input', FakeInput(["T A", "P"]))
    tab = fp.cria_tabuleiro()
    pontos = {}
    assert fp.processa_jogada(tab, jogador, pilha, pontos, True) is False

def test_processa_jogada_joga_palavra_valida(monkeypatch):
    """
    Testa jogar uma palavra válida na primeira jogada que passa pelo centro.
    Verifica retorno True, atualização de pontos e inserção no tabuleiro.
    """
    tab = fp.cria_tabuleiro()
    # jogador com letras C,A,O necessárias para CAO
    conj = fp.cria_conjunto(('C','A','O'), (1,1,1))
    jogador = fp.cria_jogador(1, 0, conj)
    # pilha com letras para repor
    pilha = ['A','B','C']
    # pontos por letra usados na soma
    pontos = {'C':3, 'A':1, 'O':1}
    # Simular a jogada que coloca "CAO" com ponto de aplicação (8,8) horizontal
    monkeypatch.setattr(builtins, 'input', FakeInput(["J 8 8 H CAO"]))
    res = fp.processa_jogada(tab, jogador, pilha, pontos, True)
    assert res is True
    # pontos adicionados = 3 + 1 + 1 = 5
    assert jogador['pontos'] == 5
    # verificar que as letras foram efetivamente inseridas no tabuleiro
    seq = fp.obtem_sequencia(tab, fp.cria_casa(8,8), 'H', 3)
    assert seq == 'CAO'

def test_scrabble_quick_end(monkeypatch, capsys):
    """
    Testa scrabble com patch de processa_jogada para forçar duas passagens seguidas
    (dois jogadores -> termina). Verifica retorno das pontuações iniciais e
    que a função processa_jogada foi chamada exatamente duas vezes.
    """
    # saco com bastante letras para distribuir (2 de cada letra garante >=14 peças para 2 jogadores)
    saco = {let: 2 for let in fp.LETRAS}
    # pontos_por_letra deve conter todas as letras
    pontos_por_letra = {let: 1 for let in fp.LETRAS}

    calls = {'n': 0}
    def fake_processa_jogada(tab, jogador, pilha, pontos_pt, primeira):
        # incrementa contador e devolve False (pass) para terminar após duas chamadas
        calls['n'] += 1
        return False

    monkeypatch.setattr(fp, 'processa_jogada', fake_processa_jogada)

    # Executar scrabble com 2 jogadores — deve terminar após duas passagens (False, False)
    resultado = fp.scrabble(2, saco, pontos_por_letra, 1)
    # ambos começam com 0 pontos
    assert resultado == (0, 0)
    # processa_jogada chamado pelo menos duas vezes (uma por cada jogador)
    assert calls['n'] == 2

    captured = capsys.readouterr()
    assert "Bem-vindo ao SCRABBLE." in captured.out

def test_scrabble_invalid_args_raise():
    """Testa que scrabble valida argumentos e lança ValueError com inputs inválidos."""
    saco = {let: 1 for let in fp.LETRAS}
    pontos_por_letra = {let: 1 for let in fp.LETRAS}
    # num_jog inválido
    with pytest.raises(ValueError):
        fp.scrabble(1, saco, pontos_por_letra, 1)
    # saco vazio -> erro
    with pytest.raises(ValueError):
        fp.scrabble(2, {}, pontos_por_letra, 1)
    # pontos_por_letra não contém todas as letras -> erro
    with pytest.raises(ValueError):
        fp.scrabble(2, saco, {'A':1}, 1)
