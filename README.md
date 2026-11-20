# 🎮 Operação Fiscal: O Mistério da Nota 

> **Projeto de Extensão**  
> **Disciplina:** Tecnologia e Desenvolvimento de Jogos Digitais (Semestre 2026.2)   
> **Público-Alvo:** Adolecentes e Jovens (14 a 18 anos)  
> **Equipe:** Matheus 

---

## 📌 Sumário

* [1. Visão Geral e Contexto Real](#1-visão-geral-e-contexto-real)
* [2. Ficha Técnica do Protótipo](#2-ficha-técnica-do-protótipo)
* [3. Problema Educativo e Objetivos Pedagógicos](#3-problema-educativo-e-objetivos-pedagógicos)
* [4. Core Gameplay e Mecânicas de Perícia](#4-core-gameplay-e-mecânicas-de-perícia)
* [5. Arquitetura do Código e Variáveis de Progresso (Ren'Py)](#5-arquitetura-do-código-e-variáveis-de-progresso-renpy)
* [6. Ficha de Aplicação Extensionista (Atividade NAF)](#6-ficha-de-aplicação-extensionista-atividade-naf)
* [7. Guia de Instalação e Execução](#7-guia-de-instalação-e-execução)
* [8. Transparência e Uso de IA Generativa](#8-transparência-e-uso-de-ia-generativa)

---

## 1. Visão Geral e Contexto Real

**"Operação Fiscal: O Mistério da Nota"** é um protótipo de um jogo pedagógico de investigação narrativa desenvolvido para engajar adolecentes e jovens no debate sobre cidadania fiscal, combate ao descaminho e a função social dos tributos.

### 🔎 Contexto Real: Operação Mimetismo (Fortaleza/CE)
O caso jogável é inspirado na operação ostensiva deflagrada pela Receita Federal no **Centro de Fortaleza**, na qual cerca de **R$ 2 milhões em mercadorias irregulares** (eletrônicos sem nota fiscal, artigos contrafeitos e sem certificação) foram apreendidos.

No jogo, o jogador assume o papel de **Beatriz**, estagiária do Núcleo de Apoio Contábil e Fiscal (NAF), atuando ao lado do analista da Receita Federal **Jonas** na fiscalização da loja **Cell Importados**, abordando:
* **Sonegação e Omissão de Nota Fiscal:** Ausência de recolhimento de ICMS e tributos federais.
* **Descaminho e Contrafação (Falsificação):** Comercialização de produtos estrangeiros sem comprovação de importação regular ou violando propriedade intelectual.
* **Concorrência Desleal:** Como o comércio irregular prejudica o empresário formalizado que atua dentro da lei.
* **Segurança e Saúde do Consumidor:** Riscos físicos de eletrônicos sem homologação dos órgãos reguladores (Anatel/Inmetro).

---

## 2. Ficha Técnica do Protótipo

| Parâmetro | Especificação Técnica |
| :--- | :--- |
| **Gênero** | Narrativa Interativa / Visual Novel de Investigação |
| **Engine & Linguagem** | Ren'Py 8.x (Python Framework / `.rpy`) |
| **Plataformas Target** | Desktop (Windows, macOS, Linux) e Web (HTML5/WASM) |
| **Duração Média** | 15 a 20 minutos por sessão jogável |
| **Escopo da Entrega** | 1 Caso Completo (Denúncia, Briefing, Investigação, Perícia e Desfecho) |
| **Identidade Visual** | Sprites 2D e cenários urbanos do Centro de Fortaleza |

---

## 3. Problema Educativo e Objetivos Pedagógicos

### 🔍 O Problema Educacional
Adolecentes e jovens frequentemente percebem tributos como encargos burocráticos sem retorno visível. O consumo informal ou sem nota fiscal é naturalizado pela falta de percepção sobre os impactos diretos aos recursos que são destinados as áreas da saúde, educação, segurança e serviços públicos da cidade.

### 🎯 Objetivos Pedagógicos
1. Conectar a emissão da **Nota Fiscal** ao financiamento de serviços públicos essenciais (saúde, educação e infraestrutura).
2. Explicar os riscos econômicos e físicos do **descaminho**, da **falsificação** e da **concorrência desleal**.
3. Estimular atitudes de **cidadania fiscal ativa** no cotidiano de consumo dos jovens.

---

## 4. Core Gameplay e Mecânicas de Perícia

A dinâmica alterna entre escuta ativa, diálogo com o comerciante e perícia técnica de produtos:

```text
[1. Denúncia & Triagem] ➔ [2. Briefing no Escritório] ➔ [3. Abordagem na Cell Importados]
                                                                        │
                                                                        ▼
[5. Desfecho & Resumo Fiscal] ◄────────── [4. Perícia Técnica (3 Critérios)]
```

### 🔍 Mecânica de Inspeção Técnica (`menu_inspecao`)
Antes de lavrar o auto de infração, **Beatriz** precisa examinar os eletrônicos da loja em um loop não-linear, devendo comprovar **pelo menos 2 de 3 indícios técnicos** para sustentar a apreensão legal:
1. **Selo de Homologação (Anatel / Inmetro):** Verifica certificação e riscos elétricos/segurança ao consumidor.
2. **Acabamento, Ortografia e Código de Barras:** Identifica sinais de contrafação (falsificação) e violação de propriedade intelectual.
3. **Nota Fiscal de Entrada / Declaração de Importação:** Comprova a ocorrência de descaminho pela ausência de lastro aduaneiro e tributário.

---

## 5. Arquitetura do Código e Variáveis de Progresso (Ren'Py)

O roteiro está estruturado em `game/script.rpy` com controle de estados e desfechos condicionais baseados nas decisões do jogador.

### 📊 Variáveis de Estado e Métricas

| Variável | Tipo | Impacto no Gameplay e Desfecho |
| :--- | :--- | :--- |
| `indicios_encontrados` | `Integer` | Controla a trava da perícia (mínimo 2 indícios) e define entre apreensão formal ou apenas orientação. |
| `provas_apreendidas` | `Integer` | Acumula provas da denúncia inicial e da vistoria física para o relatório final. |
| `consciencia_publico` | `Integer` | Pontua escolhas educativas (recebimento de provas, diálogo com o lojista e perícia completa de 3/3 itens). |
| `tributos_estimados` | `Integer` | Calcula o impacto tributário ilustrativo (`indicios_encontrados * 15000`) exibido no encerramento. |


## 6. Ficha de Aplicação Extensionista (Atividade NAF)

Guia de orientação para estudantes de Ciências Contábeis e Direito do **NAF Unichristus** na condução de oficinas em escolas de Ensino Médio:

* **Público Esperado:** Turmas de 1º a 3º ano do Ensino Médio (30 a 45 alunos por sessão).
* **Duração Total:** 45 minutos (15 min de partida interativa + 30 min de debate mediado).
* **Recursos Necessários:** Notebook com o jogo instalado e Datashow/Projetor (**funcionamento 100% offline**).
* **Dinâmica de Grupo:** Votação coletiva dos alunos em sala de aula para decidir cada escolha da personagem **Beatriz**.

### 💬 Roteiro de Debates Pós-Jogo (Perguntas Desencadeadoras)
1. *"Quando compramos um produto barato e sem nota fiscal no Centro, quem é beneficiado e quem sai prejudicado no final?"*
2. *"Como a apreensão de R$ 2 milhões em mercadorias ilegais na Operação Mimetismo afeta os postos de saúde e escolas de Fortaleza?"*
3. *"Qual é o nosso papel como consumidores para evitar a concorrência desleal na nossa cidade?"*

---

## 7. Guia de Instalação e Execução

### Jogadores:
1. Baixe a versão compilada na aba **Releases** deste repositório.
2. Extraia o conteúdo do arquivo `.zip`.
3. Execute o arquivo `Operacao_Memitismo.exe` (Windows) ou o executável correspondente ao seu sistema operacional.

### Para Desenvolvedores (Editar no Ren'Py):
1. Instale o [Ren'Py SDK 8.x](https://www.renpy.org/).
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/operacao-fiscal-misterio-da-nota.git
   ```
3. Abra o **Ren'Py Launcher**, selecione a pasta do projeto e clique em **Launch Project**.

---

## 8. Transparência e Uso de IA Generativa

Em atendimento aos critérios do edital do projeto de extensão (Item 10):
* **Auxílio no Código:** Estruturação da sintaxe de desvios condicionais, loops de inspeção (`menu_inspecao`) e variáveis globais em Ren'Py/Python.
* **Ideação e Codificação:** Apoio na organização do escopo e alinhamento do tema às diretrizes extensionistas do NAF e da Receita Federal.
* **Validação Pedagógica:** Adaptação da linguagem técnica contábil e aduaneira (*descaminho*, *contrafação*, *ICMS* e *homologação Anatel/Inmetro*) para o público do Ensino Médio.

