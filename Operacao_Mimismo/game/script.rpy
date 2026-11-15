
define e = Character("Beatriz") # ESTAGIÁRIA 
define c = Character("Civil", color="#9a9b9d") # CIVIL
define f = Character("Dep. de Justiça Fiscal", color="#f7e26c") # FISCAL
define a = Character("Jonas", color="#21cf32") # ANALISTA
define l = Character("Logista", color="#f7e26c") # LOJA

# Definindo Blackgrand
image bg_call = "scene_1.png"
image bg_office = "scene_.png"
image bg_street = "img_4.png"
image bg_store = "img_1.jpg"
image bg_store2 = "img_5.png"
# The game starts here.

label start:

    play music "call.mp3" fadein 1.0

    $ valor_apreensao_milhoes = 2 


    scene bg_call

    # Inicio da história

    "Uma ligação é feito no departamento de justiça fiscal na Receita federal"

    show c at left
    with dissolve

    c "Olá, gostaria de fazer uma denúncia sobre uma loja de importados que está vendendo produtos falsificados."
    
    show f at right
    with dissolve

    f "Entendo. Vamos investigar essa situação. Me diga mais sobre a loja e os produtos que estão sendo vendidos."

    show c at left
    with dissolve

    c "A loja se chama 'Cell Importados' e eles estão vendendo celulares e acessórios sem comprovação de origem. Eu tenho algumas evidências que posso fornecer..."

    show f at right
    with dissolve

    f "Perfeito. Por favor, envie as evidências para que possamos analisar e tomar as medidas necessárias."

    stop music fadeout 1.0

    menu:
        "Receber as evidências":
            f "Obrigado por enviar as evidências. Vamos analisá-las e tomar as medidas necessárias para garantir que a loja esteja em conformidade com as leis e regulamentos."
            jump receitaFederal
        "Não receber as evidências":
            f "Entendo. Sem as evidências, será mais difícil para nós investigarmos a situação. No entanto, ainda podemos tomar medidas com base nas informações fornecidas."
            jump start
label receitaFederal:

    play music "office.mp3" fadein 1.0
    #scene do escritorio da Receita Federal
    scene bg_office

    "Hoje é o primeiro dia da Beatriz como estagiária na Receita Federal. Ela está animada para começar a trabalhar e aprender mais sobre o processo de fiscalização."
    
    # hide <image> with dissolve
    show a at left
    with dissolve
    
    a "Bem-vinda à equipe, Breatriz! Estou feliz em tê-la conosco. Como estagiária, você terá a oportunidade de aprender sobre o processo de fiscalização e ajudar a garantir que as leis sejam cumpridas."

    # hide <image> with dissolve
    show e at right
    with dissolve

    e "Obrigada! Estou pronta para ajudar no que for necessário."

    # hide <image> with dissolve
    show a at left
    with dissolve

    a "Otimo! a Receita Federal acabou de deflagrar uma operação no Centro de Fortaleza!"

    a "Essa operação visa apreender produtos falsificados e de descaminho, sem comprovação de origem, somando cerca de aproximadamente R$ [valor_apreensao_milhoes] milhões em produtos irregulares."

    # hide <image> with dissolve
    show e at right
    with dissolve

    e "R$ [valor_apreensao_milhoes] milhões em produtos à margem dos órgãos reguladores... Isso afeta diretamente a arrecadação e a economia do Ceará, né?"

    # hide <image> with dissolve
    show a at left
    with dissolve

    a "Exatamente. Além da sonegação de tributos federais e do ICMS que destina recursos financeiros a outros setores como saúde e educação,por exemplo. "
    
    a "Esses produtos falsificados e de descaminho geram concorrência desleal contra o lojista honesto e trazem riscos reais segurança do consumidor."

    a "Há bastante evidências que no Centro de Fortaleza é comum encontrar produtos falsificados e de descaminho, e precisamos da sua ajuda para identificar esses produtos e garantir que eles sejam devidamente apreendidos."

    a "Nossa missão de campo hoje é analisar uma das lojas-alvo dessa operação no Centro, a Cell Importados"

    # hide <image> with dissolve
    show e at right
    with dissolve

    e "Nossa, estou muito animada!"

    menu:
        "Aceitar a missão e começar a agir!":

            show e at right
            with dissolve

            e "Estou pronta para ajudar na fiscalização e garantir que os produtos irregulares sejam devidamente apreendidos."
            jump OperacaoCentro
        "Entender mais sobre as irregularidades antes de agir":

            show a at left
            with dissolve

            a "Claro! A missão de campo é uma oportunidade para você aprender mais sobre o processo de fiscalização e ajudar a garantir que as leis sejam cumpridas. Você terá a chance de analisar os produtos vendidos na loja e identificar aqueles que estão em desacordo com as normas e regulamentos."

            a "Além disso, você também terá a oportunidade de interagir com os lojistas e explicar a importância da conformidade com as leis e regulamentos. É uma experiência valiosa que irá ajudá-la a desenvolver suas habilidades profissionais e contribuir para o bem-estar da sociedade."

            show e at right
            with dissolve

            e "Entendi! Estou pronta para ajudar na fiscalização e garantir que os produtos irregulares sejam devidamente apreendidos."
            jump OperacaoCentro

    

label OperacaoCentro:

    scene bg_street

    play music "suspense.mp3" fadein 1.0

    "Você chega a um estabelecimento comercial no Centro de Fortaleza acompanhado pela equipe de fiscalização"

    "As prateleiras estão abarrotadas de eletrônicos importados com preços muito abaixo do mercado, mas sem nenhuma nota fiscal de importação ou selo de regularidade."

    scene bg_store2

    show l at left
    with dissolve

    l "Olá, posso ajudar"

    l "Espera aí! o que significa isso? Meus produtos vêm de fora, mas todo mundo assim no Centro! Por que essa fiscalização toda em cima de mim?"
    
    
    return
