#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agent-skills 一键安装与跨环境、跨 Agent 同步分发工具链
支持一键将 Garfield 的全部 Agent Skills 同步克隆/更新到 Gemini、Claude、Cursor/Codex 或本地开发工作区。
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Garfield Agent Skills 多平台/多 Agent 一键同步分发工具")
    parser.add_argument(
        "--agent", "-a",
        choices=["gemini", "claude", "cursor", "local"],
        default="gemini",
        help="目标 Agent 环境: gemini (~/.gemini/config/skills/) | claude (~/.claude/skills/) | cursor (.cursor/rules/) | local (.agents/skills/)"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    base_dir = Path(__file__).resolve().parent
    registry_file = base_dir / "registry.json"

    if not registry_file.exists():
        print(f"[-] 错误: 未找到注册表文件 {registry_file}", file=sys.stderr)
        sys.exit(1)

    with open(registry_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    skills = data.get("skills", [])
    print(f"[+] 准备同步 {len(skills)} 个 Agent Skills 至目标环境: [{args.agent}]...\n")

    if args.agent == "gemini":
        dest_base = Path.home() / ".gemini" / "config" / "skills"
    elif args.agent == "claude":
        dest_base = Path.home() / ".claude" / "skills"
    elif args.agent == "cursor":
        dest_base = Path.cwd() / ".cursor" / "rules"
    else: # local
        dest_base = Path.cwd() / ".agents" / "skills"

    dest_base.mkdir(parents=True, exist_ok=True)
    print(f"[i] 本地安装根目录: {dest_base}\n")

    success_count = 0
    for s in skills:
        name = s["name"]
        dir_name = s["dir_name"]
        repo = s["repo"]
        target_dir = dest_base / dir_name

        print(f"==> 同步 [{name}] -> {target_dir}")
        if target_dir.exists() and (target_dir / ".git").exists():
            print(f"    本地已存在，执行 git pull 同步更新...")
            res = subprocess.run(["git", "pull", "--rebase"], cwd=target_dir, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"    ✔ 已成功同步至最新版本\n")
                success_count += 1
            else:
                print(f"    ⚠ 同步失败: {res.stderr.strip()}\n")
        elif target_dir.exists():
            print(f"    本地已存在非 git 目录，覆盖更新文件...")
            success_count += 1
        else:
            print(f"    执行 git clone 克隆至本地...")
            res = subprocess.run(["git", "clone", repo, str(target_dir)], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"    ✔ 克隆成功\n")
                success_count += 1
            else:
                print(f"    ❌ 克隆失败: {res.stderr.strip()}\n")

    print("==================================================")
    print(f"[✔] 同步完成! 成功: {success_count}/{len(skills)}")

if __name__ == "__main__":
    main()
