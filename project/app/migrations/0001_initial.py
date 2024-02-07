# Generated by Django 4.2.4 on 2024-02-07 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_export', models.DateTimeField(auto_now_add=True)),
                ('formato', models.CharField(max_length=200)),
                ('nome_template', models.CharField(max_length=200)),
                ('nome_usuario', models.CharField(max_length=200)),
                ('id_projeto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id_mapeamento', models.IntegerField(primary_key=True, serialize=False)),
                ('id_favorecido', models.CharField(max_length=200)),
                ('nome_favorecido', models.CharField(max_length=200)),
                ('cnpj_favorecido', models.CharField(max_length=200)),
                ('tipo_favorecido', models.CharField(max_length=200)),
                ('valor_lancado', models.CharField(max_length=200)),
                ('valor_pago', models.CharField(max_length=200)),
                ('data_vencimento', models.CharField(max_length=200)),
                ('id_status', models.CharField(max_length=200)),
                ('status_lancamento', models.CharField(max_length=200)),
                ('flag_receita', models.CharField(max_length=200)),
                ('data_baixa', models.CharField(max_length=200)),
                ('his_lancamento', models.CharField(max_length=200)),
                ('data_emissao', models.CharField(max_length=200)),
                ('num_doc_fin', models.CharField(max_length=200)),
                ('data_cria', models.CharField(max_length=200)),
                ('data_pagamento', models.CharField(max_length=200)),
                ('id_lancamento', models.CharField(max_length=200)),
                ('id_projeto', models.CharField(max_length=200)),
                ('id_rubrica', models.CharField(max_length=200)),
                ('nome_rubrica', models.CharField(max_length=200)),
                ('tipo_movimento', models.CharField(max_length=200)),
                ('id_tp_lancamento', models.CharField(max_length=200)),
                ('tipo_lancamento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mapeamento',
            fields=[
                ('id_mapeamento', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('saldo', models.CharField(max_length=200)),
                ('data_assinatura', models.CharField(max_length=200)),
                ('data_vigencia', models.CharField(max_length=200)),
                ('data_encerramento', models.CharField(max_length=200)),
                ('tipo_contrato', models.CharField(max_length=200)),
                ('instituicao_executora', models.CharField(max_length=200)),
                ('processo', models.CharField(max_length=200)),
                ('subprocesso', models.CharField(max_length=200)),
                ('cod_proposta', models.CharField(max_length=200)),
                ('proposta', models.CharField(max_length=200)),
                ('objetivos', models.CharField(max_length=200)),
                ('valor_aprovado', models.CharField(max_length=200)),
                ('nome_tp_controle_saldo', models.CharField(max_length=200)),
                ('grupo_gestores', models.CharField(max_length=200)),
                ('gestor_resp', models.CharField(max_length=200)),
                ('coordenador', models.CharField(max_length=200)),
                ('procedimento_compra', models.CharField(max_length=200)),
                ('tab_frete', models.CharField(max_length=200)),
                ('tab_diarias', models.CharField(max_length=200)),
                ('custo_op', models.CharField(max_length=200)),
                ('nome_financiador', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=200)),
                ('situacao', models.CharField(max_length=200)),
                ('banco', models.CharField(max_length=200)),
                ('agencia_bancaria', models.CharField(max_length=200)),
                ('conta_bancaria', models.CharField(max_length=200)),
                ('centro_custo', models.CharField(max_length=200)),
                ('conta_caixa', models.CharField(max_length=200)),
                ('categoria_projeto', models.CharField(max_length=200)),
                ('cod_convenio_conta', models.CharField(max_length=200)),
                ('cod_status', models.CharField(max_length=200)),
                ('ind_sub_projeto', models.CharField(max_length=200)),
                ('tipo_custo_op', models.CharField(max_length=200)),
                ('projeto_mae', models.CharField(max_length=200)),
                ('id_coordenador', models.CharField(max_length=200)),
                ('id_financiador', models.CharField(max_length=200)),
                ('id_instituicao', models.CharField(max_length=200)),
                ('id_departamento', models.CharField(max_length=200)),
                ('nome_instituicao', models.CharField(max_length=200)),
                ('id_instituicao_executora', models.CharField(max_length=200)),
                ('id_tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('tipo_erro', models.CharField(choices=[('erro1', 'Falta de informação no projeto'), ('erro2', 'Campo preenchido incorretamente')], max_length=20)),
                ('id_projeto', models.CharField(max_length=50)),
                ('nome_usuario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=50)),
                ('activity', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_template', models.CharField(max_length=200)),
                ('endereco_template', models.CharField(max_length=200)),
                ('mapeamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mapeamento')),
            ],
        ),
    ]
