def criptografa_cpf(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    cpf_formatado = "***"
    cpf_formatado += cpf[3:6] + "." + cpf[6:9] +"-**"
    return cpf_formatado