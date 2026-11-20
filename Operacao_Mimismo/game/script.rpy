
# Define characters
# ESTAGIÁRIA
define e = Character("Beatriz", color="#2b5b84")
# CIVIL
define c = Character("Cívil", color="#10a562")
# DEPARTAMENTO DA RECEITA FEDERAL
define f = Character("Dep. de Justiça Fiscal", color="#130c9e")
# ANALISTA
define a = Character("Jonas", color="#21cf32")
# LOJISTA
define l = Character("Lojista", color="#c21515")

# Definindo imagens e backgrounds
image bg_call = "scene_1.png"
image bg_office = "img_2.png"
image bg_office2 = "img_6.png"
image bg_street = "img_4.png"
image bg_store = "img_1.jpg"
image bg_store2 = "img_5.png"
image bg_store3 = "scene_7.png"
image bg_product = "scene_.png"
image beatriz = "beatriz.png"

# Definindo variáveis de investigacao
default provas_apreendidas = 0
default consciencia_publico = 0
default indicios_encontrados = 0
default selo_verificado = False
default rotulo_verificado = False
default nf_verificada = False
default valor_apreensao_milhoes = 2
default tributos_estimados = 0

# O jogo começa aqui
label start:

    play music "call.mp3" fadein 1.0
    scene bg_call
    with dissolve

    "Uma ligação chega ao plantão de fiscalização e cidadania fiscal da Receita Federal."

    c "Olá, quero fazer uma denúncia sobre uma loja de importados que vende eletrônicos sem procedência e com cara de falsificação."


    f "Entendido. Vamos apurar o caso. Que loja é e o que estão vendendo?"


    c "É a 'Cell Importados'. Vendem celulares e acessórios bem abaixo do preço, sem nota fiscal nem comprovação de origem. Tenho registros que posso mandar."


    f "Ótimo. Envie o que você reuniu para a equipe analisar e direcionar a fiscalização."

    stop music fadeout 1.0

    menu:
        "Receber e registrar as provas iniciais":
            $ provas_apreendidas += 1
            $ consciencia_publico += 1
            f "Provas recebidas e anexadas ao caso. Isso ajuda a direcionar a verificação em campo."
            jump receitaFederal

        "Seguir só com o relato e abrir triagem":
            f "Certo. Sem o material prévio a apuração exige mais atenção em campo, mas vamos registrar a denúncia para triagem."
            jump receitaFederal


label receitaFederal:

    play music "office.mp3" fadein 1.0
    scene bg_office
    with dissolve

    "Primeiro dia da Beatriz como estagiária na Receita Federal, em parceria com as ações de cidadania fiscal."

    a "Bem-vinda à equipe, Beatriz! Aqui você vai ver na prática como a fiscalização protege o consumidor e os recursos públicos."

    show beatriz at right
    with dissolve
    e "Obrigada, Jonas! Tô pronta para acompanhar e aprender."

    a "Chegou uma operação no Centro de Fortaleza: cerca de R$ [valor_apreensao_milhoes] milhões em mercadorias com indícios de falsificação e descaminho."

    show beatriz at right
    with dissolve
    e "R$ [valor_apreensao_milhoes] milhões sem controle... Isso tira dinheiro de imposto que voltaria pra cidade, né?"

    a "Isso mesmo. Quando entram tributos federais e ICMS fora da lei, faltam recursos para saúde, educação e serviços básicos."
    a "Além disso, quem vende produto irregular sem imposto concorre de forma desleal com o lojista correto e pode colocar a segurança de quem compra em risco."
    a "Hoje vamos averiguar a Cell Importados, no Centro."

    show beatriz at right
    with dissolve
    e "Partiu! Quero ver como isso funciona na prática."

    menu:
        "Ir direto para a operação no Centro":
            $ consciencia_publico += 1
            show beatriz at right
            with dissolve
            e "Vamos nessa! Quero acompanhar a inspeção de perto."
            jump OperacaoCentro

        "Pedir um resumo rápido antes de sair":
            a "Resumo rápido: falsificação é copiar marca ou produto ilegalmente, violando direitos e enganando o cliente."
            a "Descaminho é trazer mercadoria estrangeira sem pagar os impostos devidos na entrada. Nos dois casos, há perda fiscal e risco ao consumidor."

            show beatriz at right
            with dissolve
            e "Fechado! Agora ficou bem claro o que observar."
            jump OperacaoCentro


