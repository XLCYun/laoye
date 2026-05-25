# 老爷（laoye）

蒸馏玉帝老爷，可向老爷提问。添加求签功能。通过真实掷茭杯，从玉帝二十八签中抽取对应签文，再结合用户当下的问题给出解读。

- 使用随机掷茭杯流程
- 使用玉帝二十八星宿签
- 先出签面，再解签意，再落到当前问题

## 前置要求

- 可用的 AI Agent 环境
- 已安装 `python3`
- 如使用 Skills CLI，需可执行 `npx skills`

## 安装方式一：`npx skills add`

如果你使用的是支持 Skills CLI 的 Agent，推荐直接安装：

```bash
npx skills add XLCYun/laoye --skill laoye -g -a codex -y
```

参数说明：

- `--skill laoye`：只安装这个技能
- `-g`：全局安装，当前用户下所有项目可用
- `-a codex`：安装到 Codex
- `-y`：跳过交互确认

如果你想先查看仓库里有哪些技能，也可以先运行：

```bash
npx skills add XLCYun/laoye --list
```

## 安装方式二：`git clone`

如果你不想走 Skills CLI，也可以手动安装。

先克隆仓库：

```bash
git clone https://github.com/XLCYun/laoye.git
```

然后把仓库里的 `skills/laoye` 放到你的 Agent 技能目录中。以 Codex 为例：

```bash
ln -s /path/to/laoye/skills/laoye ~/.codex/skills/laoye
```

如果你不想使用软链接，也可以直接复制目录：

```bash
cp -R /path/to/laoye/skills/laoye ~/.codex/skills/laoye
```

完成后，重启 Agent 或重新打开当前工作区。

## 技能会如何工作

当问题适合通过求签来回答时，这个技能会按下面的流程运行：

1. 读取玉皇大帝人格设定
2. 运行 `python3 scripts/jiaobei.py`
3. 先判极低概率的立杯，否则掷三次茭杯
4. 从玉帝二十八签中抽取对应签文
5. 先展示签面，再结合你当前的问题解签

输出通常包含：

- 签面
- 断曰
- 结合当前问题的解释与提醒

## 目录结构

```text
skills/laoye/
├── SKILL.md
├── data/yudi_lingqian_all_28.json
├── references/玉皇大帝人格.md
└── scripts/jiaobei.py
```

## 说明

-  仅供娱乐，求签为随机过程，请勿迷信

