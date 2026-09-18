# Central Agent Skills Hub (AI Agent 专业技能中央索引库)

> 工业级多 Agent 架构核心规范库，为 Google Antigravity、Claude Desktop、Cursor 等现代智能体系统提供全生命周期研发技能底座。

## 🌟 技能全景索引 (Skills Registry)

| 技能唯一标识 (Skill Name) | 类别与领域 | 核心职责与规范重点 | GitHub 源码仓库 |
| :--- | :--- | :--- | :--- |
| `skill-manager` | 🛠 技能元治理 | 技能生命周期管理、脚手架规范生成、敏感合规脱敏审查与跨环境自动建仓同步 | [查看](https://github.com/Garfield247/agent-skill-manager) |
| `codebase-reconnaissance` | 🧭 代码勘测与逆向检索 | 摸骨五步法、五级代码检索武器库 (fd/rg/ast-grep/LSP/Repo-Map/Git 考古) 与 ARCH_RECON 全景沉淀 | [查看](https://github.com/Garfield247/agent-skill-codebase-reconnaissance) |
| `technical-design` | 📐 前期程序设计 | 方案先行与审阅确认、苏格拉底式需求收敛、微任务自动化检验命令与完成前铁证门禁 | [查看](https://github.com/Garfield247/agent-skill-technical-design) |
| `systematic-debugging` | 🔍 排障与根因分析 | 系统化排障五步法、根因机理剖析 (RCA)、完成前铁证门禁、杜绝盲改与静默兜底、高价值避坑档案 | [查看](https://github.com/Garfield247/agent-skill-systematic-debugging) |
| `git-workflow-mastery` | 🌿 Git 研发流治理 | 完成即提交、Conventional Commits 中文原子提交、分支治理、变基冲突化解与 .gitignore 分类治理 | [查看](https://github.com/Garfield247/agent-skill-git-workflow) |
| `project-documentation` | 📚 项目文档与知识管理 | 目录自适应探测、00 号标准约束、Diátaxis 四象限、MADR 架构决策、Post-Mortem 案例与 Mermaid 防崩 | [查看](https://github.com/Garfield247/agent-skill-project-documentation) |
| `golang-base` | 🐹 Go 基础通用规范 | 地道 Go 开发规范、代码封装六原则、pkg 基础层分层收紧与 *x 扩展工具包、指针内存语义、时间/枚举规范 | [查看](https://github.com/Garfield247/agent-skill-golang-base) |
| `go-zero-development` | ⚡ Go / 微服务架构 | goctl 契约边界、API/RPC 设计、Handler/Logic/Model 四层分层、统一响应与错误码、并发 Panic 拦截、分布式锁 | [查看](https://github.com/Garfield247/agent-skill-go-zero) |
| `python-base` | 🐍 Python 基础通用规范 | Python 3.10+ 原生类型、代码封装六原则、common 基础层分层收紧与 *x 扩展工具包、不可变常量枚举、流式防 OOM | [查看](https://github.com/Garfield247/agent-skill-python-base) |
| `python-fastapi` | 🚀 Python Web API | Async/Await 防阻塞黄金法则、统一响应包装、BaseBusinessException 全局业务异常拦截 (拒 500)、Pydantic v2 | [查看](https://github.com/Garfield247/agent-skill-python-fastapi) |
| `python-crawler` | 🕷 Python 网络爬虫 | 协议逆向优先、httpx 异步连接池与限流、Playwright 拦截优化、TLS/JA3 指纹伪装与强制 Docstring 样例 | [查看](https://github.com/Garfield247/agent-skill-python-crawler) |
| `python-scripting` | 💻 Python 自动化脚本 | Typer 现代 CLI、安全 Subprocess 调度 (严禁 shell=True, 显式 timeout)、pathlib 流式 I/O、Linux 退出码 | [查看](https://github.com/Garfield247/agent-skill-python-scripting) |

---

## 🏛️ 多 Agent 架构规范兼容性

本索引库下的所有技能，均严格遵循 Antigravity IDE、Claude Desktop、Cursor Rules 与 Multi-Agent 标准协议：
1. **根目录规范**：每个技能均包含权威 `SKILL.md`（带标准 YAML frontmatter）与 `skills/<skill_name>/SKILL.md` 双重兼容结构；
2. **脱敏合规审查**：严禁出现敏感业务或网络字样，统一使用通用的“机房/物理机房/真机设备”等技术术语；
3. **开源授权**：全库统一采用宽松友好的 MIT License。