label OperacaoCentro:

    scene bg_street
    with dissolve

    "A equipe chega ao Centro de Fortaleza. O movimento é intenso e o analista Jonas alinha os critérios da vistoria."

    scene bg_store
    with dissolve
    play music "suspense.mp3" fadein 1.0

    "Na Cell Importados, há carregadores, fones e acessórios com preços bem baixos, sem nota visível nem selo de certificação."

    menu:
        "Ir direto inspecionar os produtos":
            jump Investigacao

        "Conversar primeiro com o lojista":
            jump ConversaLojista


label Investigacao:

    scene bg_store3
    with dissolve

    a "Antes de sair recolhendo qualquer coisa, a regra é checar indícios objetivos: nota ou declaração de importação, selos de segurança e qualidade da embalagem."

    show beatriz at right
    with dissolve
    e "Se faltar documento de entrada, pode ser descaminho. Se tiver marca falsa ou falha grave de segurança, também é irregularidade."

    a "Exato. Pegue um item da vitrine e faça a conferência passo a passo."

    hide beatriz
    with dissolve

    jump inspecionarProduto


label ConversaLojista:

    scene bg_store2
    with dissolve
    $ consciencia_publico += 1

    
    l "E aí, tudo certo? Posso ajudar?"

    a "Bom dia. Estamos fazendo uma verificação de regularidade fiscal e de produtos. Mercadoria sem nota de importação ou sem selo pode configurar descaminho ou falsificação."
    a "Isso prejudica quem paga imposto direitinho, reduz verba pública de áreas como saúde e educação e pode trazer risco pra quem usa."

    l "Ah, mas todo mundo vende assim aqui no Centro, o preço fica mais em conta..."

    a "Preço baixo sem origem legal costuma ter um custo escondido pra cidade e pro consumidor. Vamos conferir os itens expostos agora."


    jump inspecionarProduto

label inspecionarProduto:

    scene bg_store3
    with dissolve
    show beatriz at left
    with dissolve

    "Você pega uma caixa de carregador turbo e fone sem fio na vitrine por um terço do preço de loja oficial."

    a "Beatriz, para sustentar qualquer medida, precisamos levantar indícios concretos no item. O que você vai checar?"

    jump menu_inspecao


label menu_inspecao:

    menu:
        "1. Verificar Selo de Homologação (Anatel / Inmetro)" if not selo_verificado:
            $ selo_verificado = True
            $ indicios_encontrados += 1
            show beatriz at left
            with dissolve
            e "Olhando atrás da caixa... Não tem selo da Anatel nem do Inmetro."
            
            a "Sem certificação, o carregador não passou por teste de segurança. Pode superaquecer, dar curto ou estragar o aparelho."
            jump menu_inspecao

        "2. Analisar Acabamento, Ortografia e Código de Barras" if not rotulo_verificado:
            $ rotulo_verificado = True
            $ indicios_encontrados += 1
            show beatriz at left
            with dissolve
            e "A impressão tá borrada, o manual tem vários erros de português e o código de barras não confere."
            
            a "Forte indício de falsificação. Além de enganar quem compra, derruba a concorrência justa com quem trabalha legalizado."
            jump menu_inspecao

        "3. Cobrar Nota Fiscal de Entrada / Declaração de Importação" if not nf_verificada:
            $ nf_verificada = True
            $ indicios_encontrados += 1
            show beatriz at left
            with dissolve
            e "Tem nota fiscal de compra desse lote ou declaração de importação?"
            
            l "Pior que não... peguei direto num fornecedor sem nota pra baratear."
            
            a "Aí entra o descaminho: produto estrangeiro sem comprovação fiscal e sem o recolhimento devido dos tributos."
            jump menu_inspecao

        "Concluir verificação técnica" if indicios_encontrados >= 2:
            jump resultado_inspecao

        "Concluir verificação técnica (Ainda faltam indícios)" if indicios_encontrados < 2:

            a "Ainda tá cedo pra fechar a análise, Beatriz. Checa mais algum ponto da embalagem ou da documentação."
            jump menu_inspecao


