可以。我重新看了当前 **v3.0.0** 的仓库后，我认为这次方案不应该只是“增加一个 Digital Prototype mode”，而应该把整个 Skill 的 Prototype 层重新抽象成：

> **Simulation → Digital Prototype → Physical Prototype 的 Fidelity Ladder**

因为你现在的 v3 已经具备了很好的基础：Core Objects 已经明确为 State / Claim / Experiment / Artifact；Symptom Routing 已经采用 evidence discriminator；Evaluation 已经有 structural validator + manual behavior evaluation；而现有 Prototype pipeline 已经可以把 Components Sheet → CSV/JSON → nanDECK → PnP。

尤其需要注意，目前仓库仍明确以 **paper PnP 为默认 prototype medium**，digital 只是 optional；而 Component Schema 虽然已经存在，真正的 schema validator 仍是 future work。([GitHub][1])

基于这些现状，我建议不要把 v4 做成“增加几个工具”，而是做成一次 **Prototype Architecture 2.0**。

下面这份可以直接作为给开发者的 Solution Design。

# Board Game Design Skill

## v4 Digital-First Prototyping & Automated Validation

**Status:** Partially implemented (skill v4.0.0 Markdown slice); full runtime stack still Proposed
**Target:** v4.x
**Based on:** v3.0.0
**Primary goal:** 将 Skill 从 evidence-driven tabletop design framework 升级为 evidence-driven tabletop design + simulation + digital prototyping + physical prototyping system。

**Shipped in skill v4.0.0:** Fidelity Ladder, Simulate mode, evidence types, BG015–BG020, `simulation-run` artifacts, `validate_components.py`. Runtime engines remain optional — see `prototype/runtime.md`.

---

# 1. Executive Summary

当前 v3.0 已经建立了较完整的：

* Design State
* Core Objects
* Genre Profiles
* Symptom Routing
* Diagnostics
* Hypothesis / Experiment
* Confidence Model
* Balance Model
* Structural Validation
* PnP Export Pipeline

但 Prototype 层仍然采用：

```text
Mechanism
↓
Paper PnP
↓
Playtest
↓
Optional Digital
```

这不再是 AI-native design workflow 的最佳默认路径。

随着 LLM、代码生成、脚本化模拟、浏览器 UI、TTS/nanDECK 和自动化测试的发展，早期设计可以采用：

```text
Design Intent
↓
Formalized Game Model
↓
Simulation
↓
Digital Prototype
↓
Human Digital Playtest
↓
Physical Prototype
↓
Physical Playtest
```

核心原则：

> **Use the cheapest prototype fidelity that can answer the current hypothesis.**

因此 v4 不应该简单增加一个 `Digital Prototype` Mode，而应该引入：

## Prototype Fidelity Ladder

```text
P0 — Concept / Model
P1 — Simulation
P2 — Interactive Digital Prototype
P3 — Networked / Tabletop Digital Prototype
P4 — Physical PnP Prototype
P5 — Production Prototype
```

不同 Fidelity Level 服务不同类型的问题。

---

# 2. Design Goals

## 2.1 Primary Goals

### G1 — Digital-first early validation

允许 Agent 在实体原型之前验证：

* game loop
* rules consistency
* economy
* probability
* balance
* dominant strategies
* first-player advantage
* game length
* card usage
* resource flow
* decision space

### G2 — Automated simulation

支持 AI / deterministic agents / heuristic bots / Monte Carlo / scripted agents 自动运行大量对局。

### G3 — Human digital playtesting

支持通过数字 UI / TTS / Web prototype 进行真人测试。

### G4 — Instrumentation

数字游戏必须能够记录结构化 telemetry：

* actions
* turns
* rounds
* decisions
* timing
* resource changes
* scores
* card usage
* player interaction
* win condition
* game duration

### G5 — Evidence integration

Simulation 和 Digital Playtest 产生的结果必须能够进入：

```text
Evidence
↓
Claim
↓
Confidence
↓
Diagnosis
↓
Experiment
↓
Design State
```

### G6 — Physical validation remains mandatory when appropriate

Digital validation 不得被解释为 Physical validation 的替代品。

---

# 3. Non-Goals

v4 不应该试图：

* 自动生成最终商业级游戏
* 自动决定“游戏是否好玩”
* 用 simulation 取代 human playtest
* 用 digital prototype 取代 physical prototype
* 建立通用 AAA game engine
* 强制所有项目使用数字原型
* 强制所有机制都进行 Monte Carlo simulation

原则：

> **Automation validates systems; humans validate experiences.**

---

# 4. Core Architectural Change

## 4.1 Current architecture

```text
Intent
↓
Model
↓
Hypothesis
↓
Mechanism
↓
Prototype
↓
Experiment
↓
Evidence
↓
Diagnosis
↓
Decision
↓
Design State
```

保持不变。

但是 Prototype 节点升级为：

```text
                         ┌──────────────┐
                         │   Prototype  │
                         └──────┬───────┘
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
       Simulation          Digital Human       Physical
           P1                  P2/P3              P4
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ↓
                             Evidence
```

---

# 5. Prototype Fidelity Ladder

## P0 — Formal Game Model

目标：

