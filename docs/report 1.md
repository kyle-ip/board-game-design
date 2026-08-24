
下面这份报告，我把重点放在一个问题上：

> **如何把你现在已经相当完整的“桌游设计知识 + 原型工作流 Skill”，进一步演进成一个真正能够持续参与设计、诊断、实验、迭代的 Board Game Design Agent。**

我重新检查了你当前仓库的 `SKILL.md`、`workflow.md`、`patterns.md`、`cheatsheet.md`、`playtesting.md`、`probability-and-balance.md` 以及几个核心模板；同时参考了当前 Agent Skills 规范。你的 Skill 本身已经遵循了比较好的 progressive disclosure 结构，而且 `SKILL.md` 目前约 157 行，明显低于规范建议的 500 行以内；规范也明确鼓励把详细知识放入按需加载的 reference/resources 中。

------

# 一、执行摘要

我对当前版本的判断，比上一轮更明确：

### 当前版本不是“还缺很多知识”

实际上，你现在的知识层已经比较扎实。

你已经有：

- 13 类核心机制
- pattern catalog
- symptom → resource routing
- workflow
- playtest framework
- balance rules
- PnP / printing
- concept / mechanism / playtest / balance 等项目模板

而且这些东西已经被组织成一个明确的：

> Concept → Mechanism → Paper PnP → Playtest → Balance → Publish

流程。

### 真正的问题是：

**“设计决策”还没有成为一个独立的一等对象。**

现在的结构更接近：

```
Knowledge
   ↓
Workflow
   ↓
Artifacts
   ↓
Playtest
```

下一阶段应该变成：

```
Design Intent
      ↓
Design Model
      ↓
Hypothesis
      ↓
Design Decision
      ↓
Prototype
      ↓
Experiment
      ↓
Evidence
      ↓
Diagnosis
      ↓
Iteration
```

这是两者最大的区别。

------

# 二、当前架构的成熟度评估

我把你的 Skill 分成七层来看。

| 层级                    | 当前成熟度 | 判断                   |
| ----------------------- | ---------: | ---------------------- |
| Agent Skill 基础结构    |       9/10 | 已经很好               |
| 桌游机制知识            |       9/10 | 暂时不应继续无脑扩张   |
| 机制选择与 routing      |       8/10 | 已经实用               |
| Prototype workflow      |     8.5/10 | 很成熟                 |
| Playtest                |     7.5/10 | 有框架，但还缺“实验化” |
| Balance / Diagnosis     |     6.5/10 | 是下一阶段重点         |
| Persistent Design State |       3/10 | 当前最大结构性缺口     |

其中最值得强调的是最后一项。

------

# 三、你现在最大的结构问题：Skill 是“过程型”，不是“状态型”

你的 `workflow.md` 定义得非常清晰：

> Stage 0 Concept
> Stage 1 Core Mechanic MVP
> Stage 2 Structure
> Stage 3 Playtest
> Stage 4 Polish
> Stage 5 Publish

并且要求每个阶段写对应 artifact。

这是很好的 workflow。

但是有一个隐藏问题：

## Agent 缺少一个“当前游戏到底处于什么设计状态”的单一事实来源。

例如一个游戏经过 8 次 playtest 后，Agent 应该知道：

```
当前已经确定：
- 4 人游戏
- 45–60 分钟
- Worker Placement
- 公开资源市场
- VP 独立于资源币
```

同时也应该知道：

```
尚未确定：
- First Player Advantage
- End-game timing
- 玩家之间的直接 interaction
```

还应该知道：

```
已经否决：
- Auction
- Hidden Roles
- Dice combat
```

再进一步：

```
最近一次实验：
假设：减少资源供给会增加资源竞争
结果：成立
```

而目前这些信息是分散在：

- `mechanism-skeleton.md`
- `balance-notes.md`
- `playtest-log.md`
- rulebook
- concept brief

中的。

所以当前 Agent 很容易出现一个典型问题：

> **它“读过历史”，但没有真正维护设计状态。**

------

# 四、建议新增核心对象：`design-state.md`

这是我认为整个 v2 最重要的改动。

我建议：

```
game-project/
├── concept-brief.md
├── design-state.md        ← 新增
├── mechanism-skeleton.md
├── rulebook-draft.md
├── components-sheet.md
├── playtests/
│   ├── PT-001.md
│   ├── PT-002.md
│   └── PT-003.md
├── experiments/
│   ├── EXP-001.md
│   └── EXP-002.md
├── decisions/
│   ├── DEC-001.md
│   └── DEC-002.md
├── balance-notes.md
└── ...
```

