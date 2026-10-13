


define estagiaria = Character("Beatriz")
define civil = Character("Civil", color="#9a9b9d")
define fiscal = Character("Dep. de Justiça Fiscal", color="#f7e26c")
define analista = Character("Jonas", color="#21cf32")
# Definindo Blackgrand
image bg_street = "img_1"
# The game starts here.

label start:


    scene bg_street

    # Inicio da história

    "Uma ligação é feito no departamento de justiça fiscal na Receita federal"

    civil "Olá, gostaria de fazer uma denúncia sobre uma loja de importados que está vendendo produtos sem licença."

    fiscal "Entendo. Vamos investigar essa situação. Me diga mais sobre a loja e os produtos que estão sendo vendidos."

    civil "A loja se chama 'Cell Importados' e eles estão vendendo celulares e acessórios sem a devida autorização. Eu tenho algumas evidências que posso fornecer..."

    fiscal "Perfeito. Por favor, envie as evidências para que possamos analisar e tomar as medidas necessárias."

    # Agora, a estagiária Beatriz entra em cena
    #scene do escritorio da Receita Federal

    f"Hoje é o primeiro dia de {estagiaria} como estagiária na Receita Federal. Ela está animada para começar a trabalhar e aprender mais sobre o processo de fiscalização."
    
    show estagiaria happy
    
    analista "Bem-vinda à equipe, Beatriz! Como estagiária da Receita Federal, seu primeiro caso envolve a loja 'Cell Importados'."

    estagiaria "Obrigada! Estou pronta para ajudar no que for necessário. O que devo fazer primeiro?"
    
    analista "Otimo! Primeiro, precisamos analisar as evidências fornecidas pelo denunciante. Depois, você precisará visitar a loja para verificar se eles estão realmente vendendo produtos sem licença."

    return