> 把设计思想转换成可以被机器理解的结构。

至少定义：

```yaml
players:
  min:
  max:

turn_structure:
round_structure:

actions:

resources:

cards:

resolution:

victory:

end_condition:

randomness:

information:

interaction:
```

P0 不要求 UI。

---

## P1 — Simulation Prototype

目标：

> 验证游戏系统是否成立。

适合：

* balance
* probability
* economy
* dominant strategy
* first-player advantage
* game length
* resource flow
* score distribution
* card utilization
* runaway leader

支持：

```text
Deterministic Simulation
Monte Carlo
Heuristic Bots
Random Bots
Scripted Bots
Rule-based Agents
```

输出：

```text
simulation-run
simulation-summary
metrics
anomalies
hypothesis-result
```

---

## P2 — Interactive Digital Prototype

目标：

> 验证真人是否理解并能够操作核心 loop。

重点：

* rules clarity
* UI clarity
* action discoverability
* pacing
* agency
* information visibility
* decision flow

不要求最终视觉设计。

推荐：

```text
HTML/CSS/JS
React
minimal local web app
```

优先：

> Functional UI > visual polish.

---

## P3 — Digital Tabletop Prototype

目标：

> 验证多人互动和桌游 dynamics。

适合：

* negotiation
* hidden information
* social deduction
* simultaneous action
* direct interaction
* table politics
* cooperation
* kingmaking
* communication

工具可以包括：

* TTS
* WebRTC / browser multiplayer
* Tabletopia
* custom lightweight multiplayer prototype

---

## P4 — Physical PnP Prototype

目标：

> 验证真实桌面体验。

验证：

* component ergonomics
* table footprint
* manipulation cost
* readability
* physical affordance
* setup
* teardown
* physical randomness
* social interaction
* downtime
* visual hierarchy

---

## P5 — Production Prototype

目标：

> 接近最终产品。

验证：

* component quality
* manufacturing constraints
* production cost
* graphic hierarchy
* packaging
* insert
* component count

---

# 6. Prototype Selection Algorithm

Agent 不应该默认选择 P4。

应该根据 Hypothesis 自动选择最低成本的有效 Fidelity。

定义：

```text
Prototype Cost
+
Required Evidence
+
Question Type
+
Physical Dependency
```

---

## 6.1 Hypothesis → Fidelity Matrix

| Question                    | Preferred |
| --------------------------- | --------- |
| 是否存在 dominant strategy      | P1        |
| First-player advantage      | P1        |
| Economy 是否爆炸                | P1        |
| 游戏平均长度                      | P1        |
| 卡牌使用率                       | P1        |
| 胜率分布                        | P1        |
| 玩家是否理解规则                    | P2        |
| UI 是否容易理解                   | P2        |
| Decision space 是否有意义        | P2        |
| Negotiation 是否成立            | P3        |
| Social deduction 是否成立       | P3        |
| Hidden information 是否产生正确体验 | P3        |
| 桌面空间是否足够                    | P4        |
| Token 操作是否舒服                | P4        |
| 实体组件是否容易识别                  | P4        |
| Setup 是否过于繁琐                | P4        |
| 最终产品质感                      | P5        |

---

# 7. Simulation Architecture

## 7.1 Simulation must be deterministic by default

每次 simulation 必须保存：

```yaml
seed:
rules_version:
prototype_version:
simulation_version:
agent_version:
player_count:
configuration:
```

这样：

```text
same seed
+
same rules version
=
same result
```

能够支持 regression testing。

---

# 8. Simulation Run Object

新增：

```text
simulation-run.md
```

或机器可读：

```text
simulation-run.json
```

建议：

```yaml
id: SIM-001
game_version: v0.4
rules_version: R-012
seed: 482193
players: 4
agent_profiles:
  - heuristic-balanced
  - heuristic-greedy
runs: 10000

objective:
  HYP-004

metrics:
  first_player_win_rate:
  average_game_length:
  score_spread:
  comeback_rate:

anomalies:

conclusion:

confidence:
```

---

# 9. Agent Strategy Profiles

不要让一个 AI Agent 代表所有玩家。

至少提供：

## Random Agent

随机合法行动。

用途：

* rules sanity check
* baseline

---

## Greedy Agent

最大化当前 immediate utility。

用途：

* 检查短期最优策略
* 检查 obvious dominant strategies

---

## Conservative Agent

偏向：

* safety
* resource preservation
* low risk

---

## Opportunistic Agent

优先：

* combos
* tactical opportunities
* high-value temporary actions

---

## Strategic Agent

使用：

* planning
* resource valuation
* future value

---

## Adversarial Agent

目标：

> 主动寻找游戏系统的 exploit。

例如：

```text
Find strategy maximizing win rate.
```

用途非常重要。

它不是为了模拟“普通玩家”，而是为了：

> **攻击设计。**

---

# 10. AI Simulation Strategy

不建议默认让 LLM 直接“玩 10,000 局”。

原因：

* 成本高
* latency 高
* non-deterministic
* reasoning noise
* token consumption 高
* 难以 reproducible

应该采用三层 Agent：

```text
Layer 1
Deterministic / Rule-based
        ↓
Layer 2
Heuristic / Utility-based
        ↓
Layer 3
LLM Agent
```