其中：

## `design-state.md`

只记录：

### 1. Locked

已经决定，不要反复讨论。

### 2. Open

尚未解决的问题。

### 3. Hypotheses

正在验证的设计假设。

### 4. Evidence

重要 playtest evidence。

### 5. Rejected

已经否决的方案。

### 6. Current risks

目前最大的设计风险。

### 7. Next experiment

下一轮最值得验证什么。

------

# 五、为什么这比继续增加 mechanism chapter 更重要

你当前的 mechanism catalog 已经很丰富：

Structure、Turn Order、Actions、Resolution、Victory、Uncertainty、Economics、Auctions、Worker Placement、Movement、Area Control、Set Collection、Card Mechanisms，一共 13 个章节。

`patterns.md` 进一步提供了带 code、使用场景与 trade-off 的 mechanism lookup。

而 `cheatsheet.md` 已经开始承担 decision layer，例如：

- snowball → balance
- randomness → input/output randomness
- AP → reduce branching
- auction → auction chapter
- worker placement blocking → worker placement chapter



所以你的知识瓶颈其实已经不大。

现在继续添加：

> Negotiation / Trading / Social Deduction / Trick Taking / Legacy……

当然有价值，但边际收益已经下降。

真正缺的是：

> **为什么在当前这个设计状态下选择 A 而不是 B？**

------

# 六、第二个核心改造：从“Mechanism Selection”升级到“Design Reasoning”

当前 pattern 的结构大致是：

```
When to use
How
Trade-offs
```

这是不错的机制知识格式。

但我建议下一版增加：

```
Design goal
      ↓
Constraints
      ↓
Candidate mechanisms
      ↓
Trade-offs
      ↓
Expected dynamics
      ↓
Failure risks
      ↓
Experiment
```

例如 Agent 不应该只回答：

> “可以使用 Worker Placement。”

而应该输出：

```
Design goal:
制造稀缺资源竞争。

Constraints:
- 2–4 players
- 45 min
- 中等复杂度
- 不希望过度 blocking

Candidates:
A. Worker Placement
B. Action Drafting
C. Open Market

Recommendation:
A

Why:
- 强竞争性
- decision density 高
- 与资源经济天然耦合

Risk:
- 2P blocking 价值不足
- first-player advantage

Test:
- Prototype A
- Prototype B
- 比较 3 个指标
```

这才是真正的 **design reasoning**。

------

# 七、建议增加 `decision matrix`

这是一个成本很低、收益非常高的改动。

例如：

```
Candidate | Agency | Interaction | Complexity | Variance | AP Risk
----------|--------|-------------|------------|----------|--------
Worker Placement | High | High | Medium | Low | Medium
Action Drafting  | High | Medium | Low | Low | Low
Dice Selection    | Medium | Low | Low | High | Low
```

然后要求 Agent：

> 不要只给一个机制；至少在存在明显设计 trade-off 时比较 2–4 个候选方案。

这样能显著减少 LLM 最常见的问题：

> **第一个想到的机制就直接用了。**

------

# 八、第三个核心改造：把 Playtest 从“记录”升级成“实验”

这一点你其实已经走到一半了。

你现在的 `playtest-log.md` 已经有：

> Hypothesis Under Test
> What one thing are you trying to learn?

这已经是非常好的基础。

而 `playtesting.md` 也已经具备：

- Scattershot
- Four Fs
- Good/Bad/Meh
- Three-Bucket
- Blind Rulebook

等不同测试框架。

但它仍然偏：

> **Playtest logging**

而不是：

> **Experiment management**

------

# 九、建议增加 `experiment.md`

我会把它设计成：

```
Experiment ID
Objective
Hypothesis
Design Variable
Baseline
Variant
Success Criteria
Observed Data
Conclusion
Decision
Next Experiment
```

例如：

```
EXP-004

Objective:
降低 First Player Advantage

Hypothesis:
Changing first player selection to auction
will reduce seat advantage.

Baseline:
Player 1 wins 58% in 10 plays.

Variant:
Players bid 0–3 influence for first player.

Success criteria:
P1 win rate < 40%.

Result:
P1 win rate = 31%.

Conclusion:
Hypothesis supported.

Decision:
Keep mechanism.

Follow-up:
Check whether bidding adds excessive downtime.
```

