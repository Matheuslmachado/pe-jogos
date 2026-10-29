


define e = Character("Beatriz") # ESTAGIÁRIA 
define c = Character("Civil", color="#9a9b9d") # CIVIL
define f = Character("Dep. de Justiça Fiscal", color="#f7e26c") # FISCAL
define a = Character("Jonas", color="#21cf32") # ANALISTA

# Definindo Blackgrand
image bg_call = "scene_1.png"
image bg_office = "scene_.png"
image bg_street = "img_4.png"
image bg_store = "img_1.jpg"
image bg_store2 = "img_5.png"
# The game starts here.

label start:


    scene bg_call

    # Inicio da história

    "Uma ligação é feito no departamento de justiça fiscal na Receita federal"

    c "Olá, gostaria de fazer uma denúncia sobre uma loja de importados que está vendendo produtos falsificados."

    f "Entendo. Vamos investigar essa situação. Me diga mais sobre a loja e os produtos que estão sendo vendidos."

    c "A loja se chama 'Cell Importados' e eles estão vendendo celulares e acessórios sem comprovação de origem. Eu tenho algumas evidências que posso fornecer..."

    f "Perfeito. Por favor, envie as evidências para que possamos analisar e tomar as medidas necessárias."

    jump receitaFederal

label receitaFederal:
    #scene do escritorio da Receita Federal
    scene bg_office

    "Hoje é o primeiro dia da Beatriz como estagiária na Receita Federal. Ela está animada para começar a trabalhar e aprender mais sobre o processo de fiscalização."
    
    show a
    with dissolve
    
    a "Bem-vinda à equipe, Breatriz! Estou feliz em tê-la conosco. Como estagiária, você terá a oportunidade de aprender sobre o processo de fiscalização e ajudar a garantir que as leis sejam cumpridas."

    show e happy
    with dissolve

    e "Obrigada! Estou pronta para ajudar no que for necessário."

    show a
    with dissolve

    a "Otimo! a Receita Federal acabou de deflagrar uma operação no Centro de Fortaleza!"

    a "Essa operação visa apreender produtos falsificados e de descaminho, sem comprovação de origem, somando cerca de aproximadamente R$ 2 milhões em produtos irregulares."

    show e
    with dissolve

    e "R$ 2 milhões em produtos à margem dos órgãos reguladores... Isso afeta diretamente a arrecadação e a economia do Ceará, né?"

    show a
    with dissolve

    a "Exatamente. Além da sonegação de tributos federais e do ICMS que destina recursos financeiros a outros setores como saúde e educação,por exemplo. "
    
    a "Esses produtos falsificados e de descaminho geram concorrência desleal contra o lojista honesto e trazem riscos reais segurança do consumidor."

    a "Há bastante evidências que no Centro de Fortaleza é comum encontrar produtos falsificados e de descaminho, e precisamos da sua ajuda para identificar esses produtos e garantir que eles sejam devidamente apreendidos."

    a "Nossa missão de campo hoje é analisar uma das lojas-alvo dessa operação no Centro, a Cell Importados"

    show e
    with dissolve

    e "Nossa, estou muito animada!"

    jump OperacaoCentro

label OperacaoCentro:

    scene bg_street

    "Você chega a um estabelecimento comercial no Centro de Fortaleza acompanhado pela equipe de fiscalização"

    "As prateleiras estão abarrotadas de eletrônicos importados com preços muito abaixo do mercado, mas sem nenhuma nota fiscal de importação ou selo de regularidade."

    scene bg_store2

    l "Olá, posso ajudar"

    l "Espera aí! o que significa isso? Meus produtos vêm de fora, mas todo mundo assim no Centro! Por que essa fiscalização toda em cima de mim?"
    
    
    return