---

## Layer 1 — Deterministic

优先使用代码执行：

```text
if legal_actions:
    choose first legal action
```

或固定策略。

用途：

* rules validation
* simulation baseline

---

## Layer 2 — Heuristic

使用：

```text
score(action)
=
immediate_value
+
future_value
+
interaction_value
-
risk
```

可以运行数千 / 数万局。

---

## Layer 3 — LLM Agent

LLM 只用于：

* complex decision making
* qualitative behavior
* unusual strategy discovery
* interpreting ambiguous rules
* human-like play patterns

不用于默认的大规模 Monte Carlo。

---

# 11. Hybrid Simulation

推荐：

```text
10,000 heuristic games
        ↓
发现异常
        ↓
100 LLM games
        ↓
分析异常策略
        ↓
Human playtest
```

而不是：

```text
10,000 LLM games
```

---

# 12. Simulation Metrics

建立标准 Metrics Taxonomy。

## Outcome Metrics

```text
win_rate
score_mean
score_median
score_std
score_spread
```

## Tempo Metrics

```text
game_length
round_length
turn_length
phase_length
```

## Economy Metrics

```text
resource_generation
resource_spend
resource_stock
resource_conversion
resource_sink
```

## Action Metrics

```text
action_frequency
action_diversity
action_success_rate
unused_action_rate
```

## Interaction Metrics

```text
attack_frequency
trade_frequency
blocking_frequency
help_frequency
negotiation_frequency
```

## Strategy Metrics

```text
strategy_distribution
dominant_action_rate
dominant_strategy_rate
strategy_switch_rate
```

## Comeback Metrics

```text
lead_change_count
comeback_rate
leader_survival_rate
```

---

# 13. Important: Metrics are not automatically fun

必须建立 Hard Invariant：

> **Metrics describe behavior; they do not prove fun.**

例如：

```text
High action diversity
≠
Interesting choices

Balanced win rate
≠
Good game

Short game
≠
Good pacing
```

因此 simulation 输出必须区分：

```text
System Evidence
```

和：

```text
Experience Evidence
```

---

# 14. Evidence Model Extension

当前：

```text
Claim
↓
Evidence
↓
Confidence
↓
Contradiction
↓
Decision
```

升级为：

```text
Claim
↓
Evidence
├── Simulation Evidence
├── Digital Playtest Evidence
├── Physical Playtest Evidence
└── Expert / Designer Evidence
↓
Confidence
↓
Contradiction
↓
Decision
```

建议 Evidence metadata：

```yaml
source_type:
  simulation
  digital_playtest
  physical_playtest
  expert
  intuition

sample_size:

method:

version:

confidence:

limitations:
```

---

# 15. Evidence Hierarchy

不要简单认为 simulation > human。

建议：

```text
                    Question-specific evidence
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
          System           Human            Physical
         Evidence         Experience        Reality
```

例如：

### First-player advantage

Simulation：

> High value.

### “玩家觉得紧张”

Simulation：

> Low value.

### “桌面太拥挤”

Simulation：

> Almost zero value.

因此 Evidence Quality 必须是：

```text
Question
+
Evidence Type
+
Fit
```

而不是固定 ranking。

---

# 16. Automated Testing Architecture

建立三层测试。

## Level 1 — Rule Tests

类似 software unit tests。

例如：

```text
setup()
draw_card()
pay_cost()
resolve_action()
end_round()
calculate_score()
```

测试：

```text
assert resource >= 0
assert deck_count decreases by 1
assert score calculated correctly
```

---

## Level 2 — Invariant Tests

测试设计不变量。

例如：

```text
No player may receive negative resources.

Game must eventually terminate.

All cards must have valid IDs.

All actions must be resolvable.

Every player must have at least one legal action during normal play.
```

---

## Level 3 — Property Tests

测试：

> 在大量随机输入下，系统是否始终满足设计性质。

例如：

```text
For all legal states:
    score calculation is deterministic.
```

或：

```text
For all games:
    game terminates within 100 rounds.
```

---

# 17. Monte Carlo Test Suite

建立：

```text
simulation/
├── scenarios/
├── agents/
├── metrics/
├── seeds/
├── runs/
└── reports/
```

建议默认测试规模：

```text
Smoke:
100 games

Development:
1,000 games

Balance:
10,000 games

Regression:
1,000 fixed-seed games

Stress:
100,000+ games when cheap
```

实际数量应该由 game complexity 自动调整。

---

# 18. Regression Simulation

每次规则版本变化：

```text
v0.5
↓
v0.6
```

自动比较：

```text
win_rate
game_length
score_spread
action_frequency
resource_flow
```

输出：

```text
REGRESSION REPORT

Game:
v0.6

Compared:
v0.5

Changes:
first_player_win_rate
  31% → 44%  ⚠

average_game_length
  47m → 61m  ⚠

resource_A:
  +18%       ℹ

dominant_action_rate:
  21% → 39%  🔴
```

这应该成为未来 Design State 的 Evidence 来源。

---

# 19. Statistical Guardrails

AI 不得根据少量 simulation 宣布：

> “已证明平衡。”

必须考虑：