这一步一旦建立，你的 Skill 就有了：

> **Scientific method / experimental loop**

的雏形。

------

# 十、特别重要：Hypothesis 必须“可证伪”

我建议在 Skill 中加入一个硬规则：

> **每一个 design hypothesis 必须描述 observable evidence。**

不要：

> “玩家应该觉得更紧张。”

而是：

> “至少 3/4 玩家在最终两轮中主动调整策略，并且至少一次因资源稀缺改变原计划。”

不要：

> “这个机制应该更有趣。”

而是：

> “在 5 次 playtest 中，该机制至少出现 3 次玩家主动谈论/主动选择，而非被规则强迫执行。”

当然这些阈值不必固定，但必须存在。

------

# 十一、第四个核心改造：建立 Design Diagnosis Engine

这是我认为你的 Skill 最终最有差异化竞争力的部分。

目前你已经有很多 failure modes：

- Snowball
- Kingmaking
- Dominant Strategy
- Turtling
- Lucky Runaway
- Analysis Paralysis
- First Player Advantage
- Dead Last / No Agency

而且有对应 tell + fix。

这其实已经是一个 **diagnosis knowledge base** 的雏形。

下一步应该把它正式化。

------

# 十二、建议建立 `diagnostics/`

例如：

```
diagnostics/
├── runaway-leader.md
├── first-player-advantage.md
├── dominant-strategy.md
├── analysis-paralysis.md
├── dead-turn.md
├── low-agency.md
├── kingmaking.md
├── runaway-randomness.md
└── weak-interaction.md
```

每个 diagnosis 都统一使用：

```
Symptom

Likely Causes

Evidence to Collect

Diagnostic Questions

Candidate Fixes

Risks of Each Fix

Minimal Experiment

Success Criteria
```

于是用户说：

> “我的游戏玩起来很无聊。”

Agent 不应该直接推荐机制。

它应该首先进入：

```
Diagnosis mode
```

然后区分：

```
Low decision density?
Low interaction?
Low uncertainty?
Repetitive action?
Weak payoff?
No meaningful progression?
```

然后才开始 intervention。

------

# 十三、最关键的原则：先诊断，再修改

我建议把它写成 v2 的核心 invariant：

> **Do not change a mechanism before identifying the observed symptom and a plausible causal hypothesis.**

这句话非常重要。

因为 LLM 在游戏设计中一个非常常见的问题是：

```
Problem:
“游戏无聊。”

LLM:
“加资源卡。”
```

而成熟设计过程应该是：

```
Symptom
↓
Diagnosis
↓
Hypothesis
↓
Minimal intervention
↓
Experiment
```

------

# 十四、第五个核心改造：从线性 Workflow 转为“Milestone + Loop”

你现在写的是：

> “Pick the row that matches your project state; do not run stages in parallel.” 

我建议这个思想保留，但修改含义：

**Stage 不是 waterfall，而是 milestone。**

也就是：

```
Stage 0 Concept
      ↓
Stage 1 Core Loop
      ↓
Stage 2 Structure
      ↓
Stage 3 Playtest
      ↓
Stage 4 Polish
      ↓
Stage 5 Publish
```

只是允许：

```
Stage 3
  ↓
发现核心问题
  ↓
回 Stage 1
```

甚至：

```
Stage 4
  ↓
Blind Test
  ↓
Rule failure
  ↓
Stage 2
```

所以建议：

```
stage = current maturity
state transition = design decision
```

而不是：

```
stage = irreversible pipeline position
```

------

# 十五、建议增加 `iteration.md`

例如：

```
Iteration 08

Previous build:
v0.7

Observed problem:
Resource scarcity disappears after round 3.

Diagnosis:
Economy inflation.

Hypothesis:
Scaling income is too aggressive.

Change:
Reduce base income from 4 → 3.

Expected effect:
Resource pressure remains through round 4.

Experiment:
3-player playtest.

Result:
...
```

这会把你的整个项目历史串起来。

------

# 十六、第六个核心改造：把 Balance 从 checklist 升级为 Model

目前这一部分我反而觉得你基础已经很好。

你已经规定：

- dice → McDie
- card/economy → spreadsheet
- income curve
- snowball analysis
- failure mode detection

而且明确要求：

> “Do not eyeball dice-pool balance.” 

