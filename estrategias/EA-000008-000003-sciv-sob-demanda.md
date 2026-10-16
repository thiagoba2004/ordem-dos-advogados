# EA-000008-000003 — Implantação do SCIV Essencial Sob Demanda
**Projeto:** PRJ-000008 — Ordem dos Advogados (repositório público não oficial). **Mandato:** REQ-GLOBAL-20261011-001 / EA-000000-000034/F006/ACT-000000-000034-009; pedido local REQ-000008-20261015-005. **Data:** 15/10/2026. **Estado:** CREATED_DOCUMENTARY, F001 com registro dual pendente. **Fonte preparatória:** gerador-de-agents/handoffs/sciv/EA-000000-000034/PRJ-000008-plano-local-proposto.md.

## Coexistência, finalidade e limites
EA-000008-000001 foi concluída documentalmente. **EA-000008-000002 continua principal**, no site F004/05 bloqueado por GitHub Pages; preservar main/docs, identidade visual, AGENTS, missão e políticas da OAB. SCIV não altera competência jurídica nem identifica o projeto com a OAB. Opt-in autorizado conforme perfil do Gerador, `mode=ON_DEMAND`, `enabled=false`; não existe ativação ou implantação pela criação deste plano. Os dois ciclos têm destinos principais diferentes e escrita serializada em PROJECT_STATE, ROADMAP e logs. Preflight auditorias/EA-000008-000003-preflight-sciv-2026-10-15.md.

## Fases e responsáveis
1. **F-000008-000003-001 — Admissão e registro dual.** CHAT/G0, GitHub connector, registrar solicitação, CREATED, plano, matriz, estado paralelo e índice global após readback. **Gate SCIV_ADMISSAO_REGISTRADA**, escopo documental.
2. **F-000008-000003-002 — Caixas bilaterais e estado.** CODEX Local no checkout PRJ-000008: provisionar comunicados/SCIV_STATE.json ON_DEMAND enabled=false, operational_ref=main e READMEs em comunicados/governanca-geral/{mensagens,historico} e comunicados/ia-especializada/{mensagens,historico}. Testar segurança e idempotência. **Gate CAIXAS_VERSIONADAS**.
3. **F-000008-000003-003 — Adaptador integral.** CODEX Local PRJ-000008: bloco SCIV gerenciado em adaptadores/chatgpt/INSTRUCOES.md, preservando bytes externos e missão OAB; nenhuma alteração na UI nativa. **Gate INSTRUCOES_VERSIONADAS**.
4. **F-000008-000003-004 — Validações offline e readback.** CODEX Local PRJ-000008: gates Rota B/SCIV do Gerador, matriz de ações, histórico Git completo, regressões de filesystem/symlink/hardlink/junction/reparse, isolamento, fail-closed, interrupção e idempotência. Preservar PASS/FAIL/ERROR/SKIP e recibos. **Gate SCIV_REPO_VERIFICADO**, apenas escopo comprovado.
5. **F-000008-000003-005 — Configuração nativa e recebimento B8 pós-instalação.** HUMAN instala instruções integrais na UI do Projeto ChatGPT somente após decisão/contexto; CHAT/G0 publica Comunicado de recebimento real sob solicitação, IA especializada responde no contexto confirmado. **Gate INSTALACAO_E_TESTE_DE_RECEBIMENTO_CLASSIFICADOS**; B8 e SCIV são provas distintas.
6. **F-000008-000003-006 — Comportamento real e arquivo bilateral.** CHAT/G0 + HUMAN e IA especializada confirmada: ausência de leitura automática, leitura sob demanda, resposta correlacionada, tratamento e arquivamento bilateral, com limites PEP. **Gate SCIV_COMPORTAMENTO_CLASSIFICADO**.

## Matriz e segurança
Sete ações tipadas estão em estrategias/EA-000008-000003-actions.json; F001 CHAT, F002–F004 CODEX, F005 HUMAN e CHAT, F006 CHAT. Sem substituição de executor. Apenas S0/S1 revisado no Git público, proibidos S2+, dados pessoais não públicos, material sigiloso, credenciais e gasto novo. Sem polling, cron, webhooks, Pages, ativação SCIV, instalação nativa, C3/B1/B8 presumidos ou PEP live. **Testes físicos de symlink necessários para liberação operacional; SKIP não equivale a PASS.** F002 só após F001 dual com readback e autorização própria de CODEX. Handoff: handoffs/codex/EA-000008-000003-SCIV-F002-F004.md.

## Checkpoint F001 — registro dual verificado em 15/10/2026

G0 confirmou os commits de registro local `012bac1fcac53f426b04b1a3a82e4c8c5d7a748d` e global `93f041df9a514c19a03cb612eb11fb9cced5f9e1`, com readback de ambas as fontes. `ACT-000008-000003-001=VERIFIED_DOCUMENTARY_DUAL`; gate `SCIV_ADMISSAO_REGISTRADA=PASS` somente documental, sem operação SCIV. Recibo: `auditorias/EA-000008-000003-F001-registro-dual-2026-10-15.md`. F002 passa a próximo executor CODEX Local PRJ-000008; F003/F004 CODEX pendentes, F005 HUMAN e F006 CHAT/contexto pendentes. Site EA-000008-000002 permanece principal e bloqueado por Pages; SCIV desabilitado.


## Checkpoint tecnico F002-F004 - 16/10/2026

Provisao ON_DEMAND enabled=false e bloco integral SCIV aplicados; testes finais 275 PASS, 0 FAIL, 0 ERROR e 2 SKIP fisicos de symlink. Gate Rota B/SCIV e matriz atual PASS. Escopo local com limitacao ambiental, publicacao/readback remoto pendentes neste checkpoint. Relatorio: auditorias/EA-000008-000003-codex-f002-f004.md. Site EA-000008-000002 preservada; F005 HUMAN/F006 CHAT e seguranca fisica pendentes. Sem ativacao ou mudanca de Pages.