```text
sample size
variance
confidence interval
effect size
seed sensitivity
```

尤其是：

```text
10 games
```

不能支持强结论。

建议：

```text
Low:
< 100 runs

Medium:
100–999

High:
1000+ with stable result
```

但这只是默认值，不能替代 statistical validity。

---

# 20. Automated Test Selection

不要每次运行所有 tests。

根据当前 Hypothesis 自动选择：

```text
HYP-001:
first-player advantage
→ first-player simulation suite

HYP-002:
economy runaway
→ resource-flow suite

HYP-003:
dominant strategy
→ adversarial agent suite

HYP-004:
game too long
→ termination / game-length suite
```

建立：

```text
Hypothesis
↓
Test Profile
↓
Minimum Required Simulation
```

---

# 21. Experiment Engine Integration

当前：

```text
Hypothesis
↓
Experiment
↓
Playtest
```

升级：

```text
Hypothesis
↓
Experiment Planner
↓
Choose cheapest valid evidence method
├── Simulation
├── Digital test
├── Physical test
└── Mixed
↓
Evidence
↓
Decision
```

例如：

```text
HYP-017:
First player advantage too high

Recommended:
P1 Simulation

Cost:
Low

Evidence quality:
High

Run:
10,000 games
```

而：

```text
HYP-021:
Players don't feel enough tension

Recommended:
P2/P3 Human Playtest

Simulation:
Not sufficient
```

---

# 22. Experiment Priority 2.0

当前优先级：

```text
Impact × Uncertainty × (1 / Test Cost)
```

升级为：

```text
Priority =
Impact
×
Uncertainty
×
Evidence Gap
×
Decision Relevance
÷
Test Cost
```

其中：

### Evidence Gap

当前证据越不足，优先级越高。

### Decision Relevance

如果该 Hypothesis 会阻塞：

```text
Locked decision
Prototype gate
Kill gate
```

则提高优先级。

---

# 23. Prototype Gate

增加：

```text
prototype-gate.md
```

每一个 Fidelity Level 都有进入条件。

例如：

## P1 → P2

必须：

```text
Rules executable
No critical invariant failures
No obvious dominant strategy
Game terminates
Core economy stable
```

## P2 → P3/P4

必须：

```text
Core loop understandable
Core actions usable
No critical UI ambiguity
```

## P3/P4 → P5

必须：

```text
Core experience validated
Physical constraints validated
Major balance risks resolved
```

---

# 24. Digital Prototype Architecture

建议不要一开始绑定具体 engine。

建立抽象：

```text
Game Model
    ↓
Rules Engine
    ↓
State
    ↓
Action Resolver
    ↓
Event Log
    ↓
Metrics
```

UI：

```text
                 ┌── Web UI
Rules Engine ────┼── TTS adapter
                 ├── CLI
                 └── Simulation
```

核心原则：

> **Rules Engine must be independent from UI.**

这样：

```text
Human player
Bot
LLM Agent
CLI
Web UI
TTS
```

都可以调用同一套 rules。

---

# 25. Canonical Game State

建立：

```text
game-state.json
```

作为 Digital Prototype 的 canonical state。

示例：

```json
{
  "version": "0.6",
  "round": 4,
  "current_player": "P2",
  "players": {
    "P1": {
      "resources": {},
      "hand": [],
      "score": 12
    },
    "P2": {
      "resources": {},
      "hand": [],
      "score": 15
    }
  },
  "board": {},
  "deck": {},
  "history": []
}
```

所有：

```text
simulation
CLI
Web
TTS
```

尽可能共享该模型。

---

# 26. Event Log

所有游戏行为转换成 Event：

```json
{
  "turn": 12,
  "player": "P2",
  "event": "BUY_CARD",
  "target": "CARD-014",
  "cost": {
    "gold": 3
  }
}
```

Event log 是未来：

* replay
* debugging
* telemetry
* analytics
* regression
* AI training

的基础。

---

# 27. Replay

Digital Prototype 必须支持：

```text
seed
+
game version
+
event log
```

重新播放一局。

用途：

* bug reproduction
* design debugging
* unusual strategy analysis
* player behavior review

未来可以：

```text
Replay → branch at turn 17
```

测试：

> “如果玩家在这里选择 B，会发生什么？”

---

# 28. AI Game Master / Rules Interpreter

LLM 可以作为：

```text
Rules Interpreter
```

但不能成为唯一 source of truth。

推荐：

```text
Natural Language Rules
        ↓
Structured Rules
        ↓
Rules Engine
        ↓
LLM Explanation Layer
```

而不是：

```text
LLM reads rulebook
↓
LLM decides what happens
```

后者非常容易产生 simulation hallucination。

---

# 29. Rulebook → Executable Rules

未来可以支持：

```text
rulebook-draft.md
↓
rules-schema
↓
machine-readable rules
↓
simulation / digital prototype
```

目标不是完全自动编译自然语言。

第一阶段只要求：

> Agent 将核心规则结构化。

例如：

```yaml
action:
  id: BUY_CARD
  cost:
    gold: 3
  effect:
    draw: 1
```

---

# 30. Component Schema 2.0

当前已有：

```text
component-schema.json
```

下一步扩展：