这是很正确的。

但是现在 balance 更像：

> **发现问题 → 调数字**

下一版应该进一步发展成：

> **建立价值模型 → 比较不同资源 / action / tempo 的相对价值。**

------

# 十七、建议加入 `balance-model.md`

至少建立：

```
Resource Value
Action Value
Tempo Value
VP Value
Information Value
Position Value
Risk Value
```

例如：

```
1 Wood
≈ 0.7 VP
≈ 0.25 Action
```

不需要追求绝对科学。

目标是：

> **帮助 Agent 保持内部一致性。**

这样 AI 就不会出现：

```
Card A:
cost 2 → 5 VP

Card B:
cost 3 → 2 VP
```

但它却说两个都“差不多”。

------

# 十八、应该引入“Value Budget”

例如：

```
Card:
Cost 3

Expected value:
Immediate VP: 2
Resource generation: 1.2
Tempo: 0.5
Information: 0.3

Total estimated value:
4.0

Balance target:
3.5–4.2
```

这类模型尤其适合：

- engine builder
- deck builder
- card game
- resource economy
- set collection

你的 `probability-and-balance.md` 已经建议对 cards/actions 做 spreadsheet，而且要求关注 early/mid/late income 与 snowball；因此向这个方向扩展是自然演化，而不是另起炉灶。

------

# 十九、第七个核心改造：加入 Game Design Linter

这个我非常推荐。

因为这是 Skill 最容易形成“工具感”的地方。

例如：

```
BG001 First Player Advantage
BG002 Dominant Strategy
BG003 Runaway Leader
BG004 Low Agency
BG005 Dead Turn
BG006 Kingmaking
BG007 Unbounded Engine
BG008 Randomness Dominates Skill
BG009 Analysis Paralysis
BG010 Negative Interaction
BG011 Score Opacity
BG012 Endgame Drag
BG013 Component Ambiguity
BG014 Rule Ambiguity
```

然后：

```
$ board-game-design lint
```

得到：

```
Design Lint

⚠ BG001 First Player Advantage
Evidence: 7 / 10 wins by Player 1

⚠ BG003 Runaway Leader
Evidence: leader income compounds from round 3

? BG009 Analysis Paralysis
Evidence insufficient

✓ BG005 Dead Turn
No evidence
```

当然不一定真的需要执行脚本。

第一阶段甚至可以完全基于 Markdown + Agent instructions 实现。

------

# 二十、第八个核心改造：增加“最小修改原则”

这是我特别建议加入的。

现在你的 balance notes 已经有一个很好的规则：

> “Spot tell in 2+ playtests → apply one fix → measure in the next playtest. Do not stack three balance changes at once.” 

我会把这个规则从 balance 扩展为整个 Skill：

> **Change the smallest design variable that can test the hypothesis.**

比如：

### 错误做法

因为玩家觉得经济系统无聊：

```
改 resource
改 action
改 VP
改 market
改 turn order
```

然后测试。

结果当然什么都不知道。

### 正确做法

```
Hypothesis:
resource income too abundant

Change:
only income curve

Measure:
decision density
resource contention
```

这是从“AI 会改游戏”走向“AI 会做实验”的关键。

------

# 二十一、一个更完整的 v2 架构

我建议你最终演进到：

```
board-game-design/
│
├── SKILL.md
│
├── workflow.md
├── cheatsheet.md
│
├── reasoning/
│   ├── design-reasoning.md
│   ├── decision-matrix.md
│   ├── hypothesis.md
│   └── intervention.md
│
├── diagnostics/
│   ├── runaway-leader.md
│   ├── first-player-advantage.md
│   ├── dominant-strategy.md
│   ├── analysis-paralysis.md
│   └── ...
│
├── experiments/
│   ├── framework.md
│   ├── experiment-design.md
│   └── metrics.md
│
├── balance/
│   ├── probability-and-balance.md
│   ├── balance-model.md
│   └── value-budget.md
│
├── playtesting.md
│
├── patterns.md
├── glossary.md
│
├── chapters/
│   └── ...
│
├── templates/
│   ├── design-state.md
│   ├── hypothesis.md
│   ├── experiment.md
│   ├── decision.md
│   ├── playtest-log.md
│   ├── iteration.md
│   └── ...
│
└── lint/
    ├── rules.md
    └── checklist.md
```

注意：

**我不建议把所有这些都放到 `SKILL.md`。**

