class Pessoa:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.setor = None  # será definido depois


class Setor:
    def __init__(self, nome):
        self.nome = nome
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        pessoa.setor = self.nome


# =========================
# CADASTRO DE PESSOAS
# =========================

p1 = Pessoa("Alexandre Castro", "8426")
p2 = Pessoa("Sandro", "8992")
p3 = Pessoa("Fabiane", "8584")
p4 = Pessoa("Henrique", "8422")
p5 = Pessoa("Rodolfo", "8430")
p6 = Pessoa("Karen - estagiária", "8419")

pessoas = [p1, p2, p3, p4, p5, p6]

# =========================
# CRIAR SETORES
# =========================

convenio = Setor("Convênios - DCP")
rh = Setor("RH")
ti = Setor("TI")
marketing = Setor("Marketing")

# =========================
# ADICIONAR PESSOAS AOS SETORES
# =========================

# você pode escolher pelo nome
while True:
    for pessoa in pessoas:
        if pessoa.nome in ["Alexandre Castro", "Sandro", "Fabiane", "Henrique", "Rodolfo", "Karen - estagiária"]:
            convenio.adicionar_pessoa(pessoa)

    # =========================
    # BUSCA POR NOME
    # =========================

    busca = input("\nDigite o nome para filtrar: ").lower()

    for pessoa in pessoas:
        if busca in pessoa.nome.lower():
            print("\nNome:", pessoa.nome)
            print("Número:", pessoa.numero)
            print("Setor:", pessoa.setor)