```yaml
component:
  id:
  type:
  name:
  quantity:
  cost:
  effect:
  tags:
  vp:

  visual:
    template:
    icon:
    color_group:

  digital:
    asset:
    interaction:

  physical:
    size:
    material:
    handling:
```

这样同一个 Component Definition 可以同时生成：

```text
PnP
nanDECK
Digital UI
TTS
Simulation data
```

---

# 31. Prototype as a First-Class Core Object

当前 Core Objects：

```text
State
Claim
Experiment
Artifact
```

新增：

```text
Prototype
```

即：

```text
State
Claim
Experiment
Prototype
Evidence
Artifact
```

Prototype metadata：

```yaml
id:
type:
fidelity:
version:
source_rules:
hypotheses:
supported_tests:
known_limitations:
generated_at:
```

---

# 32. Prototype Lineage

必须记录：

```text
P0.1
↓
P0.2
↓
P1.0
↓
P1.1
↓
P2.0
↓
P4.0
```

每个 Prototype 都关联：

```text
Game Version
Experiment
Hypothesis
Evidence
Decision
```

这样可以回答：

> “为什么这个数字版本和上一个版本不同？”

---

# 33. Physical vs Digital Divergence

必须允许：

```text
Digital Rule
≠
Physical Rule
```

但必须显式记录。

例如：

```yaml
digital_substitution:
  - "automatic resource counting"
  - "instant card shuffling"

physical_constraint:
  - "manual counting"
  - "manual shuffle"
```

Agent 必须标记：

```text
DIGITAL-ONLY
```

或：

```text
PHYSICAL-DEPENDENT
```

避免数字测试结果被误用于实体体验结论。

---

# 34. Digital-to-Physical Validation Matrix

| Property            | Simulation | Digital | Physical |
| ------------------- | ---------: | ------: | -------: |
| Probability         |        ★★★ |      ★★ |        ★ |
| Balance             |        ★★★ |      ★★ |        ★ |
| Game length         |        ★★★ |      ★★ |       ★★ |
| Rules correctness   |        ★★★ |     ★★★ |       ★★ |
| UI clarity          |          — |     ★★★ |      ★★★ |
| Agency              |          ★ |     ★★★ |      ★★★ |
| Social interaction  |          — |      ★★ |      ★★★ |
| Negotiation         |          — |      ★★ |      ★★★ |
| Physical ergonomics |          — |       — |      ★★★ |
| Table space         |          — |       — |      ★★★ |
| Component handling  |          — |       — |      ★★★ |
| Atmosphere          |          ★ |      ★★ |      ★★★ |

`★` 表示适用程度，而不是质量。

---

# 35. Automated Playtest Reports

每次 simulation / digital test 应生成：

```text
reports/
  SIM-001/
    summary.md
    metrics.json
    anomalies.json
    strategy-analysis.md
    regression.md
```

Summary 示例：

```text
SIM-001

Runs: 10,000
Players: 4
Version: v0.6

First-player win:
31.8%

Average length:
47.2 rounds

Dominant action:
BUY_CARD = 42.7%

Potential issue:
BUY_CARD selected > 2× next action.

Recommendation:
Open HYP-012.
Do not change rules automatically.
```

---

# 36. AI Should Diagnose, Not Auto-Fix

Simulation 发现：

```text
BUY_CARD = 42.7%
```

Agent 不应该自动：

```text
increase cost from 3 → 4
```

而应该：

```text
Observation
↓
Diagnostic
↓
Hypothesis
↓
Candidate intervention
↓
Experiment
```

保持 v3 的核心 invariant：

> Diagnose before changing.

---

# 37. Automated Fuzz Testing

对 Rules Engine 进行随机状态测试：

```text
random setup
random legal actions
random player counts
random resource distributions
random deck states
```

检查：

```text
No crash
No illegal state
No impossible resource
No infinite loop
No invalid winner
No unresolved action
```

这可以成为：

```text
BG015 — Runtime State Integrity
```

---

# 38. New Lint Rules

建议增加：

### BG015 — Prototype Fidelity Mismatch

例如：

> 用 simulation 证明 social tension。

### BG016 — Unvalidated Digital Assumption

数字 prototype 中使用了实体版不会存在的 automation。

### BG017 — Missing Simulation Seed

Simulation 无 reproducibility metadata。

### BG018 — Missing Rules Version

Simulation / playtest 没有关联 rules version。

### BG019 — Unsupported Claim

Claim 的 evidence type 不适合该 claim。

### BG020 — Physical Validation Required

Claim 明确依赖实体体验，却只有 digital evidence。

---

# 39. Evaluation 2.0

当前 Evaluation：

```text
Structural = automated
Behavior = manual
```

升级为：

```text
Layer 1
Structural

Layer 2
Behavior

Layer 3
Simulation

Layer 4
Regression
```

---

# 40. New Evaluation Cases

保留现有 A–F。

增加：

## Case G — Simulation

Prompt：

> Analyze first-player advantage and run an appropriate simulation strategy.

检查：

* correct prototype fidelity
* deterministic seed
* appropriate agent
* sufficient runs
* metrics
* confidence
* no unsupported claim

---

## Case H — Digital Prototype

检查：

