# Define characters

define e = Character("Beatriz") # ESTAGIÁRIA 
define c = Character("Civil", color="#9a9b9d") # CIVIL
define f = Character("Dep. de Justiça Fiscal", color="#f7e26c") # FISCAL
define a = Character("Jonas", color="#21cf32") # ANALISTA
define l = Character("Logista", color="#f7e26c") # LOJA

# Definindo imagens
image bg_call = "scene_1.png"
image bg_office = "scene_2.png"
image bg_office2 = "img_6.png"
image bg_street = "img_4.png"
image bg_store = "img_1.jpg"
image bg_store2 = "img_5.png"
image bg_store3 = "scene_7.png"
image bg_product = "scene_.png"

# Definindo variáveis de investigacao
default provas_apreendidas = 0
default consciencia_publico = 0
default indicios_encontrados = 0
default selo_verificado = False
default rotulo_verificado = False
default nf_verificada = False

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

            e "Entendi! Agora estou pronta para ajudar na fiscalização e garantir que os produtos irregulares sejam devidamente apreendidos."
            
            jump OperacaoCentro

    

label OperacaoCentro:

    scene bg_street

    "Você chega ao Centro de Fortaleza, onde a operação de fiscalização está sendo realizada. A equipe de fiscalização está pronta para começar a inspeção das lojas e identificar produtos irregulares."
    
    "A operação é liderada por um analista da Receita Federal, que explica a importância da conformidade com as leis e regulamentos e orienta a equipe sobre como identificar produtos irregulares."

    scene bg_store

    play music "suspense.mp3" fadein 1.0

    "Você chega a um estabelecimento comercial no Centro de Fortaleza acompanhado pela equipe de fiscalização"

    "As prateleiras estão abarrotadas de eletrônicos importados com preços muito abaixo do mercado, e precisa identificar se há algum produtos com nota fiscal de importação ou selo de regularidade."

    menu:
        "Avançar e Investigar a loja e identificar produtos irregulares":
            jump Investigacao
        "Conversar com o lojista e explicar a importância da conformidade com as leis e regulamentos":
            jump ConversaLojista

label Investigacao:

    scene bg_store

    "Você começa a investigar a loja e identificar produtos irregulares. A equipe de fiscalização está pronta para ajudá-la a analisar os produtos e identificar aqueles que estão em desacordo com as normas e regulamentos."

    # Explicação sobre como identificar produtos irregulares

    "Para identificar produtos irregulares, você deve verificar se eles possuem documentação adequada, como nota fiscal de importação e selo de regularidade."

    "Além disso, você deve verificar se os produtos estão em conformidade com as normas e regulamentos aplicáveis, como requisitos de segurança e qualidade."

    "Sobre produtos falsificados, você deve verificar se eles possuem marcas registradas e se estão em conformidade com as leis de propriedade intelectual."

    "Se você identificar produtos irregulares, deve registrá-los e encaminhá-los para apreensão pela equipe de fiscalização."

    "Sobre descaminho, você deve verificar se os produtos foram introduzidos no país sem o recolhimento dos tributos aduaneiros devidos."

    "Você consegue identificar produtos de descaminho verificando se eles possuem nota fiscal de importação ou declaração de importação."

    "Beatriz começa a analisar os produtos atraves de uma lista de verificação fornecida pela equipe de fiscalização. Ela verifica a documentação dos produtos e identifica aqueles que estão em desacordo com as normas e regulamentos."
    
    jump inspecionarProduto
        
        