Agent Skills 的当前规范本身就强调：主 `SKILL.md` 负责 instructions，详细 resources 按需加载，并推荐把主体控制在 500 行以内。你目前的渐进式加载设计已经符合这个原则。

------

# 二十二、我建议你重新定义 Skill 的核心 Loop

目前：

```
Concept
↓
Mechanism
↓
Prototype
↓
Playtest
↓
Balance
```

v2：

```
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
Iteration
↺
```

这里最重要的是：

**Mechanism 不再是中心。**

中心变成：

> **Design Decision**

------

# 二十三、整个 Agent 可以设计成 5 种 Mode

我认为这样会非常清晰。

### 1. Create

从零设计。

```
idea
→ design intent
→ mechanism options
→ hypothesis
→ MVP
```

### 2. Diagnose

已有游戏出问题。

```
symptom
→ evidence
→ diagnosis
→ causes
→ intervention options
```

### 3. Experiment

用户已经知道问题，准备验证。

```
hypothesis
→ variant
→ metric
→ test
→ result
```

### 4. Balance

主要解决：

```
economy
probability
VP
curve
tempo
dominant strategy
```

### 5. Prototype

主要负责：

```
rules
components
PnP
versioning
```

这五种 mode 会比单纯按 workflow stage 更符合实际使用。

------

# 二十四、建议加入一个非常重要的“设计对象层”

我建议以后不要只记录文件。

可以定义一些概念对象：

```
DesignGoal
Mechanism
Constraint
Hypothesis
Evidence
Decision
Experiment
Risk
Version
```

它们之间有关系：

```
DesignGoal
    ↓
Mechanism
    ↓
Hypothesis
    ↓
Experiment
    ↓
Evidence
    ↓
Decision
```

比如：

```
Goal:
high player interaction

Mechanism:
worker placement

Risk:
blocking frustration

Hypothesis:
limited blocking increases interaction without increasing frustration

Experiment:
compare 3 vs 5 worker spaces

Evidence:
...

Decision:
keep 3 spaces
```

这是以后如果你想做真正的工具化产品，非常重要的基础。

------

# 二十五、可执行改进计划

我建议不要一次性大重构。

按照下面四个版本迭代最稳。

------

## Phase 1 — v1.1：Design State

### 目标

解决：

> AI 不知道“现在这个游戏已经决定了什么”。

### 新增

```
templates/design-state.md
```

内容：

```
Project Status

Locked Decisions
Open Questions
Current Hypotheses
Known Risks
Rejected Ideas
Recent Evidence
Next Experiment
```

### 修改

```
SKILL.md
```

加入：

```
For an existing game project:
1. Read design-state.md first.
2. Do not reopen locked decisions unless new evidence contradicts them.
3. Update design-state.md after consequential decisions.
```

### 修改

```
workflow.md
```

把：

> Stage

改成：

> Stage + State.

### 成功标准

Agent 在第 10 次设计对话时仍然能够回答：

> “我们目前已经确定什么？”

而不是重新从头设计。

------

# 二十六、Phase 2 — v1.2：Hypothesis + Experiment

### 新增

```
reasoning/
experiments/
templates/hypothesis.md
templates/experiment.md
```

要求：

任何非 trivial design change 必须有：

```
Observed Problem
Hypothesis
Change
Expected Effect
Metric
Decision Rule
```

### 成功标准

Agent 不再只给：

> “我建议把资源从 5 改成 4。”

而给：

> “我建议先把资源从 5 改到 4，因为假设是供给过剩导致竞争不足；下一轮观察 resource contention 与玩家计划改变次数。”

------

# 二十七、Phase 3 — v1.3：Diagnosis + Linter

### 新增

```
diagnostics/
lint/
```

### 第一批只做 8 个

我推荐：

1. Runaway Leader
2. Dominant Strategy
3. First Player Advantage
4. Analysis Paralysis
5. Low Agency
6. Kingmaking
7. Endgame Drag
8. Randomness Dominates Skill

不要一开始做 30 个。

### 每个 diagnosis 都统一 schema

```
Symptom
Evidence
Possible Causes
Diagnostic Questions
Candidate Interventions
Experiment
Success Criteria
```

------

# 二十八、Phase 4 — v2.0：Design Engine

这是大的版本。

### 新增：

```
design reasoning
decision matrix
balance model
value budget
iteration history
```