* canonical game state
* rules separation
* UI-independent rules
* event log
* telemetry

---

## Case I — Regression

修改一个 rule：

```text
cost 3 → 4
```

验证：

```text
simulation
→ metrics
→ regression report
```

---

## Case J — Fidelity Selection

给 Agent 一个 ambiguous hypothesis。

检查：

> Agent 是否选择了最便宜且足够回答问题的 Prototype Level？

---

# 41. Golden Artifacts 2.0

新增：

```text
eval/golden/
  design-state/
  hypothesis/
  experiment/
  playtest/
  simulation-run/
  game-state/
  event-log/
  prototype/
  regression-report/
```

Validator 检查：

```text
schema
required fields
IDs
version references
seed
lineage
evidence references
```

---

# 42. Automated Behavior Evaluation

目标：

```text
Prompt
↓
Agent
↓
Artifacts
↓
Structural Validator
↓
Semantic Assertions
↓
Score
```

Semantic assertions 可以首先使用 rule-based checks：

```text
must mention simulation
must not claim fun validated
must include seed
must include sample size
must choose P1 for balance hypothesis
must choose P4 for physical ergonomics
```

后续再加入 LLM judge。

---

# 43. LLM Judge Guardrails

LLM judge 不应该单独决定 pass/fail。

推荐：

```text
Deterministic Validator
+
Metric Assertions
+
LLM Judge
```

最终：

```text
Score =
structural
+
behavioral
+
simulation
```

---

# 44. CI / Release Gate

未来 release：

```bash
pytest
python eval/validators/validate.py --fixture-all
python eval/simulation/run_regression.py
python eval/eval_behavior.py
```

Release gate：

```text
Structural: 100%
Simulation regression: PASS
Behavior: ≥ 5/6
Critical invariants: 100%
```

---

# 45. Recommended Repository Structure

建议 v4：

```text
board-game-design/
│
├── SKILL.md
│
├── core/
│   ├── objects.md
│   ├── evidence.md
│   └── fidelity-ladder.md
│
├── simulation/
│   ├── README.md
│   ├── architecture.md
│   ├── agents/
│   │   ├── random.md
│   │   ├── greedy.md
│   │   ├── conservative.md
│   │   ├── opportunistic.md
│   │   ├── strategic.md
│   │   └── adversarial.md
│   ├── metrics/
│   ├── scenarios/
│   ├── schemas/
│   │   └── simulation-run.json
│   └── reports/
│
├── digital/
│   ├── README.md
│   ├── architecture.md
│   ├── game-state.schema.json
│   ├── event-log.schema.json
│   ├── rules-engine.md
│   ├── telemetry.md
│   └── replay.md
│
├── prototype/
│   ├── fidelity-ladder.md
│   ├── selection.md
│   └── gates.md
│
├── tools/
│   ├── component-schema.json
│   ├── export-pipeline.md
│   ├── validate_components.py
│   └── examples/
│
├── eval/
│   ├── benchmark-prompts.md
│   ├── validators/
│   ├── golden/
│   ├── fixtures/
│   ├── simulation/
│   └── regression/
│
├── routing/
├── diagnostics/
├── experiments/
├── balance/
├── lint/
├── genre-profile/
├── chapters/
├── reasoning/
├── templates/
└── docs/
```

---

# 46. SKILL.md Changes

当前：

```text
Prototype
→ templates
→ export pipeline
```

升级为：

```text
Prototype
→ fidelity selection
→ simulation / digital / physical
→ appropriate toolchain
```

建议 Agent Modes：

```text
Create
Diagnose
Experiment
Simulate
Prototype
Balance
Evaluate
```

其中：

### Simulate

Trigger：

```text
test balance
run many games
check strategy
estimate win rate
find dominant strategy
stress test rules
```

Load：

```text
simulation/README.md
core/fidelity-ladder.md
```

---

# 47. Mixed Mode Priority

新的 priority tree：

```text
User Request
│
├── Existing symptom?
│     └── Diagnose
│
├── Specific hypothesis?
│     └── Experiment
│
├── System question?
│     └── Simulate
│
├── Human experience question?
│     └── Digital / Physical Playtest
│
├── Broken numeric system?
│     └── Balance
│
└── New game?
      └── Create
```

Prototype 不再是单一默认步骤。

---

# 48. Design State Extension

增加：

```text
## Prototype State

| ID | Fidelity | Version | Status | Purpose |
|---|---|---|---|---|
| PRT-001 | P1 Simulation | v0.3 | active | first-player test |
| PRT-002 | P2 Digital | v0.4 | active | usability |
| PRT-003 | P4 Physical | v0.5 | planned | ergonomics |
```

增加：

```text
## Simulation Evidence

| ID | Runs | Seed | Metric | Finding | Confidence |
|---|---:|---|---|---|---|
```

---

# 49. Hypothesis Extension

新增：

```yaml
preferred_fidelity:
minimum_fidelity:
evidence_type:
simulation_profile:
physical_dependency:
```

例如：

```yaml
id: HYP-017
claim: "First player has excessive advantage"

preferred_fidelity: P1
minimum_fidelity: P1
evidence_type: simulation
simulation_profile: first-player-advantage
physical_dependency: false
```

