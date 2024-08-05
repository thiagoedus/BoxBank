def retorna_choices_chave_pix(user):
    chave_pix = []

    if user.cpf:
        chave_pix.append(('CPF', user.cpf))

    if user.email:
        chave_pix.append(('EM', user.email))

    if user.telefone:
        chave_pix.append(('TEL', user.telefone))

    return tuple(chave_pix)


estados_conta = (
    ('A', 'ATIVA'),
    ('D','DESATIVADA'),
    ('B','BLOQUEADA'),
    ('C','CONGELADA'),
    ('E','ENCERRADA'),
    ('P','PENDENTE'),
)