label resultado_inspecao:

    $ provas_apreendidas += indicios_encontrados

    if indicios_encontrados == 3:
        $ consciencia_publico += 2
        show beatriz at left
        with dissolve
        e "Fechei os três pontos: sem selo de segurança, sinais de falsificação e sem nota ou declaração de importação."
        
        a "Ótima checagem, Beatriz. Com indícios claros e documentados, a base técnica fica bem mais sólida."
    else:
        $ consciencia_publico += 1
        show beatriz at left
        with dissolve
        e "Reuni [indicios_encontrados] indícios técnicos sobre a irregularidade do produto."
        
        a "Bom avanço. Quanto mais critérios conferidos com precisão, mais consistente fica a análise."

    jump analise_tecnica


label analise_tecnica:

    scene bg_store2
    with dissolve

    "Com os registros da inspeção em mãos, a equipe avalia o enquadramento do material encontrado."

    if indicios_encontrados >= 2:
        scene bg_product
        with dissolve
        "Há indícios consistentes de irregularidade nos itens analisados. A equipe formaliza a apreensão dos produtos irregulares e lavra o procedimento cabível."
        "O lojista é notificado sobre a apreensão e as consequências legais da venda de mercadorias falsificadas ou sem comprovação fiscal."
    else:
        "Os indícios reunidos são limitados para uma medida mais ampla no momento."
        "A equipe orienta o responsável sobre a necessidade de regularizar a procedência, a documentação fiscal e os padrões de conformidade."

    jump fim_operacao


label fim_operacao:

    stop music fadeout 1.0
    scene bg_office
    with dissolve

    $ tributos_estimados = indicios_encontrados * 15000

    "De volta ao escritório, a equipe fecha o relatório da ação no Centro de Fortaleza."

    if indicios_encontrados >= 2:
        
        a "Mandou bem, Beatriz. Consolidamos [indicios_encontrados] indícios técnicos e encaminhamos a apreensão dos itens irregulares."

        show beatriz at right
        with dissolve
        e "Dá pra ver como a falta de nota, a ausência de certificação e o descaminho afetam tanto quem compra quanto os cofres públicos."

        
        a "Exato. Uma estimativa ilustrativa de R$ [tributos_estimados] em impactos tributários e de conformidade mostra por que isso importa: tributos bem arrecadados financiam saúde, educação e serviços essenciais."
        a "E coibir irregularidades protege o comércio regular e evita riscos de acidentes com eletrônicos sem certificação."
    else:
        
        a "Registramos a vistoria, Beatriz, mas ainda faltou aprofundar a checagem técnica para um encaminhamento mais firme."

        show beatriz at right
        with dissolve
        e "Fica a lição de olhar cada detalhe antes de concluir."

        
        a "Com certeza. Cidadania fiscal começa ao cobrar nota, conferir a origem do que se compra e entender o destino dos recursos públicos."

    hide beatriz
    with dissolve

    scene bg_office
    with dissolve

    "--- RESUMO DO CASO: OPERAÇÃO NO CENTRO DE FORTALEZA ---"
    "Indícios técnicos verificados: [indicios_encontrados] de 3"
    "Provas registradas: [provas_apreendidas] | Consciência e engajamento fiscal: [consciencia_publico]"

    "Reflexão: Exigir nota fiscal, checar procedência e combater a irregularidade ajudam a manter a concorrência justa e a financiar os serviços públicos."


    return