---

# 50. Experiment Template Extension

新增：

```text
## Evidence Plan

Minimum evidence source:
Prototype fidelity:
Simulation profile:
Human playtest required:
Physical validation required:
```

这样 Experiment Engine 可以自动选择测试方式。

---

# 51. Kill Criteria Integration

Kill criteria 不应该只读取 physical playtests。

应该支持：

```text
Simulation Gate
Digital Gate
Physical Gate
```

例如：

```text
Simulation:
dominant strategy detected
→ Red

Digital:
players repeatedly misunderstand action
→ Yellow

Physical:
setup > 20 min
→ Red
```

但：

> Automated failure should trigger investigation, not automatically kill the game.

---

# 52. Genre-specific Simulation Profiles

不同 Genre 必须使用不同 simulation strategy。

## Euro

重点：

* win rate
* economy
* strategy
* efficiency

## Party

Simulation价值较低。

重点：

* rules
* timing
* content coverage

Human test priority 高。

## Social Deduction

普通 simulation 很有限。

重点：

* information structure
* role balance
* information leakage

需要：

```text
LLM / human agents
```

## Solo

重点：

* difficulty
* variance
* Automa behavior
* scenario stability

---

# 53. Simulation Confidence

Simulation Confidence 不应该只根据 runs 数量。

建议：

```text
Confidence =
Sample Size
+
Stability
+
Seed Robustness
+
Agent Diversity
+
Effect Size
+
Question Fit
```

例如：

```text
10,000 games
1 agent
one seed
small effect
```

不应该自动得到 High。

---

# 54. AI Agent Diversity Requirement

如果某策略只击败：

```text
Greedy Agent
```

不能宣布：

> “Strategy is dominant.”

至少检查：

```text
Greedy
Strategic
Random baseline
Adversarial
```

如果不同 agent 都得到类似结果，证据更强。

---

# 55. Adversarial Design Mode

未来可以增加：

```text
Break the Game
```

目标：

> 主动寻找规则漏洞。

Agent 应尝试：

```text
maximize win rate
maximize resource accumulation
find infinite loop
find degenerate strategy
find kingmaking exploit
find unreachable state
```

输出：

```text
Exploit:
Strategy:
Reproduction:
Severity:
Suggested Experiment:
```

这会成为非常有特色的功能。

---

# 56. LLM-assisted Strategy Discovery

对于复杂游戏：

```text
Simulation
↓
Top winning trajectories
↓
LLM analyzes event logs
↓
Strategy hypothesis
↓
HYP-XXX
```

例如：

```text
Observation:
Winning games purchase CARD-014 in rounds 2–3.

Hypothesis:
CARD-014 creates an early tempo advantage.

Confidence:
Medium.

Next:
Test CARD-014 cost +1.
```

这样 simulation 也能反向驱动 Design Reasoning。

---

# 57. Automatic Experiment Generation

Simulation 不应该直接修改规则。

应该自动生成：

```text
SIM-021
↓
Anomaly
↓
HYP-031
↓
EXP-018
```

例如：

```text
Anomaly:
action A chosen in 71% of all turns.

Potential cause:
A has dominant expected value.

Generated HYP:
"Action A is strategically dominant."

Generated EXP:
"Reduce A reward by 1."

Status:
Proposed — not yet accepted.
```

Human / designer remains the decision maker.

---

# 58. Physical Validation Triggers

Agent 应自动识别：

```text
Physical Dependency = High
```

例如：

* dexterity
* spatial layout
* tactile component
* hidden physical information
* simultaneous grabbing
* physical bluffing
* card handling
* token management

这些不得仅凭 digital simulation 宣布完成。

---

# 59. Recommended Development Phases

## Phase 1 — Foundation

优先级：P0

实现：

* Prototype Fidelity model
* Prototype object
* Simulation Run schema
* Game State schema
* Event Log schema
* Design State integration

---

## Phase 2 — Simulation

优先级：P0

实现：

* deterministic simulator
* Random Agent
* Greedy Agent
* metrics
* seed
* reports
* regression

---

## Phase 3 — Validation

优先级：P0

实现：

* component validator
* simulation validator
* prototype validator
* regression validator
* Cases G–J

---

## Phase 4 — Digital Prototype

优先级：P1

实现：

* lightweight web runtime
* canonical rules engine
* event log
* replay
* telemetry

---

## Phase 5 — AI Agents

优先级：P1

实现：

* heuristic agents
* adversarial agents
* LLM agent adapter
* strategy discovery

---

## Phase 6 — Advanced Automation

优先级：P2

实现：

* automatic hypothesis generation
* experiment recommendation
* automatic regression reports
* automatic digital prototype generation

---

# 60. MVP Definition

v4.0 不需要一次完成全部内容。

推荐 MVP：

```text
1. Fidelity Ladder
2. Simulate Mode
3. Deterministic game model
4. Random + Greedy agents
5. 1,000–10,000 game simulation
6. Standard metrics
7. Seeded runs
8. Simulation Run artifact
9. Simulation → Evidence integration
10. Regression comparison
11. Component schema validator
12. Cases G–I
```

暂时不要求：

* multiplayer web
* LLM agents
* TTS integration
* automatic UI generation

