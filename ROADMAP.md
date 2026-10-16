# ROADMAP — Ordem dos Advogados

**project_code:** `PRJ-000008`  
**status:** `GOVERNANCE_BASELINE_ESTABLISHED`

## Estado comprovado

A infraestrutura mínima de governança foi criada pela
`EA-000000-000019`, usando a Rota B do Gerador. Este arquivo não inventa uma
Estratégia local nem substitui planos substantivos existentes em outros
caminhos do repositório.

## Próximo passo

Reconciliar objetivos, estratégias e fases locais somente a partir de evidência
persistida. Até essa reconciliação, o estado substantivo permanece
`UNKNOWN_NOT_INFERRED`.

## Constituição documental pública — 10/10/2026

**Estratégia:** `EA-000008-000001`, aprovada por `REQ-000008-20261010-001` e conduzida pela Rota B do Gerador `EA-000002-000024`. Esta seção complementa sem apagar a história da EA-000000-000019.

1. **F01:** inventário, identidade e repositório público verificados.
2. **F02:** missão e perfis específicos dos módulos registrados no Gerador.
3. **F03:** README público, missão, protocolo de fontes/publicação, classificação da informação e AGENTS integrados.
4. **F04:** readback, auditoria de conformidade e encerramento documental.

**Gate de conclusão:** `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED`, sem criar site ou afirmar pesquisa substantiva verificada.

**Primeiro candidato de entrega posterior:** Inventariar fontes oficiais das normas estruturantes e dos órgãos da OAB, conferindo competência, versão e vigência. Não iniciar automaticamente; recuperar o mandato local, definir escopo, fonte e critério de verificação e selecionar a estratégia pertinente.

**Restrições:** GitHub público, fonte oficial verificada, representação não oficial, vedação de S2+, dados privados, despesas e implantação web presumida. A verificação de site/Pages permanece `NOT_VERIFIED`.

## EA-000008-000002 — Site próprio e acervo inicial de fontes — 10/10/2026

**Autoridade:** `REQ-000008-20261010-002` · [Plano de Fases](estrategias/EA-000008-000002-site-publico-fontes.md).

- **F01/05:** delimitação de fontes, repositório público e arquitetura Pages — realizada.
- **F02/05:** conteúdo inicial e arquitetura `SITE_ARCHITECTURE.md` — preparada.
- **F03/05:** arquivos `docs/index.md`, `docs/eixos.md`, `docs/fontes.md`, `docs/sobre.md` — salvos em `main`, pendente de auditoria final.
- **F04/05:** habilitar GitHub Pages de `main/docs` — **aguarda configuração pelo proprietário na interface administrativa**.
- **F05/05:** verificar URL pública, conteúdo servido, links e exclusão de dados sensíveis — **NÃO INICIADA**.

**Proveniência:** 5 referências iniciais oficiais identificadas, sem reivindicação de exaustividade ou revisão completa de vigência. **Sem construção de interface customizada nem gasto novo.** O site não deve ser apresentado como publicado antes de evidência de Pages + HTTP.

## EA-000008-000003 — SCIV Essencial Sob Demanda (15/10/2026)

Pedido REQ-000008-20261015-005; mandato global REQ-GLOBAL-20261011-001, F006 ACT009. Plano estrategias/EA-000008-000003-sciv-sob-demanda.md; matriz estrategias/EA-000008-000003-actions.json; preflight auditorias/EA-000008-000003-preflight-sciv-2026-10-15.md; handoff handoffs/codex/EA-000008-000003-SCIV-F002-F004.md. **F001 local criada, registro dual global pendente** neste checkpoint. F002–F004 são CODEX local, F005 HUMAN/CHAT, F006 CHAT. Site EA-000008-000002 permanece principal F004 BLOCKED_ADMIN_CONFIGURATION_REQUIRED por Pages, docs/ não alterado. SCIV ON_DEMAND enabled=false e **não provisionado** nesta F001, B8/C3/instalação nativa/symlink físico não atestados; sem uso operacional, gasto novo ou mensagem automática.

### Checkpoint F001 SCIV — Registro dual verificado (15/10/2026)

F001 SCIV_ADMISSAO_REGISTRADA = PASS_DOCUMENTARY_DUAL_GITHUB_READBACK: criação local 012bac1fcac53f426b04b1a3a82e4c8c5d7a748d; índice global 93f041df9a514c19a03cb612eb11fb9cced5f9e1; relatório auditorias/EA-000008-000003-F001-registro-dual-2026-10-15.md. Próxima F002 ACT-002 CODEX Local no PRJ-000008, sem substituir executor. SCIV enabled=false, Site EA-000008-000002 principal bloqueado por Pages, sem alteração docs/; F002–F006 não executadas, segurança de symlink e C3/B1/B8 não verificados.


## Checkpoint tecnico F002-F004 - 16/10/2026

Provisao ON_DEMAND enabled=false e bloco integral SCIV aplicados; testes finais 275 PASS, 0 FAIL, 0 ERROR e 2 SKIP fisicos de symlink. Gate Rota B/SCIV e matriz atual PASS. Escopo local com limitacao ambiental, publicacao/readback remoto pendentes neste checkpoint. Relatorio: auditorias/EA-000008-000003-codex-f002-f004.md. Site EA-000008-000002 preservada; F005 HUMAN/F006 CHAT e seguranca fisica pendentes. Sem ativacao ou mudanca de Pages.


### Publicacao e readback F002-F004 - 16/10/2026

Commit ede6d885290a76718280f92d09c27c12bb7e847f publicado em main por push normal; 26 arquivos do manifesto relidos remotamente e conferidos por bytes/SHA256/Git blob. CAIXAS_VERSIONADAS e INSTRUCOES_VERSIONADAS PASS; SCIV_REPO_VERIFICADO PASS_WITH_ENV_LIMITATION_REPOSITORY_SCOPE. Recibo: auditorias/EA-000008-000003-publicacao-readback.json. F005 HUMAN e F006 CHAT/contexto real pendentes; G0 deve reconciliar ACT010. Dois SKIPs fisicos nao aprovados, enabled=false, Site/Pages preservados.
