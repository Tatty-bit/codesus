def cadastrar_paciente(nome, cpf, data_nascimento, endereco):
    """Cadastra um paciente no sistema."""
    # Aqui você pode usar um banco de dados ou uma lista para armazenar os dados.
    # Por exemplo, usando uma lista:
    pacientes = []
    pacientes.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    return pacientes

def listar_pacientes(pacientes):
    """Lista os pacientes cadastrados."""
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for paciente in pacientes:
        print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Data de Nascimento: {paciente['data_nascimento']}, Endereço: {paciente['endereco']}")

def buscar_paciente(pacientes, cpf):
    """Busca um paciente pelo CPF."""
    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            return paciente
    return None

# Exemplo de uso:
pacientes = []
pacientes = cadastrar_paciente("João Silva", "123.456.789-00", "01/01/1990", "Rua A, 123")
pacientes = cadastrar_paciente("Maria Souza", "987.654.321-00", "15/05/1985", "Rua B, 456")

listar_pacientes(pacientes)

paciente_encontrado = buscar_paciente(pacientes, "123.456.789-00")
if paciente_encontrado:
    print(f"Paciente encontrado: {paciente_encontrado['nome']}")
else:
    print("Paciente não encontrado.")