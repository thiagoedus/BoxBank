

teste_boleto = """
<html charset="UTF-8">

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="robots" content="noindex">
        <style>
                body {
                font-family: "Arial";
            }

            @media print {
                .no-print,
                .no-print * {
                    display: none !important;
                }
            }

            .document {
                margin: auto auto;
                width: 216mm;
                height: 108mm;
                background-color: #fff;
            }

            .headerBtn {
                margin: auto auto;
                width: 216mm;
                background-color: #fff;
                display: none;
            }

            table {
                width: 100%;
                position: relative;
                border-collapse: collapse;
            }

            .bankLogo {
                width: 28%;
            }

            .boletoNumber {
                width: 62%;
                font-weight: bold;
            }

            .center {
                text-align: center;
            }

            .right {
                text-align: right;
                right: 20px;
            }

            td {
                position: relative;
            }

            .title {
                position: absolute;
                left: 0px;
                top: 0px;
                font-size: 12px;
                font-weight: bold;
            }

            .text {
                font-size: 12px;
            }

            p.content {
                padding: 0px;
                width: 100%;
                margin: 0px;
                font-size: 12px;
            }

            .sideBorders {
                border-left: 1px solid black;
                border-right: 1px solid black;
            }

            hr {
                size: 1;
                border: 1px dashed;
            }

            br {
                content: " ";
                display: block;
                margin: 12px 0;
                line-height: 12px;
            }

            .print {
                /* TODO(dbeam): reconcile this with overlay.css' .default-button. */
                background-color: rgb(77, 144, 254);
                background-image: linear-gradient(to bottom, rgb(77, 144, 254), rgb(71, 135, 237));
                border: 1px solid rgb(48, 121, 237);
                color: #fff;
                text-shadow: 0 1px rgba(0, 0, 0, 0.1);
            }

            .btnDefault {
                font-kerning: none;
                font-weight: bold;
            }

            .btnDefault:not(:focus):not(:disabled) {
                border-color: #808080;
            }

            button {
                border: 1px;
                padding: 5px;
                line-height: 20px;
            }


        
        i[class*=icss-]{position:relative;display:inline-block;font-style:normal;background-color:currentColor;-webkit-box-sizing:border-box;box-sizing:border-box;vertical-align:middle}i[class*=icss-]:after,i[class*=icss-]:before{content:"";border-width:0;position:absolute;-webkit-box-sizing:border-box;box-sizing:border-box}i.icss-print{width:.68em;height:1em;border-style:solid;border-color:currentcolor;border-width:.07em;-webkit-border-radius:.05em;border-radius:.05em;background-color:transparent;margin:0 .17em}i.icss-print:before{width:1em;height:.4em;border-width:.07em .21em 0;border-style:solid;border-color:currentColor currentcolor transparent;-webkit-border-radius:.05em .05em 0 0;border-radius:.05em .05em 0 0;top:.25em;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);background-image:-webkit-gradient(linear,left top,left bottom,color-stop(20%,transparent),color-stop(20%,currentcolor),color-stop(60%,currentcolor),color-stop(60%,transparent));background-image:-webkit-linear-gradient(transparent 20%,currentcolor 20%,currentcolor 60%,transparent 60%);background-image:-o-linear-gradient(transparent 20%,currentcolor 20%,currentcolor 60%,transparent 60%);background-image:linear-gradient(transparent 20%,currentcolor 20%,currentcolor 60%,transparent 60%)}i.icss-print:after{width:.45em;height:.065em;background-color:currentColor;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);top:.6em;-webkit-box-shadow:0 .12em,-.1em -.28em 0 .05em;box-shadow:0 .12em,-.1em -.28em 0 .05em}i.icss-files{width:.75em;height:.95em;background-color:transparent;border:.05em solid transparent;border-width:0 .05em .05em 0;-webkit-box-shadow:inset 0 0 0 .065em,.13em .11em 0 -.05em;box-shadow:inset 0 0 0 .065em,.13em .11em 0 -.05em;-webkit-border-radius:0 .3em 0 0;border-radius:0 .3em 0 0;margin:0 .17em .05em .1em}i.icss-files:before{border-style:solid;border-width:.2em;top:.037em;left:.25em;-webkit-border-radius:.1em;border-radius:.1em;border-color:transparent currentColor transparent transparent;-webkit-transform:rotate(-45deg);-ms-transform:rotate(-45deg);transform:rotate(-45deg)}
            </style>

            <script type="text/javascript">
                window.onload = function getUrlParams() {
                    var url_string = window.location.href;
                    var url = new URL(url_string);
                
                    var fmt = url.searchParams.get("fmt");
                
                    if(fmt === "html") {
                        document.getElementById("headerBtn").style.display = "block";
                    } 
                }
            </script>    
    </head>

    <body>
        <br/>
        <div class="headerBtn" id="headerBtn">
            <div style="text-align:right;">
                        
            </div>
        </div>
        <br/>
        <div class="document">
            <table cellspacing="0" cellpadding="0">
                <tr class="topLine">
                    <td class="bankLogo" style='text-align:center'>
                        <img src="templates/static/global/img/logo_boleto.png"
                            style="width:200px" alt="">
                    </td>
                    <td class="sideBorders center"><span style="font-size:24px;font-weight:bold;">902-0</span></td>
                    <td class="boletoNumber center"><span>{{boleto.codigo}}</span></td>
                </tr>
            </table>
            <table cellspacing="0" cellpadding="0" border="1">
                <tr>
                    <td width="70%" colspan="6">
                        <span class="title">Local de Pagamento</span>
                        <br/>
                        <span class="text">ATÉ O VENCIMENTO EM QUALQUER BANCO OU CORRESPONDENTE NÃO BANCÁRIO, APÓS O VENCIMENTO, PAGUE EM QUALQUER BANCO OU CORRESPONDENTE NÃO BANCÁRIO</span>
                    </td>
                    <td width="30%">
                        <span class="title">Data de Vencimento</span>
                        <br/>
                        <br/>
                        <p class="content right text" style="font-weight:bold;">{{boleto.vencimento}}</p>
                    </td>
                </tr>
                <tr>
                    <td width="70%" colspan="6">
                        <span class="title">Nome do Beneficiário / CNPJ / CPF / Endereço:</span>
                        <br/>
                        <table border="0" style="border:none">
                            <tr>
                                <td width="60%"><span class="text">{{beneficiario.nome_completo}}</span></td>
                                <td><span class="text">CPF/CNPJ {{beneficiario.cpf}}</span></td>
                            </tr>
                        </table>
                        <br/>
                        <span class="text">{{endereco_beneficiario.logradouro}}, {{endereco_beneficiario.numero}} - {{endereco_beneficiario.bairro}} - {{endereco_beneficiario.cidade}} - {{endereco_beneficiario.estado}} - {{endereco_beneficiario.cep}}</span>
                    </td>
                    <td width="30%">
                        <span class="title">Agência/Código Beneficiário</span>
                        <br/>
                        <br/>
                        <p class="content right">{{conta_beneficiario.agencia}}/{{conta_beneficiario.numero_conta}}</p>
                    </td>
                </tr>

                <tr>
                    <td width="15%">
                        <span class="title">Data do Documento</span>
                        <br/>
                        <p class="content center">{{boleto.data_e_hora_processamento}}</p>
                    </td>
                    <td width="17%" colspan="2">
                        <span class="title">Num. do Documento</span>
                        <br/>
                        <p class="content center">{{boleto.id}}</p>
                    </td>
                    <td width="10%">
                        <span class="title">Espécie doc</span>
                        <br/>
                        <p class="content center">DM</p>
                    </td>
                    <td width="8%">
                        <span class="title">Aceite</span>
                        <br/>
                        <p class="content center">N</p>
                    </td>
                    <td>
                        <span class="title">Data Processamento</span>
                        <br/>
                        <p class="content center">{{boleto.data_e_hora_processamento}}</p>
                    </td>
                    <td width="30%">
                        <span class="title">Carteira/Nosso Número</span>
                        <br/>
                        <br/>
                        <p class="content right">157/12345678-9</p>
                    </td>
                </tr>

                <tr>
                    <td width="15%">
                        <span class="title">Uso do Banco</span>
                        <br/>
                        <p class="content center">&nbsp;</p>
                    </td>
                    <td width="10%">
                        <span class="title">Carteira</span>
                        <br/>
                        <p class="content center">157</p>
                    </td>
                    <td width="10%">
                        <span class="title">Espécie</span>
                        <br/>
                        <p class="content center">R$</p>
                    </td>
                    <td width="8%" colspan="2">
                        <span class="title">Quantidade</span>
                        <br/>
                        <p class="content center">N</p>
                    </td>
                    <td>
                        <span class="title">Valor</span>
                        <br/>
                        <p class="content center">{{boleto.valor}}0</p>
                    </td>
                    <td width="30%">
                        <span class="title">(=) Valor do Documento</span>
                        <br/>
                        <br/>
                        <p class="content right">{{boleto.valor}}0</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="6" rowspan="4">
                        <span class="title">Instruções de responsabilidade do BENEFICIÁRIO. Qualquer dúvida sobre este boleto contate o beneficiário.</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(-) Descontos/Abatimento</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(+) Juros/Multa</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(=) Valor Pago</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="7">
                        <table border="0" style="border:none">
                            <tr>
                                <td width="60%"><span class="text"><b>Nome do Pagador: </b> {{beneficiario.nome_completo}}</span></td>
                                <td><span class="text"><b>CNPJ/CPF: </b> {{beneficiario.cpf}}</span></td>
                            </tr>
                            <tr>
                                <td><span class="text"><b>Endereço: </b> {{endereco_beneficiario.logradouro}}, {{endereco_beneficiario.numero}} - {{endereco_beneficiario.bairro}} - {{endereco_beneficiario.cidade}} - {{endereco_beneficiario.estado}} - {{endereco_beneficiario.cep}}</span></td>
                                <td>&nbsp;</td>
                            </tr>
                            <tr>
                                <td><span class="text"><b>Sacador/Avalista: </b> &nbsp;</span></td>
                                <td><span class="text"><b>CNPJ/CPF: </b> &nbsp;</span></td>
                            </tr>
                        </table>

                    </td>

                </tr>
            </table>
        </div>
        <div class="document">
            <hr/>
            <table cellspacing="0" cellpadding="0">
                <tr class="topLine">
                    <td class="bankLogo" style='text-align: center'>
                        <img src="templates/static/global/img/logo_boleto.png"
                            alt="" style='width: 200px'>
                    </td>
                    <td class="sideBorders center"><span style="font-size:24px;font-weight:bold;">902-0</span></td>
                    <td class="boletoNumber center"><span>{{boleto.codigo}}</span></td>
                </tr>
            </table>
            <table cellspacing="0" cellpadding="0" border="1">
                <tr>
                    <td width="70%" colspan="6">
                        <span class="title">Local de Pagamento</span>
                        <br/>
                        <span class="text">ATÉ O VENCIMENTO EM QUALQUER BANCO OU CORRESPONDENTE NÃO BANCÁRIO, APÓS O VENCIMENTO, PAGUE EM QUALQUER BANCO OU CORRESPONDENTE NÃO BANCÁRIO</span>
                    </td>
                    <td width="30%">
                        <span class="title">Data de Vencimento</span>
                        <br/>
                        <br/>
                        <p class="content right text" style="font-weight:bold;">01/01/2016</p>
                    </td>
                </tr>
                <tr>
                    <td width="70%" colspan="6">
                        <span class="title">Nome do Beneficiário / CNPJ / CPF / Endereço:</span>
                        <br/>
                        <table border="0" style="border:none">
                            <tr>
                                <td width="60%"><span class="text">Simulação</span></td>
                                <td><span class="text">CPF/CNPJ {{beneficiario.cpf}}</span></td>
                            </tr>
                        </table>
                        <br/>
                        <span class="text">{{endereco_beneficiario.logradouro}}, {{endereco_beneficiario.numero}} - {{endereco_beneficiario.bairro}} - {{endereco_beneficiario.cidade}} - {{endereco_beneficiario.estado}} - {{endereco_beneficiario.cep}}</span>
                    </td>
                    <td width="30%">
                        <span class="title">Agência/Código Beneficiário</span>
                        <br/>
                        <br/>
                        <p class="content right">{{conta_beneficiario.agencia}}/{{conta_beneficiario.numero_conta}}</p>
                    </td>
                </tr>

                <tr>
                    <td width="15%">
                        <span class="title">Data do Documento</span>
                        <br/>
                        <p class="content center">{{boleto.data_e_hora_processamento}}</p>
                    </td>
                    <td width="17%" colspan="2">
                        <span class="title">Num. do Documento</span>
                        <br/>
                        <p class="content center">{{boleto.id}}</p>
                    </td>
                    <td width="10%">
                        <span class="title">Espécie doc</span>
                        <br/>
                        <p class="content center">DM</p>
                    </td>
                    <td width="8%">
                        <span class="title">Aceite</span>
                        <br/>
                        <p class="content center">N</p>
                    </td>
                    <td>
                        <span class="title">Data Processamento</span>
                        <br/>
                        <p class="content center">{{boleto.data_e_hora_processamento}}</p>
                    </td>
                    <td width="30%">
                        <span class="title">Carteira/Nosso Número</span>
                        <br/>
                        <br/>
                        <p class="content right">157/12345678-9</p>
                    </td>
                </tr>

                <tr>
                    <td width="15%">
                        <span class="title">Uso do Banco</span>
                        <br/>
                        <p class="content center">&nbsp;</p>
                    </td>
                    <td width="10%">
                        <span class="title">Carteira</span>
                        <br/>
                        <p class="content center">157</p>
                    </td>
                    <td width="10%">
                        <span class="title">Espécie</span>
                        <br/>
                        <p class="content center">R$</p>
                    </td>
                    <td width="8%" colspan="2">
                        <span class="title">Quantidade</span>
                        <br/>
                        <p class="content center">N</p>
                    </td>
                    <td>
                        <span class="title">Valor</span>
                        <br/>
                        <p class="content center">{{boleto.valor}}0</p>
                    </td>
                    <td width="30%">
                        <span class="title">(=) Valor do Documento</span>
                        <br/>
                        <br/>
                        <p class="content right">{{boleto.valor}}0</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="6" rowspan="4">
                        <span class="title">Instruções de responsabilidade do BENEFICIÁRIO. Qualquer dúvida sobre este boleto contate o beneficiário.</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(-) Descontos/Abatimento</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(+) Juros/Multa</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="title">(=) Valor Pago</span>
                        <br/>
                        <p class="content right">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="7">
                        <table border="0" style="border:none">
                            <tr>
                                <td width="60%"><span class="text"><b>Nome do Pagador: </b> {{beneficiario.nome_completo}}</span></td>
                                <td><span class="text"><b>CNPJ/CPF: </b> {{beneficiario.cpf}}</span></td>
                            </tr>
                            <tr>
                                <td><span class="text"><b>Endereço: </b> {{endereco_beneficiario.logradouro}}, {{endereco_beneficiario.numero}} - {{endereco_beneficiario.bairro}} - {{endereco_beneficiario.cidade}} - {{endereco_beneficiario.estado}} - {{endereco_beneficiario.cep}}</span></td>
                                <td>&nbsp;</td>
                            </tr>
                            <tr>
                                <td><span class="text"><b>Sacador/Avalista: </b> &nbsp;</span></td>
                                <td><span class="text"><b>CNPJ/CPF: </b> &nbsp;</span></td>
                            </tr>
                        </table>

                    </td>

                </tr>
            </table>
            <br/>
            <img src="data:image/png;base64,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"
                alt="">
            <br/>
            <br/>
            <br/>
        </div>
    </body>

    </html>"""

def criptografa_cpf(cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    cpf_formatado = "***"
    cpf_formatado += cpf[3:6] + "." + cpf[6:9] +"-**"
    return cpf_formatado