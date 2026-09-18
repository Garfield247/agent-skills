# agent-skills (Garfield's Agent Skills Hub)

> 🌟 Garfield 的 AI Agent 研发工程技能索引总览中心 (Awesome Agent Skills Hub) 与一键环境同步分发工具链。
> 适配 Google Antigravity、Gemini Code Assist、Claude、Cursor 等主流现代 Agentic IDE。

---

## 📚 技能全景索引目录 (Skills Registry)

本中心收录了涵盖**前期架构设计、规范编码、全生命周期排错、Git 流转与知识管理**的全套独立专业技能库：

| 分类 | 技能名称 (GitHub 仓库) | 职责与规范重点 | 本地加载路径 |
| :--- | :--- | :--- | :--- |
| 🧭 **元管理** | [agent-skill-manager](https://github.com/Garfield247/agent-skill-manager) | **技能管理与元治理**：Skill 规范脚手架创建、脱敏合规审查、中央索引自动同步。 | `skills/skill-manager` |
| 🏛️ **方案设计** | [agent-skill-technical-design](https://github.com/Garfield247/agent-skill-technical-design) | **前期程序设计 (TDD/RFC)**：方案先行与审阅确认、需求模糊 2-3 个确认点、严禁静默重试/兜底、LaTeX 公式推导、ER 建模与 FSM 闭环。 | `skills/technical-design` |
| 🩺 **排障诊断** | [agent-skill-systematic-debugging](https://github.com/Garfield247/agent-skill-systematic-debugging) | **系统化 Bug 深度排查**：排障五步法 SOP、根因剖析 (RCA)、严禁盲改代码、严禁静默兜底、最小破坏性原子修复与回归闭环。 | `skills/systematic-debugging` |
| 🛠 **协作流转** | [agent-skill-git-workflow](https://github.com/Garfield247/agent-skill-git-workflow) | **Git 全生命周期研发工作流**：完成即提交、Conventional Commits 中文原子提交、分支治理、变基冲突化解、`.gitignore` 四分类动态维护。 | `skills/git-workflow-mastery` |
| 📚 **知识管理** | [agent-skill-project-documentation](https://github.com/Garfield247/agent-skill-project-documentation) | **人机双重视角文档体系**：目录自适应探测、面向工程师业务设计 + 面向 AI 上下文地图架构、分类治理、**Mermaid 4 大防崩语法铁律**。 | `skills/project-documentation` |
| ⚡ **后端服务** | [agent-skill-go-zero](https://github.com/Garfield247/agent-skill-go-zero) | **Go & go-zero 高性能微服务**：goctl 契约生成边界、Handler/Logic/Model 四层分层、统一响应与错误码、并发 Panic 拦截、Redis 缓存与专属排障武器库。 | `skills/go-zero-development` |
| 🚀 **后端服务** | [agent-skill-python-fastapi](https://github.com/Garfield247/agent-skill-python-fastapi) | **Python 3.10+ & FastAPI Web API**：Async/Await 防阻塞黄金法则、统一响应包装、BaseBusinessException 全局业务异常拦截 (拒 500)、Pydantic v2 与专属排障武器库。 | `skills/python-fastapi` |
| 🕷 **采集逆向** | [agent-skill-python-crawler](https://github.com/Garfield247/agent-skill-python-crawler) | **Python 3.10+ 网络爬虫与逆向**：协议逆向优先、httpx 异步连接池与限流、Playwright 资源拦截优化、强制 Docstring 携带 Request/Response 样例红线。 | `skills/python-crawler` |
| ⚙️ **自动化运维** | [agent-skill-python-scripting](https://github.com/Garfield247/agent-skill-python-scripting) | **Python 3.10+ 运维脚本与 CLI**：Typer 现代 CLI、安全 Subprocess 调度 (严禁 shell=True, 显式 timeout)、pathlib 与流式 I/O 防 OOM、Linux 标准退出码。 | `skills/python-scripting` |

---

## ⚡ 一键安装与跨环境同步 (Quick Start)

当你在新电脑、物理机房服务器或新项目中，只需克隆本索引仓库，即可一键将全部技能分发就绪：

### 1. 克隆索引仓库
```bash
git clone git@github.com:Garfield247/agent-skills.git
cd agent-skills
```

### 2. 同步全量技能至 Antigravity / Gemini 全局库
```bash
python3 sync_skills.py --target global
# 自动下载并同步到 ~/.gemini/config/skills/
```

### 3. 或同步全量技能至当前开发项目本地工作区
```bash
cd /path/to/your-project
python3 /path/to/agent-skills/sync_skills.py --target local
# 自动下载并同步到当前项目的 .agents/skills/
```

---

## 📄 开源协议 (License)
本项目采用 [MIT License](LICENSE) 授权。
