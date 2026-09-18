# Central Agent Skills Hub (AI Agent 专业技能中央索引库)

> 工业级多 Agent 架构核心规范库，为 Google Antigravity、Claude Desktop、Cursor 等现代智能体系统提供全生命周期研发技能底座。

---

## 🌟 技能全景索引 (Categorized Skills Registry)

### 🛠️ 1. 技能元治理 (Meta Governance)
*专司技能生命周期管理、规范脚手架生成、安全合规审查与跨环境自动建仓发布。*

| 技能标识 (Skill Name) | 核心职责与规范重点 | GitHub 源码仓库 |
| :--- | :--- | :--- |
| `skill-manager` | 技能全生命周期管理、规范脚手架生成、脱敏合规审查与跨环境自动建仓同步 | [查看仓库](https://github.com/Garfield247/agent-skill-manager) |

---

### 🚀 2. 研发生命周期通用能力 (Engineering Lifecycle Superpowers)
*覆盖软件工程全链路：从代码逆向、方案设计、Bug 排查，到版本提交与文档资产沉淀。*

| 技能标识 (Skill Name) | 领域定位 | 核心职责与规范重点 | GitHub 源码仓库 |
| :--- | :--- | :--- | :--- |
| `codebase-reconnaissance` | 🧭 代码勘测与逆向 | 宏观摸骨五步法、五级代码检索武器库 (fd/rg/ast-grep/LSP/Repo-Map/Git 考古) 与 ARCH_RECON 全景卡片沉淀 | [查看仓库](https://github.com/Garfield247/agent-skill-codebase-reconnaissance) |
| `technical-design` | 📐 方案设计与 TDD | 方案先行与审阅确认、苏格拉底式需求收敛、微任务自动化检验命令与完成前铁证门禁 | [查看仓库](https://github.com/Garfield247/agent-skill-technical-design) |
| `systematic-debugging` | 🔍 排障与根因剖析 | 排障五步法、根因机理深度剖析 (RCA)、完成前铁证门禁、杜绝盲改与静默兜底、高价值避坑档案 | [查看仓库](https://github.com/Garfield247/agent-skill-systematic-debugging) |
| `git-workflow-mastery` | 🌿 Git 工作流治理 | 完成即提交、Conventional Commits 中文原子提交、分支治理、变基冲突化解与 .gitignore 分类治理 | [查看仓库](https://github.com/Garfield247/agent-skill-git-workflow) |
| `project-documentation` | 📚 文档与知识资产 | 目录自适应探测、00 号标准约束、Diátaxis 四象限架构、MADR 决策记录与 Mermaid 防崩规范 | [查看仓库](https://github.com/Garfield247/agent-skill-project-documentation) |

---

### 💻 3. 核心语言与微服务框架栈 (Language & Framework Stacks)
*聚焦于主流后端主力语言地道开发规范、代码封装六大原则、pkg/common 基础分层与微服务架构治理。*

| 技能标识 (Skill Name) | 语言 / 框架 | 核心职责与规范重点 | GitHub 源码仓库 |
| :--- | :--- | :--- | :--- |
| `golang-base` | 🐹 Go 基础通用 | 地道 Go 开发规范、代码封装六原则、pkg 基础层分层收紧与 *x 扩展工具包、指针内存语义、时间与 iota 枚举设计 | [查看仓库](https://github.com/Garfield247/agent-skill-golang-base) |
| `go-zero-development` | ⚡ Go / 微服务 | goctl 契约边界、API/RPC 设计、Handler/Logic/Model 四层分层、统一响应与错误码、并发 Panic 拦截、分布式锁与优雅停机 | [查看仓库](https://github.com/Garfield247/agent-skill-go-zero) |
| `python-base` | 🐍 Python 基础通用 | Python 3.10+ 原生类型、代码封装六原则、common 基础层分层收紧与 *x 扩展工具包、不可变常量枚举、流式防 OOM | [查看仓库](https://github.com/Garfield247/agent-skill-python-base) |
| `python-fastapi` | 🚀 Python Web API | Async/Await 防阻塞黄金法则、统一响应包装、BaseBusinessException 业务异常拦截 (拒 500)、Pydantic v2 与异步 Session | [查看仓库](https://github.com/Garfield247/agent-skill-python-fastapi) |
| `python-crawler` | 🕷 Python 爬虫逆向 | 协议逆向优先、httpx 异步连接池与限流、Playwright 拦截优化、TLS/JA3 指纹伪装与强制 Docstring 契约样例 | [查看仓库](https://github.com/Garfield247/agent-skill-python-crawler) |
| `python-scripting` | 💻 Python 运维脚本 | Typer 现代 CLI、安全 Subprocess 调度 (严禁 shell=True, 显式 timeout)、pathlib 流式 I/O、Linux 标准退出码语义 | [查看仓库](https://github.com/Garfield247/agent-skill-python-scripting) |
| `hyperf-framework` | 🐘 PHP 协程微服务 | Controller->DTO->Service->Repository 四层分层、Swoole 协程常驻内存安全 (Hyperf\Context\Context)、PHP 8 原生 Attribute 注解、N+1 杜绝、队列幂等 | [查看仓库](https://github.com/Garfield247/agent-skill-hyperf-framework) |

---

### 🗄️ 4. 基础设施与中间件存储架构 (Infrastructure & Middlewares)
*关系型数据库、高性能分布式内存缓存与可靠消息事件驱动基石。*

| 技能标识 (Skill Name) | 中间件领域 | 核心职责与规范重点 | GitHub 源码仓库 |
| :--- | :--- | :--- | :--- |
| `mysql-mastery` | 🐬 关系型数据库 | InnoDB 建表规约 (强制 utf8mb4/NOT NULL/无符号自增主键)、最左前缀覆盖索引、EXPLAIN 调优、间隙锁死锁防范、深分页延迟关联与大表无锁 DDL | [查看仓库](https://github.com/Garfield247/agent-skill-mysql-mastery) |
| `redis-mastery` | ⚡ 高并发缓存协调 | Key 冒号命名与强 TTL 约束、BigKey/HotKey 治理与禁用清单 (禁 KEYS/FLUSHALL)、缓存三灾难终结方案、双写一致性、原子 Lua 分布式锁 | [查看仓库](https://github.com/Garfield247/agent-skill-redis-mastery) |
| `rabbitmq-mastery` | 🐇 消息中间件解耦 | Connection 单例复用与 Channel 隔离、零丢失闭环 (Confirm + 3层持久化 + 手动 Ack)、QoS 背压限流、死信 DLX 与消费幂等防重 | [查看仓库](https://github.com/Garfield247/agent-skill-rabbitmq-mastery) |

---

## 🏛️ 多 Agent 架构规范兼容性

本索引库下的所有技能，均严格遵循 Antigravity IDE、Claude Desktop、Cursor Rules 与 Multi-Agent 标准协议：
1. **双重兼容结构**：每个技能均包含根目录权威 `SKILL.md`（带标准 YAML frontmatter）与 `skills/<skill_name>/SKILL.md` 双重兼容结构；
2. **脱敏合规审查**：代码与文档保持标准技术术语，严禁泄露内部敏感信息；
3. **开源授权**：全库统一采用宽松友好的 MIT License。