---

# 61. v4.0 Success Criteria

一个 Skill v4.0 project 至少应该能够：

### Scenario A

用户：

> “这个游戏可能有 first-player advantage。”

Agent：

```text
Read design-state
↓
Recognize system hypothesis
↓
Select P1
↓
Run / propose simulation
↓
Use seeded agents
↓
Generate metrics
↓
Update Evidence
↓
Update HYP confidence
```

---

### Scenario B

用户：

> “玩家说游戏有点无聊。”

Agent：

```text
Symptom Routing
↓
Evidence discriminator
↓
Diagnose
↓
Determine whether simulation can answer
↓
If not:
recommend human digital/physical playtest
```

---

### Scenario C

用户：

> “我把 card cost 从 3 改成 4。”

Agent：

```text
Version bump
↓
Simulation regression
↓
Compare metrics
↓
Flag significant changes
↓
Do not auto-accept rule
```

---

### Scenario D

用户：

> “这个游戏已经在数字版里很好玩了。”

Agent 应回答：

```text
Digital evidence supports:
- rules
- pacing
- agency
- interaction

Still unvalidated:
- physical ergonomics
- table footprint
- component handling
```

然后推荐 P4，而不是宣布游戏完成。

---

# 62. Updated Core Loop

最终建议将 Skill 的 Core Loop 改为：

```text
Intent
  ↓
Experience / Model
  ↓
Claim / Hypothesis
  ↓
Select Minimum Valid Fidelity
  ↓
Prototype
  ↓
Simulation / Digital / Physical Experiment
  ↓
Evidence
  ↓
Diagnosis
  ↓
Decision
  ↓
Design State
  ↓
Repeat
```

最重要的新原则：

> **Do not build a higher-fidelity prototype than the hypothesis requires.**

---

# 63. Updated Design Philosophy

v4 的核心原则建议固定为：

### Principle 1 — Evidence over opinion

### Principle 2 — State preservation

### Principle 3 — Diagnose before changing

### Principle 4 — Minimal intervention

### Principle 5 — Cheapest valid test first

### Principle 6 — System evidence ≠ experience evidence

### Principle 7 — Automation validates systems, humans validate experiences

### Principle 8 — Digital does not replace physical validation

### Principle 9 — Reproducibility matters

### Principle 10 — Never auto-fix from a simulation anomaly

---

# 64. Final Architecture

最终 Skill 应形成：

```text
                         BOARD GAME DESIGN
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
     EXPERIENCE             REASONING              STATE
          │                     │                     │
       MDA / Genre        Claim / Hypothesis      Design State
       Emotion            Diagnosis                Version Lineage
       Theme              Experiment               Evidence
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                         FIDELITY ENGINE
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
       P0                      P1                      P2
     Model                Simulation               Digital
                                │                       │
                                │                       ↓
                                │                      P3
                                │                  Multiplayer
                                │                       │
                                └──────────┬────────────┘
                                           ↓
                                          P4
                                      Physical PnP
                                           ↓
                                          P5
                                   Production Prototype
                                           │
                                           ↓
                                      EVIDENCE
                                           │
              ┌────────────────────────────┼───────────────────────┐
              │                            │                       │
          Simulation                   Human                    Physical
           Metrics                    Experience                Reality
              │                            │                       │
              └────────────────────────────┼───────────────────────┘
                                           ↓
                                      DIAGNOSTICS
                                           ↓
                                      DECISION
                                           ↓
                                      DESIGN STATE
```

横切所有层：

```text
Lint
Validation
Regression
Confidence
Version Lineage
```

---

# 65. Recommended Priority

## P0 — Must Have

1. Prototype Fidelity Ladder
2. Simulate Mode
3. Simulation Run schema
4. Deterministic seed
5. Random + Greedy agents
6. Standard metrics
7. Simulation → Evidence
8. Simulation regression
9. Component schema validator
10. Evaluation Cases G–I

## P1 — Strongly Recommended

11. Canonical Game State
12. Event Log
13. Replay
14. Digital Prototype architecture
15. Adversarial Agent
16. Heuristic Agent framework
17. Prototype Gates
18. Physical Dependency classification
19. Fidelity-aware Experiment Priority

## P2 — Advanced

20. LLM Agent
21. Automatic strategy discovery
22. Automatic anomaly → hypothesis generation
23. Automatic experiment generation
24. Browser digital prototype generation
25. Multiplayer digital prototype
26. Automatic regression dashboard

---

# 66. Expected Outcome

完成后，Skill 不再只是：

> “帮助 AI 设计桌游。”

而会成为：

> **An evidence-driven tabletop game design and prototyping system that chooses the cheapest valid experiment, simulates game systems automatically, validates human experience digitally, and escalates to physical prototypes only when physical reality matters.**

最终设计哲学可以浓缩成一句话：

> **Build the smallest thing that can answer the biggest question.**

以及：

> **Simulate systems. Playtest experiences. Validate reality.**

[1]: https://github.com/kyle-ip/board-game-design "GitHub - kyle-ip/board-game-design: Design tabletop mechanisms, run playtest experiments, and ship paper prototypes — with design state, diagnostics, and evidence-driven iteration. · GitHub"
