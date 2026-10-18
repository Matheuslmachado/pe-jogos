


define e = Character("Beatriz") # ESTAGIÁRIA 
define c = Character("Civil", color="#9a9b9d") # CIVIL
define f = Character("Dep. de Justiça Fiscal", color="#f7e26c") # FISCAL
define a = Character("Jonas", color="#21cf32") # ANALISTA
# Definindo Blackgrand
image bg_street = "img_1.jfif"
# The game starts here.

label start:


    scene bg_street

    # Inicio da história

    "Uma ligação é feito no departamento de justiça fiscal na Receita federal"

    c "Olá, gostaria de fazer uma denúncia sobre uma loja de importados que está vendendo produtos falsificados."

    f "Entendo. Vamos investigar essa situação. Me diga mais sobre a loja e os produtos que estão sendo vendidos."

    c "A loja se chama 'Cell Importados' e eles estão vendendo celulares e acessórios sem comprovação de origem. Eu tenho algumas evidências que posso fornecer..."

    f "Perfeito. Por favor, envie as evidências para que possamos analisar e tomar as medidas necessárias."

    # Agora, a estagiária Beatriz entra em cena
    #scene do escritorio da Receita Federal

    "Hoje é o primeiro dia da Beatriz como estagiária na Receita Federal. Ela está animada para começar a trabalhar e aprender mais sobre o processo de fiscalização."
    
    show a
    
    a "Bem-vinda à equipe, Breatriz! Estou feliz em tê-la conosco. Como estagiária, você terá a oportunidade de aprender sobre o processo de fiscalização e ajudar a garantir que as leis sejam cumpridas."

    show e happy

    e "Obrigada! Estou pronta para ajudar no que for necessário."

    show a

    a "Otimo! a Receita Federal acabou de deflagrar uma operação no Centro de Fortaleza!"

    a "Essa operação visa apreender produtos falsificados e de descaminho, sem comprovação de origem, somando cerca de aproximadamente R$ 2 milhões em produtos irregulares."

    show e

    e "R$ 2 milhões em produtos à margem dos órgãos reguladores... Isso afeta diretamente a arrecadação e a economia do Ceará, né?

    show a

    a "Exatamente. Além da sonegação de tributos federais e do ICMS que destina recursos financeiros a outros setores como saúde e educação,por exemplo. Esses produtos falsificados e de descaminho geram concorrência desleal contra o lojista honesto e trazem riscos reais segurança do consumidor."

    a "Há bastante evidências que no Centro de Fortaleza é comum encontrar produtos falsificados e de descaminho, e precisamos da sua ajuda para identificar esses produtos e garantir que eles sejam devidamente apreendidos."

    a "Nossa missão de campo hoje é analisar uma das lojas-alvo dessa operação no Centro, a Cell Importados"

    show e

    e "Nossa, estou muito animada!"



    return
