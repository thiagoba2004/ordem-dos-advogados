# EA-000008-000002 — Site público próprio e acervo inicial de fontes

**Projeto:** PRJ-000008 — Ordem dos Advogados  
**Autoridade:** REQ-000008-20261010-002, autorização expressa de 10/10/2026  
**Origem:** EA-000008-000001, constituição documental pública encerrada  
**Infraestrutura existente:** GitHub público; metadata `has_pages=false` no início desta EA, sem site implantado.  
**Modelo inicial de entrega:** GitHub Pages usando arquivos Markdown em `main/docs`, sem framework e sem nova despesa autorizada.

## Objetivo

Implantar **site próprio, independente e não oficial**, com Home, campo de estudo, fontes e sobre, ancorado em registros verificáveis; iniciar um acervo mínimo com links e notas de proveniência, sem alegar pesquisa exaustiva ou atualização contínua já implantada.

## Plano de Fases

1. **FASE 01/05 [F-000008-000002-001] — Escopo, fontes e segurança**: confirmar autorização, visibilidade, host, público-alvo e fontes oficiais datadas. **Gate:** `SOURCE_BASELINE_AND_HOST_CONSTRAINTS_VERIFIED`.
2. **FASE 02/05 [F-000008-000002-002] — Arquitetura e conteúdo**: organizar Home, Eixos, Fontes e Sobre; separar informação estável e referências de pesquisa; evitar afirmação não suportada. **Gate:** `PUBLIC_CONTENT_STRUCTURE_REVIEWED`.
3. **FASE 03/05 [F-000008-000002-003] — Site Markdown preparado**: criar `docs/index.md`, `docs/eixos.md`, `docs/fontes.md`, `docs/sobre.md`; validar links, YAML front matter e referências. Ações documentais de GitHub podem ser feitas por Chat; trabalho de software/build multiarquivo customizado pertence ao Codex. **Gate:** `SITE_SOURCE_STAGED_IN_GITHUB`.
4. **FASE 04/05 [F-000008-000002-004] — Ativação do GitHub Pages**: responsável com acesso a Settings → Pages deve configurar **Deploy from a branch**, branch `main`, folder `/docs`, e salvar. Este ato de configuração não é coberto pela escrita documental do conector GitHub desta sessão. **Gate:** `PAGES_PUBLISHING_SOURCE_CONFIRMED`.
5. **FASE 05/05 [F-000008-000002-005] — Verificação pública**: conferir URL HTTP efetiva, navegação, legibilidade, independência institucional, ausência de dados sigilosos, proveniência de links e estado do deployment. Só então `PUBLIC_SITE_VERIFIED` e encerrar estratégia.

## Fontes iniciais selecionadas em 10/10/2026

1. **Lei nº 8.906/1994** — Planalto, Estatuto da Advocacia e da OAB: https://www4.planalto.gov.br/legislacao/portal-legis/legislacao-por-assunto-OLD/acesso-a-justica-e-processo-judicial/direito-processual/lei-no-8-906-de-4-de-julho-de-1994. Texto da lei de referência; conferir redação vigente e decisões de controle de constitucionalidade em cada estudo.
2. **Estatuto e anexos no Conselho Federal** — Portal oficial da OAB: https://www.oab.org.br/leisnormas/estatuto. Acesso institucional a materiais estatutários e complementares; a página não certifica isoladamente cada atualização.
3. **Código de Ética e Disciplina: Resolução nº 02/2015** — Portal oficial da OAB: https://www.oab.org.br/leisnormas/legislacao/resolucoes/02-2015. Ato que aprova o Código de Ética e Disciplina; consultar alterações posteriores.
4. **Resolução OAB nº 005/2024** — Portal oficial da OAB: https://www.oab.org.br/leisnormas/legislacao/resolucoes/005-2024. Exemplo documentado de alteração do Código de Ética e Disciplina.
5. **Legislação, provimentos e resoluções** — Busca normativa oficial OAB: https://www.oab.org.br/leisnormas/legislacao/codigoetica. Ponto de partida para verificação institucional e histórico normativo.

A seleção não afirma completude, uniformidade institucional nem vigência de qualquer dispositivo isolado. Cada pesquisa adicional exige atualização datada, recorte e verificação. Fontes de outros sistemas não são transplantadas como se fossem normativas deste Projeto.

## Proteção e limites

- Repositório e futuro site são superfícies públicas: apenas `S0_PUBLICO` ou conteúdo não sensível revisado. Sem formulários, credenciais, logotipos oficiais, dados sigilosos ou serviços pagos.
- O código/fonte do site permanece no repositório atual; conteúdo público é restrito a `/docs`.
- Não duplicar `AGENTS.md`, logs internos, `PROJECT_STATE.json` ou outras fontes de governança no conteúdo de Pages.
- **Não alegar site no ar antes de provar configuração do Pages, pipeline e URL pública**, e não confundir marcador `has_pages=false` com permissão de ativação.
- Uma expansão para portal com interface customizada, backend, busca inteligente, alertas ou automação deve ser tratada com Codex/Work conforme catálogo de executor, autorização e gate local.
