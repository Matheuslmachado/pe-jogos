# 🎮 Operação Fiscal: O Mistério da Nota (Caso 1: Operação Mimetismo - O Desafio do Centro)

> **Projeto de Extensão Universitária**  
> **Disciplina:** Tecnologia e Desenvolvimento de Jogos Digitais (Semestre 2026.2)  
> **Articulação Extensionista:** NAF Unichristus & Receita Federal do Brasil  
> **Público-Alvo Prioritário:** Estudantes do Ensino Médio (14 a 18 anos)  
> **Equipe de Desenvolvimento:** Matheus — *Investigação Nota Limpa*  

---

## 📌 Sumário
- [1. Visão Geral e Propósito](#1-visão-geral-e-propósito)
- [2. Contexto do Caso Real (Operação Mimetismo)](#2-contexto-do-caso-real-operação-mimetismo)
- [3. Ficha Técnica do Jogo](#3-ficha-técnica-do-jogo)
- [4. Problema Educativo e Objetivos de Aprendizagem](#4-problema-educativo-e-objetivos-de-aprendizagem)
- [5. Core Gameplay e Mecânicas Principais](#5-core-gameplay-e-mecânicas-principais)
- [6. Estrutura Técnica e Arquitetura do Código (Ren'Py / Python)](#6-estrutura-técnica-e-arquitetura-do-código-renpy--python)
- [7. Ficha de Aplicação Extensionista (Atividade NAF)](#7-ficha-de-aplicação-extensionista-atividade-naf)
- [8. Guia de Instalação e Execução](#8-guia-de-instalação-e-execução)
- [9. Histórico de Versões e Transparência no Uso de IA](#9-histórico-de-versões-e-transparência-no-uso-de-ia)

---

## 1. Visão Geral e Propósito

**"Operação Fiscal: O Mistério da Nota"** é um protótipo de jogo digital no formato de **Narrativa Interativa / Visual Novel de Investigação**, desenvolvido com a engine **Ren'Py (baseada em Python)**.

O projeto tem como propósito transformar conceitos fundamentais de **Educação Fiscal e Cidadania** em uma experiência lúdica, interativa e alinhada ao cotidiano do público jovem. O jogador vivencia o papel de uma estagiária do Núcleo de Apoio Contábil e Fiscal (NAF), atuando junto à Receita Federal na fiscalização e conscientização sobre **sonegação fiscal, descaminho, pirataria e a Função Social dos Tributos**.

---

## 2. Contexto do Caso Real (Operação Mimetismo)

O primeiro caso jogável do protótipo é inspirado na operação real deflagrada pela Receita Federal em **Fortaleza (Ceará)**, na qual cerca de **R$ 2 milhões em produtos irregulares** foram apreendidos em estabelecimentos comerciais no Centro da cidade.

### Tópicos Abordados no Jogo:
* **Sonegação e Omissão de Nota Fiscal:** Ausência de recolhimento de ICMS e tributos federais.
* **Descaminho e Pirataria:** Comercialização de produtos estrangeiros sem comprovação de importação regular.
* **Concorrência Desleal:** Como o comércio irregular prejudica o empresário formalizado que paga impostos e gera empregos formais.
* **Saúde e Segurança do Consumidor:** Riscos de eletrônicos e mercadorias sem certificação dos órgãos reguladores.
* **Destino Social dos Recursos:** Demonstração prática de como a arrecadação financia leitos de UBS, escolas públicas e infraestrutura no Estado.

---

## 3. Ficha Técnica do Jogo

| Parâmetro | Detalhe Técnico |
| :--- | :--- |
| **Gênero** | Narrativa Interativa / Visual Novel de Investigação |
| **Engine / Framework** | Ren'Py 8.x (Scripts em Python / `.rpy`) |
| **Linguagem Base** | Python / Script Ren'Py |
| **Plataformas de Saída** | Desktop (Windows, macOS, Linux) e Web (HTML5/WebAssembly) |
| **Estilo Gráfico** | 2D Ilustrado (Cenários e Sprites de Personagens) |
| **Escopo do Protótipo (NP2)** | Ciclo completo de 1 Caso Jogável (Briefing, Investigação, Decisão e Consequências) |

---

## 4. Problema Educativo e Objetivos de Aprendizagem

### 🔍 O Problema:
Jovens do Ensino Médio costumam enxergar impostos como fardo burocrático e muitas vezes acham vantajoso aceitar descontos oferecidos por lojas que não emitem nota fiscal. Faltam ferramentas visuais que conectem essa atitude individual às consequências coletivas (falta de verba para saúde e educação).

### 🎯 Objetivos de Aprendizagem:
1. Compreender que a **Nota Fiscal** é o instrumento que garante o retorno social dos tributos.
2. Identificar os prejuízos do **descaminho e da pirataria** para a economia local e empregos formais.
3. Exercer a **Cidadania Fiscal ativa**, exigindo comprovantes fiscais no consumo diário.

---

## 5. Core Gameplay e Mecânicas Principais

O jogo utiliza um **Core Loop de Investigação e Tomada de Decisão**:

```text
[ Briefing no NAF ] ➔ [ Inspecionar Loja no Centro ] ➔ [ Interrogar Lojista ]
                                                               │
                                                               ▼
[ Resultado & Consequências ] ◄─── [ Confrontar Dados & Provas ]
```

### Indicadores e Variáveis de Controle:
* `provas_apreendidas`: Registra a quantidade de evidências documentais de sonegação ou irregularidade encontradas.
* `consciencia_publico`: Mede a capacidade pedagógica e ética da estagiária nas abordagens.
* `valor_apreensao_milhoes`: Representa o montante econômico irregular interceptado na operação.

---

## 6. Estrutura Técnica e Arquitetura do Código (Ren'Py / Python)

O código-fonte está estruturado no diretório `/game` com suporte a variáveis globais de estado e desvios condicionais por `menu`.

### Exemplo da Estrutura Principal (`game/script.rpy`):

```renpy
# Declaração dos Personagens
define e = Character("Sofia (Estagiária)", color="#2b5b84")
define l = Character("Lojista Investigado", color="#8b4513")
define m = Character("Mentora NAF / Auditora", color="#1c7430")

# Variáveis de Controle
default provas_apreendidas = 0
default consciencia_publico = 0
default valor_apreensao_milhoes = 2

label start:
    scene bg_office
    "Outubro de 2026 - Núcleo de Apoio Contábil e Fiscal (NAF) / Unichristus."
    m "Sofia, a Receita Federal deflagrou a 'Operação Mimetismo' no Centro de Fortaleza!"
    m "Cerca de R$ [valor_apreensao_milhoes] milhões em produtos sem nota e sem origem foram apreendidos."
    
    jump operacao_centro

label operacao_centro:
    scene bg_store
    "Você investiga um dos estabelecimentos no Centro de Fortaleza."
    l "Por que essa fiscalização toda na minha loja?"

    menu:
        "Explicar sobre Concorrência Desleal e Arrecadação Social":
            $ consciencia_publico += 1
            $ provas_apreendidas += 1
            e "O descaminho e a omissão fiscal tiram recursos de hospitais e prejudicam quem vende na legalidade."
            jump final_sucesso_operacao

        "Focar apenas em aplicar uma multa rápida sem orientar":
            jump final_falha_operacao
```

---

## 7. Ficha de Aplicação Extensionista (Atividade NAF)

Ficha técnica para orientação de mediadores do NAF da Unichristus durante oficinas e palestras nas escolas de Ensino Médio:

* **Público Esperado:** Estudantes do 1º ao 3º ano do Ensino Médio (14 a 18 anos).
* **Duração Recomendada:** 45 minutos (15 min de gameplay interativo + 30 min de roda de conversa).
* **Infraestrutura Necessária:** Computador/Notebook com projetor (Datashow) ou Laboratório de Informática. **Não exige conexão com a internet após o download.**
* **Modo de Aplicação:** O mediador do NAF pode projetar o jogo e permitir que a turma vote nas opções dos menus de escolha, promovendo debate em tempo real.

### ❓ Questões para Debate Pós-Jogo:
1. *"Quando compramos um eletrônico barato sem nota no Centro, quem realmente ganha e quem perde no final?"*
2. *"Como a apreensão de R$ 2 milhões em mercadorias irregulares impacta a vida de quem precisa de posto de saúde e escola pública em Fortaleza?"*
3. *"O que podemos fazer no nosso dia a dia para combater a concorrência desleal e ajudar a cidade?"*

---

## 8. Guia de Instalação e Execução

### Para Jogadores / Mediadores:
1. Faça o download da versão compilada na aba [Releases](../../releases).
2. Extraia o arquivo ZIP.
3. Execute o arquivo `Operacao_Nota_Limpa.exe` (Windows) ou o executável correspondente ao seu sistema operacional.

### Para Desenvolvedores (Editar o Projeto):
1. Faça o download do [Ren'Py SDK 8.x](https://www.renpy.org/).
2. Clone este repositório para a sua máquina:
   ```bash
   git clone https://github.com/seu-usuario/matheus-educajogo-fiscal.git
   ```
3. Abra o Launcher do Ren'Py e selecione a pasta do projeto para testar ou compilar (`Build Distributions`).

---

## 9. Histórico de Versões e Transparência no Uso de IA

* **v1.0.0 (NP2 Final):**
  * Implementação completa do Caso 1 (Operação Mimetismo - Centro de Fortaleza).
  * Interface visual ajustada com fundos e sprites de personagens.
  * Integração das variáveis de estado (`provas_apreendidas`, `consciencia_publico`).
  * Inclusão do GDD e Ficha Extensionista no repositório.

### Uso de Inteligência Artificial Generativa (Conforme Item 10 do Edital):
* **Ideação e Codificação:** Apoio na estruturação da sintaxe de scripts Ren'Py e verificação de lógica condicional.
* **Geração de Imagens/Assets:** Criação e adaptação de planos de fundo conceituais e avatares de personagens para o protótipo.
* **Revisão Pedagógica:** Validação da adequação da linguagem técnica contábil/fiscal para o público do Ensino Médio.

---

> **EducaJogo Fiscal 2026.2** — *Promovendo a cidadania e a educação fiscal de forma lúdica.*