### Agent 行为升级为：

```
Observe
→ Model
→ Diagnose
→ Generate Options
→ Compare
→ Select
→ Prototype
→ Test
→ Analyze
→ Update State
```

到这个阶段，Skill 的定位就已经从：

> Board Game Design Knowledge Skill

真正变成：

> **Board Game Design & Prototyping Agent**

------

# 二十九、一个我非常推荐的最终工作模式

当用户说：

> “帮我设计一个关于火星殖民的工人放置游戏。”

Agent 不应该直接开始生成规则。

应该：

```
1. Identify intent
2. Identify target experience
3. Identify constraints
4. Generate 2–4 mechanism architectures
5. Compare trade-offs
6. Choose a provisional architecture
7. Record hypothesis
8. Generate mechanism skeleton
9. Build minimal paper prototype
```

------

当用户说：

> “游戏玩了三次，感觉后期越来越无聊。”

Agent：

```
1. Diagnose symptom
2. Ask / infer evidence
3. Identify possible causes
4. Choose highest-value hypothesis
5. Propose minimal intervention
6. Record experiment
7. Define success criteria
```

------

当用户说：

> “我觉得这张卡太强。”

Agent：

```
1. Quantify value
2. Compare alternatives
3. Check economy impact
4. Check tempo
5. Check compounding
6. Identify whether problem is local or systemic
```

------

# 三十、你现在最应该避免的一个陷阱

这个项目非常容易掉进：

> **知识越来越多，但 Agent 越来越笨。**

也就是：

```
13 chapters
→ 20 chapters
→ 30 chapters
→ 50 chapters
→ 100 patterns
```

最终 Agent 每次都要在知识里寻找“有什么机制可以用”。

这不一定越来越强。

你的下一个阶段应该是：

```
Knowledge ↑   少量
Reasoning ↑↑
State ↑↑↑
Evidence ↑↑↑
Experiment ↑↑↑
```

换句话说：

> **v1 解决“知道桌游怎么设计”；v2 要解决“知道为什么这样改”。**

------

# 三十一、最终优先级

如果只能做 5 件事，我建议严格按这个顺序：

| 优先级 | 改进                         |  价值 | 工作量 |
| ------ | ---------------------------- | ----: | -----: |
| P0     | `design-state.md`            | ★★★★★ |     低 |
| P0     | Hypothesis / Experiment      | ★★★★★ |     中 |
| P1     | Diagnosis framework          | ★★★★★ |     中 |
| P1     | Game Design Linter           | ★★★★½ |     中 |
| P2     | Balance Model / Value Budget |  ★★★★ |   中高 |
| P2     | Decision Matrix              |  ★★★★ |     低 |
| P3     | 更多 mechanism chapters      |    ★★ |     高 |
| P3     | Digital prototype tooling    |    ★★ |     高 |

所以：

**先别扩知识库。**

------

# 三十二、我的最终评价

我现在对这个项目的定位会稍微调整一下。

当前版本：

> **A very good mechanism-oriented board-game design skill with a practical PnP workflow.**

理想的下一版本：

> **An evidence-driven board-game design agent that helps users create, prototype, diagnose, test, balance, and iteratively refine tabletop games.**

这两者其实是很大的跃迁。

而且非常值得做，因为你的基础已经足够好：你已经有 mechanism taxonomy、decision cheat sheet、playtest framework、balance failure modes，以及从 concept 到 PnP 的 artifact workflow。

真正欠缺的是把这些东西用一条“因果链”串起来：

**Intent → Decision → Hypothesis → Experiment → Evidence → Diagnosis → Decision**

这条链一旦建立，你这个 Skill 的能力层级会发生质变。

另外，从 Agent Skills 标准本身来看，你目前采用的 `SKILL.md + references/resources + templates` 架构是正确方向；标准明确建议把详细内容拆到按需加载资源中，而不是把所有知识塞进入口文件。

### 我建议的下一步

下一步最值得直接落地的，不是继续讨论架构，而是**按照上面的 Phase 1 + Phase 2，给你现有 repo 做一次具体的 v1.1/v1.2 文件级改造设计**：我可以直接列出每一个新增/修改文件、完整目录树、`design-state.md` / `hypothesis.md` / `experiment.md` 的字段设计，以及应该如何修改现有 `SKILL.md`、`workflow.md`、`playtesting.md` 和 `mechanism-skeleton.md` 的具体规则。