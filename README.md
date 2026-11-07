<a id="top"></a>

# X + 公众号长文爆款标题 Skill

**先读正文，再给 3–5 个真正不同的角度；每条标明正文在哪里兑现，由作者来选。不改事实、不造独家、不预测点击率、不自动发布。**

An Agent Skill for headlines of Chinese long-form articles on X Articles and WeChat Official Accounts: evidence first, 3–5 ranked options, the author decides.

[中文](#zh) | [English](#en)

---

<a id="zh"></a>

## 中文

### 目录

- [一句话介绍](#zh-intro)
- [它和直接问 AI 有什么不同](#zh-diff)
- [适合 / 不适合](#zh-fit)
- [安装](#zh-install)
- [用法](#zh-usage)
- [示例](#zh-example)
- [工作流：5 步 11 项能力](#zh-workflow)
- [明确不做的事](#zh-no)
- [目录结构](#zh-structure)
- [致谢与借鉴来源](#zh-credits)
- [作者](#zh-author)
- [许可](#zh-license)

<a id="zh-intro"></a>
### 一句话介绍

给 X Article 和公众号长文拟标题的 Agent Skill。这里的「爆款」指**值得点开、且点开后正文确实兑现**的标题，而不是更劲爆的措辞：先锁定已定稿标题、提炼核心问题与证据，再从角度库出候选，经三项检查后排序交给作者选择，最后把确认的偏好记进标题库。

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用本 skill |
|---|---|
| 一次给 20–30 个，大多是同一句式换词 | 3–5 个，每个是不同的读者问题 |
| 为了吸睛，补出正文没有的数字、"独家"、危机感 | 每条标出正文兑现位置；事实口径不清就不用 |
| 看不出哪个会在手机上被截断 | 对象和问题前置；未实机预览就标「待实机预览」 |
| 满屏"赋能、炸了、彻底颠覆" | 朗读检查，删空口号、黑话和新闻腔 |
| 顺手把你定好的标题也"优化"了 | 已定稿标题逐字保留，只提示风险 |
| 给出"预计点击率 +30%" | 不预测点击率，只做编辑判断 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 写案例复盘、行业分析、产品观察等中文长文，发在 X Article 或公众号
- 已有全文，想要几个不同角度的标题来选
- 已有候选或定稿标题，想做一次事实与兑现检查

**不适合**
- 没有正文，只想批量生成大量标题
- 希望标题比正文更夸张，或加入正文没有的事实
- 需要点击率预测、自动 A/B 投放或自动发布

<a id="zh-install"></a>
### 安装

把本仓库克隆到你所用 Agent 工具的 skills 目录（具体路径以该工具的文档为准），例如：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/X-title-skill.git x-title-skill
```

目录名建议与 `SKILL.md` 中的 `name: x-title-skill` 保持一致。本 skill 是纯文本说明，不需要安装依赖、API Key 或联网接口。

<a id="zh-usage"></a>
### 用法

```text
用 x-title-skill 帮我给这篇文章拟标题。
平台：公众号 + X Article
目标读者：___
现有标题：___（已定稿 / 未定稿）
正文：___
```

只做检查时：

```text
用 x-title-skill 检查这个标题是否被正文兑现、有没有事实口径问题：「___」
正文：___
```

<a id="zh-example"></a>
### 示例

> 以下案例**全部虚构**，只展示输出格式。完整流程见 [references/examples.md](references/examples.md)。

核心问题：A 笔记怎样让个人免费用户把产品带进团队，并变成团队订阅？
不承诺：不是唯一增长来源；不保证可复制。

| # | 角度 | 候选标题 | 正文兑现 | 三检与风险 |
|---|---|---|---|---|
| 1 | 具体机制 | A 笔记怎样让免费用户把它带进团队？ | §2–§4 | 通过；待实机预览 |
| 2 | 路径复盘 | 从个人笔记到团队订阅，A 笔记改了哪一步？ | §3 | 通过；偏重 §3 |
| 3 | 选择理由 | 团队管理员为什么愿意为 A 笔记付费？ | §4 | 待改：访谈仅 3 人 |

推荐第 1 条：最贴近全文总论，对象与问题都在前半段。请作者选择。

<a id="zh-workflow"></a>
### 工作流：5 步 11 项能力

| 步骤 | 能力 | 产出 |
|---|---|---|
| 1. 读稿，锁定定稿标题 | ① 输入解析与标题锁 | 输入状态；已定稿标题逐字保留；只有摘要时标「方向草案」 |
| 2. 核心问题与证据 | ② 核心问题与证据提炼 | 一句话核心问题、"不承诺什么"、证据表 |
| 3. 角度库出候选 | ③ 角度筛选 ④ 候选生成 | 3–5 个适用角度、每角度 1 条候选；跳过的写原因 |
| 4. 三检 | ⑤ 正文兑现 ⑥ 事实口径 ⑦ 手机截断与平台 ⑧ 去 AI 味 | 每条"通过/待改/淘汰＋原因" |
| 5. 排序给作者选 | ⑨ 质量排序与异议复审 ⑩ 输出与确认 | 3–5 条排序表、推荐与取舍；停在确认点 |
| 收尾 | ⑪ 标题库反馈学习 | 作者确认后记一行：最终标题、否决原因、真实数据（没有就写待补充） |

详细规则见 [SKILL.md](SKILL.md)。

<a id="zh-no"></a>
### 明确不做的事

- 改动事实、夸大范围或因果
- 假独家、假实测、假内部消息、假时效
- 堆量生成（超过 5 条正式候选）
- 点击率 / 打开率预测、伪精确评分
- 自动发布、自动写入草稿箱、自动 A/B 投放
- 擅自修改已定稿标题

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                         # 主流程（name/description frontmatter）
references/
  angle-library.md               # 角度库：适用/不适用、正反例
  three-checks.md                # 三检清单 + 去 AI 味词表 + 编辑维度
  examples.md                    # 公开媒体标题观察 + 完整虚构演示
templates/
  output-template.md             # 交付模板
  title-feedback-log.md          # 标题库反馈表（含 CSV 表头）
scripts/
  validate.py                    # 检查 frontmatter 与必需文件
.github/workflows/ci.yml         # CI：运行 validate.py
CHANGELOG.md
LICENSE
```

<a id="zh-credits"></a>
### 致谢与借鉴来源

本项目在编写前调研了以下公开仓库（许可状态按 2026-11-07 GitHub API 返回值记录）。**只借鉴思路，所有文字、分类、骨架和例句均为本项目重新编写**；许可未识别的仓库未复制任何原文。仓库星数不代表方法有效。

| 来源 | 许可 | 借鉴了什么 | 没有采用 |
|---|---|---|---|
| [BigPengSays/bigpeng-hot-gzh](https://github.com/BigPengSays/bigpeng-hot-gzh) | MIT | 模块化流程、不同结构而非同义替换、标题承诺逐项落到正文、关键信息前置的截断意识 | 默认 6 条、自动补全身份、默认速成/情绪词 |
| [itwanger/toBeBetterJavaer · title-generator（固定提交）](https://github.com/itwanger/toBeBetterJavaer/blob/d602717b7c579f3a8c25bde178ebc29b5b13f942/.claude/skills/title-generator/SKILL.md) | 未识别 | 先读全文、证据锚点、先筛模板是否适合（思路） | 固定句式填槽、强制情绪锚点、历史打开率数据 |
| [Namtanmk/Claude-Skills-Ultimate-Bundle · headline-generator](https://github.com/Namtanmk/Claude-Skills-Ultimate-Bundle/blob/main/Content%20%26%20Copywriting/headline-generator/SKILL.md)（文件作者字段 matthewhitcham） | 未识别 | 输入简报、清晰/具体/好奇心检查维度、按偏好局部重做（思路） | 25+ 条、点击唯一目标、英文 SEO 字数限制 |
| [realkimbarrett/advertising-skills · headline-matrix](https://github.com/realkimbarrett/advertising-skills/blob/main/skills/copy-chief/headline-matrix/SKILL.md) | 未识别 | 角度矩阵思路 | 广告式紧迫感、默认 25 条 |
| [redfox-data/redfox-community · wechat-title](https://github.com/redfox-data/redfox-community/blob/main/skills/wechat-title/SKILL.md) | 未识别 | 样本须注明来源与时间窗、数据不足如实说明（思路） | 外部接口与 API Key 依赖、固定匹配指数 |
| [aaaronmiller/create-viral-content](https://github.com/aaaronmiller/create-viral-content) | 未识别 | 多读者视角复审、平台适配意识（思路） | 英文 AI 腔词表、未经核验的算法与比例断言 |
| [majiabin2020/xinzhiyuan-title-craft](https://github.com/majiabin2020/xinzhiyuan-title-craft) | MIT | 仅作反面检查：时间压缩、制造危机、添加原文没有的信息等写法列入禁区 | 主体方法均未采用 |

公开媒体标题引例来自 APPSO 公众号在 [今天看啥](https://www.jintiankansha.com/column/vkfaNCM6Dc) 的公开镜像列表与 [爱范儿官网作者档案](https://www.ifanr.com/author/appso)，仅少量逐字引用用于说明结构，版权归原作者；本项目不背书其中事实，也没有阅读/热度数据。

<a id="zh-author"></a>
### 作者

华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者。

<a id="zh-license"></a>
### 许可

本项目禁止商业用途；个人学习与非商业使用可免费使用。未经作者事先书面许可，不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道。如需转载或授权，请通过 GitHub 联系 @huaxialucaicaizi。详见 [LICENSE](LICENSE)。

[↑ 返回顶部](#top)

---

<a id="en"></a>

## English

**What it is.** An Agent Skill for writing headlines for Chinese long-form articles on X Articles and WeChat Official Accounts. "Viral" here means *worth clicking and actually delivered by the body*, not louder wording.

**Workflow (5 steps, 11 capabilities).**
1. Read the draft and lock any final title (input parsing, title lock).
2. State one core question and build an evidence table (core question & evidence).
3. Pick 3–5 fitting angles from the angle library and draft one candidate each (angle selection, candidate drafting).
4. Run three checks: body delivery, factual scope/metrics, mobile truncation + de-AI wording (checks 5–8).
5. Rank and hand 3–5 options to the author, then stop (ranking & objection review, output & confirmation).
Afterwards: log the confirmed choice and rejection reasons in a title log (feedback learning); performance data only if the author provides real numbers.

**Out of scope.** Changing or exaggerating facts, fake exclusives, mass generation, click-through prediction, auto-publishing.

**Install.** Clone this repo into your agent tool's skills directory, e.g. `~/.agents/skills/x-title-skill`. No dependencies or API keys.

**Credits.** See the table in the Chinese section. Ideas only; no text copied from repositories without an identified license.

**Author.** 华夏路菜菜子: former AI product growth at a major tech company, now an AI founder.

**License.** Non-commercial. Without prior written permission, you may not list, include, or distribute this project on any third-party AI product, skill store, or similar channel. Contact @huaxialucaicaizi on GitHub. See [LICENSE](LICENSE).

[↑ Back to top](#top)
