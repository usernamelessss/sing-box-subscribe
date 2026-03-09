# sing-box-订阅

根据配置模板生成 sing-box 使用的 `config.json`。这主要用于为使用 `clash_mode` 配置的人添加订阅节点到配置中。

不适合完全不熟悉 sing-box 配置文件的人。至少你应该了解出站、DNS 服务器、DNS 规则和路由规则。最好了解 clash 的分组方法。

请参考：[http://sing-box.sagernet.org/configuration](http://sing-box.sagernet.org/configuration/)。

**SSR 协议脚本默认不解析。如果订阅链接包含 SSR 协议，将报错！！！**

**vercel 服务器处理时间上限为 10 秒。如果 clash 文件过大，因处理超时将失败！！！**

## 功能

**sing-box 网页解析器**

使用你搭建的网站实现实时配置更新，可作为 sing-box 的远程链接

例如，我搭建的网站 [https://sing-box-subscribe.vercel.app](https://sing-box-subscribe.vercel.app)，在网站后添加 `/config/URL_LINK`，这里 `URL_LINK` 指订阅链接

```
https://xxxxxxx.vercel.app/config/https://xxxxxxsubscribe?token=123456&file=https://github.com/Toperlock/sing-box-subscribe/raw/main/config_template/config_template_groups_rule_set_tun.json
```

### 2024.2.16 更新：支持在链接后添加 `emoji`、`tag`、`prefix`、`ua`、`file`、`eps` 、`enn` 参数。用 `&` 连接多个参数。用法同 `providers.json` 中的参数

`/config/URL_LINK&emoji=1&prefix=♥&ua=v2rayng&eps=vmess,hy2&enn=网站,剩余流量&file=https://xxxxxxxxx.json`

以上示例表示：启用 emoji，节点名前添加 ♥，使用 v2rayng UA，使用 `https://xxxxxxxxx.json` 作为生成的 sing-box 配置模板

示例：https://sing-box-subscribe.vercel.app/config/https://gist.githubusercontent.com/Toperlock/b1ca381c32820e8c79669cbbd85b68ac/raw/dafae92fbe48ff36dae6e5172caa1cfd7914cda4/gistfile1.txt&file = https://github.com/Toperlock/sing-box-subscribe/raw/main/config_template/config_template_groups_rule_set_tun.json

### 2023.11.04 更新：支持处理两个子链接，格式为：`/config/URL编码`，不支持写 `emoji`、`tag`、`prefix`、`UA` 参数（2024.1.1 起支持最多三个子链接）

用 `|` 连接两个子链接后进行 [URL 编码](https://www.urlencoder.org/)，放到 `config/` 后，如图：

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/5ed8e9de-3296-4dfc-ad65-2e181017829e" alt="how-to-use" width="50%" />
</div>

示例：https://sing-box-subscribe.vercel.app/config/https%3A%2F%2Fgist.githubusercontent.com%2FToperlock%2Fb1ca381c32820e8c79669cbbd85b68ac%2Fraw%2Fdafae92fbe48ff36dae6e5172caa1cfd7914cda4%2Fgistfile1.txt%7Chttps%3A%2F%2Fgist.githubusercontent.com%2FToperlock%2Ffa2fdc5f827ff7d288c23d568db75412%2Fraw%2F6c3b725da347f57b0021b806dfca5f51e1660746%2F1.yaml

### 2023.11.10 更新：`file` 参数可简写为数字，`1`、`2` 代表使用 github 仓库中提供的模板序号

示例：https://sing-box-subscribe.vercel.app/config/https://gist.githubusercontent.com/Toperlock/b1ca381c32820e8c79669cbbd85b68ac/raw/dafae92fbe48ff36dae6e5172caa1cfd7914cda4/gistfile1.txt&file = 2

### 演示视频

|网页解析订阅链接(v2/clash/sing-box)|
|-----------------------------|
|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/a583c443-0c7b-454e-aaf2-f0a7159b276a"> </video>|

## 目录

[操作视频](https://github.com/Toperlock/sing-box-subscribe/blob/main/instructions/README.md#-demonstration-video)

[参数含义](https://github.com/Toperlock/sing-box-subscribe/tree/main/instructions#providersjson-file)

[模板详细说明](https://github.com/Toperlock/sing-box-subscribe/tree/main/instructions#config-template-files)

[Windows 上运行 sing-box](https://github.com/Toperlock/sing-box-subscribe/tree/main/instructions#windows-sing-box-usage)

## 支持的协议

|  协议 | V2 订阅 | Clash 订阅 | 标准 URI 格式 | SingBox 格式 |
|  :----  | :----: | :----: | :----: | :----: |
| http  | ✅ | ✅ | ✅ | ✅ |
| socks5  | ✅ | ✅ | ✅ | ✅ |
| shadowsocks  | ✅ | ✅ | ✅ | ✅ |
| shadowsocksR  | ✅ | ✅ | ✅ | singbox 默认不支持 |
| vmess  | ✅ | ✅ | ✅ | ✅ |
| trojan  | ✅ | ✅ | ✅ | ✅ |
| vless  | ✅ | ✅ | ✅ | ✅ |
| tuic  | ✅ | ✅ | ✅ | ✅ |
| hysteria  | ✅ | ✅ | ✅ | ✅ |
| hysteria2  | ✅ | ✅ | ✅ | ✅ |
| wireguard  | ✅ | ✅ | ✅ | ✅ |

~不支持 clash 订阅解析~ 目前只实现了勾选协议的分享链接（**v2 或 clash 订阅格式**）解析。你可以自行编写协议解析器，比如 `vless.py`（文件名必须与协议名匹配），放在 `parsers` 目录，`vless.py` 文件必须包含一个 `parse` 函数。

**此脚本供个人使用。我使用 [yacd](https://yacd.metacubex.one)（iOS 请用 http://yacd.metacubex.one）管理节点切换（出站类型 `urltest` 和 `selector`）并像 clash 一样分流，非常方便。如果你也有类似需求，可以尝试。如果有新功能需求或使用中有错误，请提交 issue，切勿骚扰 sing-box。**

**脚本可部署至 vercel 服务器网页运行，或下载源码本地运行。请使用自己部署的网站生成 sing-box 配置。**

# 一、服务器部署

## 快速开始

1. 点击项目右上角的 fork 按钮，将项目 fork 到你自己的仓库；
2. 点击右侧按钮开始部署：
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)，并用 Github 账号直接登录；[详细教程见此](../docs/vercel-en.md#how-to-create-a-new-project)。
3. 部署完成即可开始使用；
4. （可选）[绑定自定义域名](https://vercel.com/docs/concepts/projects/domains/add-a-domain)：部分地区 Vercel 分配的域名 DNS 污染，绑定自定义域名直接连接。

### 开启自动更新

> 遇到 Upstream Sync 执行错误，请手动点击 Sync Fork 一次！

fork 项目后，由于 Github 限制，需要手动进入自己 fork 的项目 Actions 页面启用工作流和 Upstream Sync Action，开启每小时自动更新：

![AutoUpdate](https://github.com/Toperlock/ChatGPT-Next-Web/raw/main/docs/images/enable-actions.jpg)

![Enable Automatic Updates](https://github.com/Toperlock/ChatGPT-Next-Web/raw/main/docs/images/enable-actions-sync.jpg)

### 手动更新代码

如果想立刻启用手动更新，查阅 [Github 文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) 了解如何同步 fork 项目与上游代码。

你可以给项目 star/关注作者，接收新功能通知。

## 页面操作步骤

[示例网站](https://sing-box-subscribe.vercel.app/)。打开自己的部署网站，编辑右侧“编辑服务器 TEMP_JSON_DATA”框内容，点击“保存”，左上角选择配置模板，点击“生成配置文件”。👉🏻 [参数填写视图](https://github.com/Toperlock/sing-box-subscribe/tree/main/instructions#providersjson-file)

iOS 可用快捷指令复制网页内容，内容过多也可选择下载文件，自行解决文件后缀问题。👉🏻 [快捷指令安装](https://www.icloud.com/shortcuts/75fd371e0aa8438a89f715238a21ee68)

安卓用 Chrome 浏览器打开网页生成配置文件（请在浏览器设置 - 辅助功能中缩小网页），长按内容，全选后分享至代码编辑器，确认编辑器显示内容完整。👉🏻 [编辑器安装](https://mt2.cn/download/)

**注意保存后请尽快去“生成配置文件”，否则你填写的内容会留在网页上，别人打开网站可浏览，暂时没想到解决方法**

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/f794806c-edfc-4951-a216-6e38646f3791" alt="how-to-use" width="50%" />
</div>

## 🎬 演示视频

|网页解析订阅链接|网页解析 URI 链接|
|-----------------------------|-----------------------------|
|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/9f8f1a70-58b1-4117-a650-f956d9249e43"> </video>|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/63e180ad-eead-433f-8ee8-73055dafbd56"> </video>|

|安卓 Chrome 页面缩小|网页直接解析 base64|
|-----------------------------|-----------------------------|
|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/cb149206-307f-4de8-9968-9832dcf8268a"> </video>|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/0081f055-2cd4-46bb-a4a9-7aac7d5f93a5"> </video>|

|本地解析订阅链接|本地解析 URI 链接|
|-----------------------------|-----------------------------|
|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/12da95a3-aae9-4ae4-ab88-774ed54f3217"> </video>|<video controls width="250" src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/7e93568d-ece6-4cba-8dd0-bc5b5e64ade7"> </video>|

# 二、本地安装
### 在 PC 安装 [Python](https://www.python.org/) 3.10 及以上版本。确保将 Python 添加到系统环境变量（可谷歌查找安装步骤）。

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/f387322b-a602-40df-b3b6-95561329f2f8" alt="install" width="60%" />
</div>

### 终端输入下列命令安装依赖（Mac 替换 `pip` 为 `pip3`）：

```
pip install -r requirements.txt
```

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/0fc03b49-4c57-4ef3-a4fc-044c1a108d75" alt="install" width="60%" />
</div>

### 下载 `sing-box-subscribe` 项目，打开终端进入项目目录（可直接在文件路径输入 `cmd`）：

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/73f05ba8-105c-4f10-8e6c-16e27f26c084" alt="run" width="60%" />
</div>

### 将你的订阅链接填入 `providers.json`，编辑 `config_template_groups_tun.json` 文件，编辑模板后运行：

```
python main.py
```

或直接用 `template_index` 选择模板，`0` 表示第一个模板（无 flask 不支持）：

```
python main.py --template_index=0
```

Windows 系统建议将命令写入批处理程序执行。

使用前务必编辑 `providers.json` 和 `config_template` 目录的 `.json` 模板文件。

包含一个懒人配置 `config_template_groups_rule_set_tun`，可根据不同类别筛选节点：
* 实现 `Openai` 路由规则
* 实现 `Youtube` 路由规则
* 实现 `Google` 路由规则
* 实现 `Github` 路由规则
* 实现 `Telegram` 路由规则
* 实现 `Twitter` 路由规则
* 实现 `Facebook` 路由规则
* 实现 `Instagram` 路由规则
* 实现 `Bilibili` 路由规则
* 实现 `Bahamut` 路由规则
* 实现 `Spotify` 路由规则
* 实现 `TikTok` 路由规则
* 实现 `Netflix` 路由规则
* 实现 `Disney+` 路由规则
* 实现 `Apple` 路由规则
* 实现 `Amazon` 路由规则
* 实现 `Microsoft` 路由规则
* 实现 `Game` 路由规则
* 实现 `Hbo` 路由规则
* 实现 `Prime Video` 路由规则


# providers.json 文件
此文件可添加订阅链接及基础设置。
```json
{
    "subscribes":[
        {
            "url": "https://4gviet.com/api/v1/client/subscribe?token=xx",
            "tag": "airport1_tag", //可保持默认无需修改
            "enabled": true, //启用此链接转换
            "emoji": 1, //添加国旗 emoji
            "subgroup": "",
            "prefix": "", //不添加节点名前缀
            "ex-node-name": "网站|流量|过期", //过滤包含关键字节点
            "User-Agent":"clashmeta" //设置浏览器 UA
        },
        {
            "url": "https://5gtocdocao.com/api/v1/client/subscribe?token=xx",
            "tag": "airport2_tag", //可保持默认无需修改
            "enabled": false, //禁用此链接转换
            "emoji": 0, //不添加国旗 emoji
            "subgroup": "named", //给订阅链接命名
            "prefix": "❤️node_name prefix - ", //添加节点名前缀
            "User-Agent":"clashmeta" //设置浏览器 UA
        }
    ],
    "auto_set_outbounds_dns":{
        "proxy": "",
        "direct": ""
    },
    "save_config_path": "./config.json",
    "auto_backup": false,
    "exclude_protocol": "ssr", //不解析 ssr 节点！！！
    "config_template": "", //自定义正确的网页 json 配置模板链接
    "Only-nodes": false //输出完整 sing-box 配置
}
```
- `url`：必填。

> 支持设置常规 V2 订阅链接（**内容为 base64 编码**）

> 支持设置 clash 订阅链接

> 支持设置 sing-box 订阅链接

> 支持设置本地文件路径（**内容为标准 URI 链接或 Clash 字段**）

    以 `.txt` 结尾的本地文件，需在文件内逐行添加单节点分享链接，例如以 `ss://` 开头（非订阅链接）。
    
    以 `.yaml` 结尾的本地文件，正确填写 clash 的 proxies 字段。
    
    本地文件需保存在同一磁盘。路径格式如 `/Desktop/sing-box-subscribe/xx.txt` 或相对路径（与 `main.py` 在同一文件夹），如 `./xx.txt`。

- `tag`：必填。保持默认即可。

> 在配置模板中填写此标签以添加该订阅。此处的 "airport1_tag" 对应模板中的 `{机场1}`，具体用法见下文配置模板部分。

<details>
      <summary> tag 截图参考 </summary>

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/781c5bb7-c5c5-467e-a6ae-05ff44a19973" alt="download" width="65%" />
</div>

</details>

- `enabled`：可选。**设为 false，订阅将被忽略**。

- `emoji`：可选。**设为 false 或 0，节点名称不带国旗 emoji**。

- `subgroup`：可选。为订阅链接命名并生成出站。

- `prefix`：可选。设置自定义前缀，添加到节点名称前面。未设为无前缀。

- `ex-node-name`：可选。过滤包含关键字节点，多关键字用 `|` 分隔。

- `User-Agent`：可选。自定义 UA，例如设置为 "clash.meta" 或 "sing-box"。

<details>
      <summary> prefix 效果参考 </summary>

![Snipaste_2023-05-02_12-53-27](https://user-images.githubusercontent.com/21310130/235582317-6bb3d0a6-916f-445f-999b-f17b3db41eea.png)

</details>

- `auto_set_outbounds_dns`：可选。
> 包含 `proxy` 和 `direct` 设置。

> `proxy` 和 `direct` 应设置为配置模板文件中 `dns server` 的 `tag`。

> 设此选项，脚本将自动适配路由规则到 DNS 规则。

> 路由规则中带有 `direct` 设置的出站规则，DNS 服务器设置为指定的 `direct` 出站。

> 路由规则中需要代理的，设置为对应 `proxy` 出站，脚本自动创建对应 `proxy` 出站的 DNS 服务器，使用 `proxy` 设置的 DNS 服务器。

- `save_config_path`：必填。设置生成配置文件路径。

- `auto_backup`：可选。
> 设为 true 时，脚本会将当前使用的 sing-box 配置文件重命名为 `原文件名.当前时间.bak` 备份，防止生成错误配置需恢复。

- `exclude_protocol`：可选。
> 设置排除协议，逗号分隔，如 ssr, vmess。

> 使用此设置协议的分享链接将忽略。

> sing-box 官方版不支持 ssr（需额外参数构建），此设置可能有用。

- `config_template`：可选。输入正确的网页 json 配置模板链接，从模板生成 sing-box 配置。

- `Only-nodes`：可选。
> 设为 true 或 1 时，仅输出订阅链接的 sing-box 格式节点信息。

# 配置模板文件
脚本会在 `config_template` 目录查找 JSON 模板文件，可运行时选择使用哪个模板文件。

例如目录中有 `tun.json` 和 `socks.json` 模板文件。

![Snipaste_2023-03-24_22-16-49](https://user-images.githubusercontent.com/21310130/227548643-ffbf3825-9304-4df7-9b65-82a935227aef.png)

脚本不会验证模板文件正确性，模板错误会导致出错且脚本无法运行。

模板文件类似 sing-box 配置，但带有 `{all}`、`{机场tag}`（翻译为 `{airport_tag}`）、`filter` 等新参数，仅对 `clash_mode` 中的 `urltest` 和 `selector` 出站生效。
```json
{
  "tag":"proxy",
  "type":"selector",
  "outbounds":[
    "auto",
    "{all}"//所有订阅的所有节点都加入此标记位置
  ],
  "filter":[
    //此过滤器会移除 airport1_tag 中包含 ˣ² 的节点
    {"action":"exclude","keywords":["ˣ²"],"for":["机场1"]}
  ]
},
{
  "tag":"netflix",
  "type":"selector",
  "outbounds":[
    "{机场1}",//带 airport1_tag 的节点加入此标记位置
    "{机场2}"//带 airport2_tag 的节点加入此标记位置
  ],
  "filter":[
    //机场1和机场2中节点名含 'sg','新加坡','tw','台湾' 的节点统称为 netflix 组
    {"action":"include","keywords":["sg|新加坡|tw|台湾"]},
    //"for" 设置为 airport1_tag，表示该规则只对机场1生效
    {"action":"exclude","keywords":["ˣ²"],"for":["机场1"]}
    //此过滤器会移除 airport1_tag 中包含 ˣ² 的节点
  ]
}
```
- `{all}`：代表所有订阅所有节点。脚本会将所有节点添加至带此标识的 `outbounds`。

- `{机场tag}`（译为 `{airport_tag}`）：即 `providers.json` 中设置的机场 `tag`，代表此订阅的所有节点。

- `filter`：可选。节点过滤，数组对象，可任意添加规则，格式如下：
```json
"filter": [
    {"action": "include", "keywords": ["keyword1|keyword2"]},
    {"action": "exclude", "keywords": ["keyword1|keyword2"], "for": ["airport1_tag", "airport2_tag"]}
  ]
```
- **关键字区分大小写**

- `include`：添加保留关键字，用 `|` 连接多个关键词，包含关键词的节点保留，其他删除。

- `exclude`：添加排除关键字，用 `|` 连接多个关键词，包含关键词的节点删除，其他保留。

- `for`：可选。设置机场 `tag`，可多选。此规则只作用于指定机场，其他忽略。

多条规则按顺序执行。

# Windows sing-box 使用

1. 下载 Windows 客户端程序 [sing-box-windows-amd64.zip](https://github.com/SagerNet/sing-box/releases)。
2. 新建 `.bat` 批处理文件，内容为 `start /min sing-box.exe run`。
3. 参考 [客户端配置](https://github.com/chika0801/sing-box-examples/blob/main/Tun/config_client_windows.json) 示例，按需修改，改名为 **config.json**，将批处理文件放与 **sing-box.exe** 同文件夹。
4. 右键 **sing-box.exe**，选择属性，兼容性里选择以管理员身份运行程序。
5. 运行批处理，弹出用户账户控制时选择是。

## 隐藏 Windows 运行 sing-box 弹出的 cmd 窗口

> 使用 WinSW 设置 sing-box.exe 作为 Windows 服务，[WinSW 教程](https://github.com/winsw/winsw)

> XML 配置文件修改示例
```xml
<service>
  <id>sing-box</id>
  <name>sing-box</name>
  <description>sing-box 服务</description>
  <executable>./sing-box.exe</executable>
  <log mode="reset"></log>
  <arguments>run</arguments>
</service>
```
<details>
      <summary> Windows sing-box 文件夹内容 </summary>

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/c6a815bf-b542-43c6-aeb6-84020586a1f1" alt="download" width="50%" />
</div>

</details>

## 非图形化客户端无 tun 操作

例如，Windows 内核运行 sing-box 时，删除入站的 tun 字段：

```json
"inbounds": [
    {
      "type": "mixed",
      "listen": "127.0.0.1",
      "listen_port": 2080, //此端口须与 Windows 代理端口一致
      "sniff": true,
      "set_system_proxy": true,
      "sniff_override_destination": false,
      "domain_strategy": "ipv4_only"
    }
  ]
```

<div align="left">
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/387f2077-b8b6-42ed-9658-361b28179db2" alt="download" width="50%" />
</div>

<details>
      <summary> <b> 效果参考 </b> </summary>

具体效果取决于各出站和规则设置。

<div align="left">
  <img src="https://user-images.githubusercontent.com/21310130/227577941-01c80cfc-1cd9-4f95-a709-f5442a2a2058.png" alt="download" width="50%" />
  <img src="https://user-images.githubusercontent.com/21310130/227577968-6747c7aa-db61-4f6c-b7cc-e3802e34cc3d.png" alt="download" width="50%" />
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/955968d7-98e7-4bd2-a582-02576877dba1" alt="download" width="50%" />
  <img src="https://github.com/Toperlock/sing-box-subscribe/assets/86833913/9e7c35ff-c6c4-46c4-a74b-624ff72c17ea" alt="download" width="50%" />
</div>

</details>

# 鸣谢
- [xream](https://github.com/xream)
- [sing-box](https://github.com/SagerNet/sing-box)
- [yacd](https://github.com/haishanh/yacd)
- [clash](https://github.com/Dreamacro/clash)
- [sing-box-examples@chika0801](https://github.com/chika0801/sing-box-examples)

部分协议解析参考 [convert2clash](https://github.com/waited33/convert2clash)。

部分 clash2v2ray 解析参考 [clash2base64](https://github.com/yuanyiwei/toys/blob/master/DEPRECATED/clash/clash2base64.py)。

部分同步代码参考 [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web)。

感谢 @SayRad 提供越南语翻译