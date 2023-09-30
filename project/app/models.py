from django.db import models

class Mapeamento(models.Model):
    class Mapeamento(models.Model):
    CODIGO = models.IntegerField()
    NOME = models.CharField(max_length=200)
    SALDO = models.DecimalField(max_digits=10, decimal_places=2)
    DATA_ASSINATURA = models.DateField()
    DATA_VIGENCIA = models.DateField()
    DATA_ENCERRAMENTO = models.DateField()
    TIPO_CONTRATO = models.CharField(max_length=200)
    INSTITUICAO_EXECUTORA = models.CharField(max_length=200)
    PROCESSO = models.CharField(max_length=200)
    SUBPROCESSO = models.CharField(max_length=200)
    COD_PROPOSTA = models.IntegerField()
    PROPOSTA = models.CharField(max_length=200)
    OBJETIVOS = models.TextField()
    VALOR_APROVADO = models.DecimalField(max_digits=10, decimal_places=2)
    NOME_TP_CONTROLE_SALDO = models.CharField(max_length=200)
    GRUPO_GESTORES = models.CharField(max_length=200)
    GESTOR_RESP = models.CharField(max_length=200)
    COORDENADOR = models.CharField(max_length=200)
    PROCEDIMENTO_COMPRA = models.CharField(max_length=200)
    TAB_FRETE = models.CharField(max_length=200)
    TAB_DIARIAS = models.CharField(max_length=200)
    CUSTO_OP = models.DecimalField(max_digits=10, decimal_places=2)
    NOME_FINANCIADOR = models.CharField(max_length=200)
    DEPARTAMENTO = models.CharField(max_length=200)
    SITUACAO = models.CharField(max_length=200)
    BANCO = models.CharField(max_length=200)
    AGENCIA_BANCARIA = models.CharField(max_length=200)
    CONTA_BANCARIA = models.CharField(max_length=200)
    CENTRO_CUSTO = models.CharField(max_length=200)
    CONTA_CAIXA = models.CharField(max_length=200)
    CATEGORIA_PROJETO = models.CharField(max_length=200)
    COD_CONVENIO_CONTA = models.IntegerField()
    COD_STATUS = models.IntegerField()
    IND_SUB_PROJETO = models.CharField(max_length=200)
    TIPO_CUSTO_OP = models.CharField(max_length=200)
    PROJETO_MAE = models.IntegerField()
    ID_COORDENADOR = models.IntegerField()
    ID_FINANCIADOR = models.IntegerField()
    ID_INSTITUICAO = models.IntegerField()
    ID_DEPARTAMENTO = models.IntegerField()
    NOME_INSTITUICAO = models.CharField(max_length=200)
    ID_INSTITUICAO_EXECUTORA = models.IntegerField()
    ID_TIPO = models.IntegerField()

class Template(models.Model):
    nome_template = models.CharField(max_length=200)
    endereco_template = models.CharField(max_length=200)
    mapeamento = models.ForeignKey(Mapeamento, on_delete=models.CASCADE)

class Report(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    tipo_erro = models.CharField(max_length=200)
    id_projeto = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=200)

class Export(models.Model):
    data_export = models.DateTimeField(auto_now_add=True)
    formato = models.CharField(max_length=200)
    nome_template = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=200)
    id_projeto = models.CharField(max_length=200)