# ==============================================================================
# LABEL: INSPEÇÃO TÉCNICA DE FALSIFICAÇÃO E DESCAMINHO
# ==============================================================================
label inspecionarProduto:

    scene bg_store3
    show e at left

    "Você pega uma caixa de carregador turbo e fone sem fio expostos na vitrine por um terço do preço oficial."
    
    a "Beatriz, antes de lavrar o auto, precisamos comprovar tecnicamente se há indícios de falsificação ou descaminho. Examine o item com atenção."

    # Loop de inspeção: o jogador precisa checar pelo menos 2 critérios para concluir
    label menu_inspecao:
        menu:
            "1. Verificar Selo de Homologação (Anatel / Inmetro)" if not selo_verificado:
                $ selo_verificado = True
                $ indicios_encontrados += 1
                e "Olhando a parte traseira... Não há selo da Anatel nem certificação do Inmetro!"
                a "Exato! Produtos eletrônicos sem homologação não passaram por testes de segurança elétrica e oferecem risco de curto-circuito ou explosão ao consumidor."
                jump menu_inspecao

            "2. Analisar Acabamento, Ortografia e Código de Barras" if not rotulo_verificado:
                $ rotulo_verificado = True
                $ indicios_encontrados += 1
                e "A impressão da marca está borrada, o manual tem erros grosseiros de português e o código de barras não bate com o fabricante oficial."
                a "Indício clássico de contrafação (falsificação). Além de enganar o consumidor, isso viola propriedade intelectual e gera concorrência desleal."
                jump menu_inspecao

            "3. Exigir Nota Fiscal de Entrada / Declaração de Importação" if not nf_verificada:
                $ nf_verificada = True
                $ indicios_encontrados += 1
                e "Sr. Lojista, cadê a Nota Fiscal de compra deste lote ou a Declaração de Importação?"
                l "Ah... comprei direto de um fornecedor sem nota mesmo, pra sair mais barato."
                a "Caracterizado o descaminho! Mercadoria estrangeira introduzida no país sem o recolhimento dos tributos aduaneiros devidos."
                jump menu_inspecao

            "Concluir Laudo Pericial" if indicios_encontrados >= 2:
                jump resultado_inspecao

            "Concluir Laudo Pericial (Precisa investigar mais)" if indicios_encontrados < 2:
                a "Calma, Beatriz! Você ainda não coletou indícios técnicos suficientes para sustentar uma apreensão legal. Examine mais detalhes do produto."
                jump menu_inspecao

label resultado_inspecao:

    $ provas_apreendidas += indicios_encontrados
    
    if indicios_encontrados == 3:
        $ consciencia_publico += 2
        e "Laudo completo! Comprovei falta de homologação (risco à saúde), indícios claros de falsificação e ausência de nota de importação (descaminho)."
        a "Perícia impecável, Beatriz! Esse relatório garante a apreensão legal do lote e protege tanto o consumidor quanto a arrecadação pública."
    else:
        $ consciencia_publico += 1
        e "Consegui reunir [indicios_encontrados] indícios técnicos suficientes para comprovar a irregularidade do produto."
        a "Bom trabalho! Sempre que possível, verifique todos os pontos para deixar o auto de infração ainda mais sólido."

    jump analise_tecnica        
        
          
label ConversaLojista:

    scene bg_store2

    show l at left
    with dissolve

    l "Olá, posso ajudar"

    #l "Espera aí! o que significa isso? Meus produtos vêm de fora, mas todo mundo assim no Centro! Por que essa fiscalização toda em cima de mim?"
    
    a "Sr. Lojista, estamos aqui para garantir que todos os produtos vendidos estejam em conformidade com as leis e regulamentos. Produtos sem nota fiscal de importação ou selo de regularidade podem ser falsificados ou de descaminho, o que representa riscos para o consumidor e prejudica a arrecadação pública."

    a "A conformidade com as leis e regulamentos é essencial para garantir a segurança do consumidor e a arrecadação de tributos, que são utilizados em serviços públicos essenciais como saúde e educação."

    a "Além disso, a venda de produtos falsificados ou de descaminho gera concorrência desleal contra lojistas que cumprem a lei, prejudicando o comércio local e a economia como um todo."

    a "Entretanto, viemos analizar os produtos expostos na loja e identificar aqueles que estão em desacordo com as normas e regulamentos. Se encontrarmos produtos irregulares, eles serão apreendidos e você poderá ser responsabilizado legalmente."

    jump inspecionarProduto

label analise_tecnica:

    scene bg_store

    "Após a inspeção técnica, você conclui que os produtos analisados apresentam indícios de irregularidades."

    if indicios_encontrados >= 2:

        scene bg_product

        "Com base nos indícios encontrados, a equipe de fiscalização decide apreender os produtos irregulares e lavrar o auto de infração."
        
        "O lojista é informado sobre a apreensão e as consequências legais de vender produtos falsificados ou de descaminho."

    else:

        "Apesar de alguns indícios encontrados, não há evidências suficientes para justificar a apreensão dos produtos."
        
        "A equipe de fiscalização orienta o lojista sobre a importância da conformidade com as leis e regulamentos e recomenda que ele regularize a situação dos produtos vendidos."

    jump fim_operacao

label fim_operacao:

    scene bg_office

    "Após a operação de fiscalização, você retorna ao escritório da Receita Federal para relatar os resultados da inspeção."

    if indicios_encontrados >= 2:

        "A equipe de fiscalização elogia seu trabalho e destaca a importância da sua contribuição para garantir a conformidade com as leis e regulamentos."

        "O relatório da operação é enviado às autoridades competentes para que sejam tomadas as medidas legais cabíveis contra o lojista."

    else:

        "A equipe de fiscalização agradece sua participação na operação e reforça a importância de continuar monitorando o comércio local para garantir a conformidade com as leis e regulamentos."
    
    return