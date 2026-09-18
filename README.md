# agent-skills (Garfield's Agent Skills Hub)

> 🌟 Garfield 的 AI Agent 研发工程技能索引总览中心 (Awesome Agent Skills Hub) 与一键环境同步分发工具链。
> 原生适配 **Google Antigravity / Gemini Code Assist**、**Anthropic Claude (Claude Code / Projects)**、**Cursor / Codex / GitHub Copilot** 等主流现代 Agentic IDE。

---

## 📚 技能全景索引目录 (Skills Registry)

本中心收录了涵盖**前期架构设计、规范编码、全生命周期排错、Git 流转与知识管理**的全套独立专业技能库：

| 分类 | 技能名称 (GitHub 仓库) | 职责与规范重点 | 推荐本地目录 |
| :--- | :--- | :--- | :--- |
| 🧭 **元管理** | [agent-skill-manager](https://github.com/Garfield247/agent-skill-manager) | **技能管理与元治理**：主流与黑马对标调研（拒闭门造车）、规范脚手架创建、脱敏合规审查、中央索引自动同步。 | `skills/skill-manager` |
| 🏛️ **方案设计** | [agent-skill-technical-design](https://github.com/Garfield247/agent-skill-technical-design) | **前期架构设计 (TDD/RFC)**：方案先行与审阅确认、**苏格拉底式需求收敛**、**微任务自动化检验命令**、**完成前铁证门禁**、严禁静默重试/兜底、LaTeX 推导。 | `skills/technical-design` |
| 🩺 **排障诊断** | [agent-skill-systematic-debugging](https://github.com/Garfield247/agent-skill-systematic-debugging) | **系统化 Bug 深度排查**：排障五步法 SOP、根因剖析 (RCA)、**完成前铁证验证门禁**、**红绿灯测试硬门禁 (Failing Test First)**、严禁盲改与静默兜底。 | `skills/systematic-debugging` |
| 🛠 **协作流转** | [agent-skill-git-workflow](https://github.com/Garfield247/agent-skill-git-workflow) | **Git 全生命周期研发工作流**：完成即提交、Conventional Commits 中文原子提交、分支治理、变基冲突化解、`.gitignore` 四分类动态维护。 | `skills/git-workflow-mastery` |
| 📚 **知识管理** | [agent-skill-project-documentation](https://github.com/Garfield247/agent-skill-project-documentation) | **人机双重视角文档体系**：目录自适应探测、**00 号标准与红线第一法则**、**Diátaxis 四象限**、**MADR 决策记录**、**高价值避坑档案**、**Mermaid 4 大防崩铁律**。 | `skills/project-documentation` |
| ⚡ **语言底座** | [agent-skill-golang-base](https://github.com/Garfield247/agent-skill-golang-base) | **地道 Go 语言核心开发规范**：**代码封装原则**、**pkg 一层收紧二层按需嵌套**、**`*x` 扩展工具包 (slicex/mapx/stringx/timex)**、**Uber Go 指针与内存语义**。 | `skills/golang-base` |
| 🐍 **语言底座** | [agent-skill-python-base](https://github.com/Garfield247/agent-skill-python-base) | **Python 3.10+ 现代基础规范**：**不可变常量与枚举 (Final/StrEnum)**、**时间格式化常量规范**、PEP 604 类型、可变默认参数避坑与流式防 OOM。 | `skills/python-base` |
| ⚡ **后端服务** | [agent-skill-go-zero](https://github.com/Garfield247/agent-skill-go-zero) | **Go & go-zero 高性能微服务**：goctl 契约生成边界、Handler/Logic/Model 四层分层、统一响应与错误码、并发 Panic 拦截、Redis 缓存与专属排障武器库。 | `skills/go-zero-development` |
| 🚀 **后端服务** | [agent-skill-python-fastapi](https://github.com/Garfield247/agent-skill-python-fastapi) | **Python 3.10+ & FastAPI Web API**：Async/Await 防阻塞黄金法则、统一响应包装、BaseBusinessException 全局业务异常拦截 (拒 500)、Pydantic v2 与专属排障武器库。 | `skills/python-fastapi` |
| 🕷 **采集逆向** | [agent-skill-python-crawler](https://github.com/Garfield247/agent-skill-python-crawler) | **Python 3.10+ 网络爬虫与逆向**：协议逆向优先、httpx 异步连接池与限流、Playwright 资源拦截优化、强制 Docstring 携带 Request/Response 样例红线。 | `skills/python-crawler` |
| ⚙️ **自动化运维** | [agent-skill-python-scripting](https://github.com/Garfield247/agent-skill-python-scripting) | **Python 3.10+ 运维脚本与 CLI**：Typer 现代 CLI、安全 Subprocess 调度 (严禁 shell=True, 显式 timeout)、pathlib 与流式 I/O 防 OOM、Linux 标准退出码。 | `skills/python-scripting` |

---

## 📦 多平台 Agent 一键安装与使用指南 (Multi-Agent Guide)

克隆索引中心仓库后，可通过内置的 `sync_skills.py` 脚本一键同步分发至不同的智能体开发环境：

```bash
git clone git@github.com:Garfield247/agent-skills.git
cd agent-skills
```

### 1. Google Antigravity / Gemini Code Assist
- **一键同步全量技能至全局环境**：
  ```bash
  python3 sync_skills.py --agent gemini
  # 自动同步至 ~/.gemini/config/skills/
  ```

### 2. Anthropic Claude (Claude Code / Claude Desktop)
- **一键同步至 Claude Code (CLI) 全局技能库**：
  ```bash
  python3 sync_skills.py --agent claude
  # 自动同步至 ~/.claude/skills/
  ```
- **项目级使用**：在项目根目录的 `CLAUDE.md` 中引用即可生效。
- **Claude Projects (Web 客户端)**：可将对应技能的 `SKILL.md` 直接上传至项目的 **Project Knowledge**。

### 3. Cursor / Codex / GitHub Copilot
- **一键同步至当前项目的 Cursor 规则库**：
  ```bash
  cd /path/to/your-project
  python3 /path/to/agent-skills/sync_skills.py --agent cursor
  # 自动克隆至当前项目的 .cursor/rules/ 目录
  ```
- **GitHub Copilot / Codex**：
  将所需的 `SKILL.md` 规范注入项目的 `.github/copilot-instructions.md` 即可。

### 4. 项目工作区通用加载
```bash
cd /path/to/your-project
python3 /path/to/agent-skills/sync_skills.py --agent local
# 自动同步至当前项目的 .agents/skills/ 目录
```

---

## 📄 开源协议 (License)
本项目采用 [MIT License](LICENSE) 授权。
